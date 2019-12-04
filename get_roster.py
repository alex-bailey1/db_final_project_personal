from bs4 import BeautifulSoup
import urllib.request
import csv
import time
from get_table import parse_table


#gets roster of the given team

#this roster
#http://www.jt-sw.com/football/pro/rosters.nsf/Annual/2013-buf
#team_code is actually the translation for the url and isn't always the actual team code
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
		
		#sleep for .5 seconds so we don't bombard the website
		time.sleep(.5)
		
	return main_list

#actually returns a dictionary
def get_player_id_list():

	entire_list = {}
	
	with open("all_players.csv", "r") as readFile:
		csv_reader = csv.reader(readFile, delimiter=",")
		
		for row in csv_reader:
			#every other row is blank
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
	# print(full_url)
	try:
		with urllib.request.urlopen(full_url) as response:
			html = response.read()
	except Exception as ex:
		# print("html exception")
		# print(template.format(type(ex).__name__, ex.args))
		return None
		
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
			
			
			
			#for storing the 2d data
			data_table = list()

			
			thead = soup_div_return.find("thead")
			#occasionally, there will be a div with the correct id, but nothing in it
			if(thead):
				#the second tr has the headers we want
				headers = thead.findChildren("tr")[1]
				
				header_list = list()
				for head in headers:
					header_list.append(head.getText())
					
				return_tables.update({div_id_translation: {}})
				return_tables[div_id_translation].update({"headers": header_list})

				data_rows = soup_div_return.find("tbody").findChildren("tr")
				
				
				
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
	
	main_list = {}

	#for some of the urls, there are 2 players with that name, so they use 02 in the 'name_combo' instead of 01
	player_number_url_exceptions = [["mason", "cole"]]
	
	for player in player_list:
		for i_year in range(0, num_years):
		
			p_name_split = player.split()
			current_year = start_year + i_year
			
			#if there are more than 2 words in the name, they're probably s special case. e.g. T. J. Yates
			if(len(p_name_split) != 2):
				#name is a special case
				# temp_skip = True
				continue
			else:	
				#name is not a special case
				first = p_name_split[0].lower()
				last =  p_name_split[1].lower()
				
				#when there are repeat names, the number_code is switched to 02
				if([first, last] in player_number_url_exceptions):
					# print("number_code: 02")
					number_code = "02"
				else:
					number_code = "01"


				#if the last name has more than 5 letters
				if (len(last) > 5):
					name_combo = last[0:5] + first[0:2] + number_code
				else:
					name_combo = last + first[0:2] + number_code
				
				#only missing the year
				full_url = base_url + first + "-" + last + "-" + name_combo + "/gamelogs/" + str(current_year)
				
				main_list.update({current_year: get_player_stats(full_url) })
		time.sleep(.5)
				
				
				
	return main_list


# #not all the websites abreviations are correct, this changes the real abbreviation to the websites version {actual_abrev: website_abrv}
# team_abrev_translation = {'ari': 'arz', 'atl': 'atl', 'bal': 'bal', 'buf': 'buf', 'car': 'car', 'chi': 'chi', 'cin': 'cin', 'cle': 'cle', 'dal': 'dal', 'den': 'den', 'det': 'det', 'gb': 'gb', 'hou': 'hou', 'ind': 'ind', 'jax': 'jac', 'kc': 'kc', 'mia': 'mia', 'min': 'min', 'ne': 'ne', 'no': 'no', 'nyg': 'nyg', 'nyj': 'nyj', 'oak': 'oak', 'phi': 'phi', 'pit': 'pit', 'sf': 'sf', 'sea': 'sea', 'tb': 'tb', 'ten': 'ten', 'was': 'was'}

# #for reference
# headers = ['pos', '#', '', 'player', 'gp', 'gs', 'start pos', 'exp', 'dob', 'ht', 'wt', 'college']

def write_team_player_table(team_abrv_trans_list, start_year, num_years):

	csv_list_before_id = list()

	for team_code, translation in team_abrv_trans_list.items():
		roster = get_roster(start_year, num_years, translation)

		del roster["team"]
		del roster["headers"]

		for key_year, year_data in roster.items():
			for row in year_data:
				#[player_name, player_pos, player_#, team_code]
				csv_list_before_id.append([row[3], get_only_one_pos(row[0]), row[1], team_code])
	
	# print(csv_list_before_id)

	#now replace all the player name with the their id
	csv_with_id = list()

	id_dictionary = get_player_id_list()

	for player_row in csv_list_before_id:
		pid = id_dictionary[player_row[0]]
		csv_with_id.append([pid, player_row[1], player_row[2], player_row[3]])
	
	
	#now write to file
	with open("team_player_table.csv", "w", newline='') as writeFile:
		writer = csv.writer(writeFile)
		
		writer.writerows(csv_with_id)

	writeFile.close()


#some players have multiple positions on the team, this returns one of them
def get_only_one_pos(pos_string):
	string_arr = pos_string.split("/")
	return string_arr[0]


	
	
	
	
	
	
	
	
	
	