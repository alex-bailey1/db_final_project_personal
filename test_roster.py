from get_roster import get_roster
from get_roster import get_player_stats
from get_roster import get_player_id_list
from get_roster import get_player_stats

player_list = get_player_id_list()

player_data_list = player_stats_handler(player_list, 2018, 1)

for year_key, year_data in player_data_list.items():
	print(year)

 
# return_table = get_player_stats("https://www.footballdb.com/players/tom-brady-bradyto01/gamelogs/2014")

# print(return_table)
# for table_type, table_headers_data in return_table.items():
	# print("***********")
	# print(table_type)
	# print("-----------")	
	# print(table_headers_data["headers"])
	# print(">>>>>>>>>>>>")
	# data = table_headers_data["data"]
	# for row in data:
		# print(row)
	