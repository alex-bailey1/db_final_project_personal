from get_roster import player_stats_handler
from get_roster import get_player_id_list
import csv

roster = get_player_id_list()

url_list = player_stats_handler(roster, 2018, 1)

with open("temp_url.csv", "w") as writeFile:
	writer = csv.writer(writeFile)
	
	for url in url_list:
		writer.writerow([url])
writeFile.close()