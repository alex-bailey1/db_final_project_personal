from get_roster import get_player_id_list

entire_list = get_player_id_list()

for p_name, pid in entire_list.items():
	print(p_name + "->" + pid)