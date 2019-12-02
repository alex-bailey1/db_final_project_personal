from bs4 import BeautifulSoup
import urllib.request
import csv
import time
from get_table import parse_table

#gets roster of the given team

#this roster
#http://www.jt-sw.com/football/pro/rosters.nsf/Annual/2013-buf
def get_roster(year_start, year_count, team_code):
	url_base = r"http://www.jt-sw.com/football/pro/rosters.nsf/Annual/"
	
	main_list = {}
	main_list.update({ "team": team_code})
	for i in range(0, year_count):
		current_year = year_start + i
		full_url = url_base + str(current_year) + "-" + team_code
		
		with urllib.request.urlopen(full_url) as response:
			html = response.read()
		# print("html length: " + str(len(html)))
		soup = BeautifulSoup(html, 'lxml')
		
		#the second table is the one we want
		table = soup.find_all("table")[1]

		data_list = list()
		
		if "headers" not in main_list:
			headers = table.find_all("th")
			head_list = list()
			for head_item in headers:
				head_list.append(head_item.getText())
			
			main_list.update({"headers": head_list})
		
		
		
		table_data = table.find_all("tr")[1:]
		# table_data = table.find_all("tr")
		
		for row in table_data:
			row_list = list()
			for item in row:
				row_list.append(item.getText())
			
			data_list.append(row_list)
		
		main_list.update({ str(current_year): data_list})
		
		#sleep for 1 second so we don't bombard the website
		time.sleep(1)
		
	return main_list


def get_player_id_list():

	entire_list = {}
	
	with open("all_players.csv", "r") as readFile:
		csv_reader = csv.reader(readFile, delimiter=",")
		
		for row in csv_reader:
			#every other row is black
			if row:				
				entire_list.update({ row[0]: row[1]})
	readFile.close()
	
	# for p_name, pid in entire_list.items():
		# print(p_name + "->" + pid)
		
	
	return entire_list

#get one year of player stats
#also parses the tables
def get_player_stats(full_url):	
	return_tables = {}
	
	with urllib.request.urlopen(full_url) as response:
		html = response.read()
		
	soup = BeautifulSoup(html, 'lxml')
	
	#list of the div IDs for the various tables and what they actually represent
	id_translation = ({ 
	"divToggle_R": "rushing", 
	"divToggle_P": "passing", 
	"divToggle_C": "receiving", 
	"divToggle_D": "defense", 
	"divToggle_U": "punting", 
	"divToggle_S": "scoring",
	"divToggle_KR": "kickoff_returns",
	"divToggle_PR": "punt_returns"
	})
	
	for table_div_id, div_id_translation in id_translation.items():
		soup_div_return = soup.find("div", {"id": table_div_id})
		
		#if soup_div_return isn't empty, there's data to look at
		#the website will generate a page for a given year, but there just won't be any tables
		if soup_div_return:
			#the second tr has the headers we want
			headers = soup_div_return.find("thead").findChildren("tr")[1]
			
			header_list = list()
			for head in headers:
				header_list.append(head.getText())
				
			return_tables.update({div_id_translation: {}})
			return_tables[div_id_translation].update({"headers": header_list})

			data_rows = soup_div_return.find("tbody").findChildren("tr")
			#for storing the 2d data
			data_table = list()
			
			for data_row in data_rows:
				row_classes = data_row.get("class")
				if "preseason" in row_classes:
					#ignoring preseason
					continue
				elif "postseason" in row_classes:
					#ignoring postseason
					continue
				else:
					row_data = list()
					columns = data_row.findChildren("td")
					
					for col in columns:
						row_data.append(col.getText())
					
					data_table.append(row_data)
			
			return_tables[div_id_translation].update({"data": data_table})
			
	return return_tables
			
	
	

#passes the url to the stats getting function
def player_stats_handler(player_list, start_year, num_years):

	base_url = 'https://www.footballdb.com/players/'
	
	main_list = []
	
	for player in player_list:
		for i_year in range(0, num_years):
		
			p_name_split = player.split()
			current_year = start_year + i_year
			
			#if there are more than 2 words in the name, they're probably s special case. e.g. T. J. Yates
			if(len(p_name_split) != 2):
				#name is a special case
				temp_skip = True
			else:	
				#name is not a special case
				first = p_name_split[0].lower()
				last =  p_name_split[1].lower()
				
				#if the last name has more than 5 letters
				if (len(last) > 5):
					name_combo = last[0:5] + first[0:2] + "01"
				else:
					name_combo = last + first[0:2] + "01"
				
				#only missing the year
				full_url = base_url + first + "-" + last + "-" + name_combo + "/gamelogs/" + str(current_year)
				
				main_list.update({current_year: get_player_stats(full_url) })
				
				
				
	return main_list



	
	
	
	
	
	
	
	
	
	
	