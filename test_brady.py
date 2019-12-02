from bs4 import BeautifulSoup
import urllib.request
from get_table import parse_table
import csv
import time


#starting year
year = 2000

#main list that will be put out to file
main_list = {}
main_list.update({"player": "Tom Brady"})

#how many years to go for
for x in range(0, 1):
	current_year = year+x
	print(current_year)
	with urllib.request.urlopen('https://www.footballdb.com/players/tom-brady-bradyto01/gamelogs/' + str(current_year)) as response:
		html = response.read()
		
	soup = BeautifulSoup(html, 'lxml')
	
	#if this object has children (i.e. the list isn't empty) then the page has actual data
	if soup.find("div", {"id": "divToggle_P"}).findChildren():
		tables = soup.find_all("table")

		table_order = ["passing","rushing","punting","receiving","scoring","defense"]
		i=0
		
		#the return values of the parse_table
		return_tables = {}
		for table in tables:
			
			#parse table returns an 2d array of pages tables
			return_tables.update({table_order[i]: parse_table(table)})
			i += 1
		
		# print(return_tables)
		main_list.update({current_year: return_tables})
		# print(type({current_year: return_tables}))
	
	#sleep for one second so the website isn't bombarded
	time.sleep(1)


with open('tom_brady.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow(["player", main_list["player"]])
	del main_list["player"]
	for key in main_list:
		writer.writerow(["year", key])
		year_list = main_list[key]
		
		for table_key in year_list:
			writer.writerow(["table_type", table_key])
			
			table_list = year_list[table_key]
			for table_row in table_list:
				writer.writerow(table_row)
writeFile.close()

# print(main_list["player"])
# del main_list["player"]
# #for each year
# for key in main_list:
	# print("*****************")
	# print(key)
	# print("--")
	# year_list = main_list[key]
	
	# #for each type of table in year
	# for year_key in year_list:
		# print(year_key)
		# print(">>>>>>>>")
		# # print(type(year_list[year_key]))
		# # print(year_list[year_key])
		
		# table_list = year_list[year_key]
		# #for each row in table
		# for table_row in table_list:
			# print(table_row)
		
	# print("*****************")

# with open('tom_brady.csv', 'w') as writeFile:
	# writer = csv.writer(writeFile)
	# writer.writerow(main_list['player'])
	# writer.writerow(main_list['player'])
	# for item in main_list:
		# writer.writerows(item)
# writeFile.close()
			

