from bs4 import BeautifulSoup
import urllib.request

#this table specifically
#https://www.footballdb.com/players/tom-brady-bradyto01/gamelogs/2014
def parse_table(table):
	#2d array of table to return at the end
	table_arr = list()

	#get the header information
	
	#the thead returns an array of 1 object, but to perform the next operation, we can't have the array
	#the column names is in the second tr
	row = table.findChildren('thead')[0].findChildren('tr')[1].findChildren('th')
	
	#temporary 1d array to store each row, then push to table_arr
	row_arr = list()
	
	for item in row:
		row_arr.append(item.getText())
	
	table_arr.append(row_arr)
	
	#getting the the rows with data
	#since there is only 1 tbody in the table, have to get the first element in the array
	data_rows = table.findChildren("tbody")[0].findChildren('tr')
	
	for row in data_rows:
		row_classes = row.get("class")
		if "preseason" in row_classes:
			#ignoring preseason
			continue
		elif "postseason" in row_classes:
			#ignoring postseason
			continue
		else:
			#if it's a normal season game
			
			#reset row array
			row_arr = list()
			
			#get the row's td
			columns = row.findChildren("td")
			#the first element is the date, but it contains a hyperlink
			
			row_arr.append(columns[0].findChildren("a")[0].getText())
			
			#get the rest of the columns
			#the last one contains the outcome of the game which will be dealt with by another scrub
			for col in columns[1:-1]:
				row_arr.append(col.getText())
			table_arr.append(row_arr)
	
		
	return table_arr