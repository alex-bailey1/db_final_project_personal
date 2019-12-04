from get_roster import get_roster
import csv
 
#not all the websites abreviations are correct, this changes the real abbreviation to the websites version {actual_abrev: website_abrv}
team_abrev_translation = {'ari': 'arz', 'atl': 'atl', 'bal': 'bal', 'buf': 'buf', 'car': 'car', 'chi': 'chi', 'cin': 'cin', 'cle': 'cle', 'dal': 'dal', 'den': 'den', 'det': 'det', 'gb': 'gb', 'hou': 'hou', 'ind': 'ind', 'jax': 'jac', 'kc': 'kc', 'mia': 'mia', 'min': 'min', 'ne': 'ne', 'no': 'no', 'nyg': 'nyg', 'nyj': 'nyj', 'oak': 'oak', 'phi': 'phi', 'pit': 'pit', 'sf': 'sf', 'sea': 'sea', 'tb': 'tb', 'ten': 'ten', 'was': 'was'}

#for reference
headers = ['pos', '#', '', 'player', 'gp', 'gs', 'start pos', 'exp', 'dob', 'ht', 'wt', 'college']

entire_list = {}

id_num = 0

star_year = 2018
num_years = 1

# for team in team_abrev_list:
# for team in ['ari', 'atl']:
for team, translation in team_abrev_translation.items():
	#for console tracking
	print(team)
	
	# roster = get_roster(star_year, num_years, team_abrev_translation[team])
	roster = get_roster(star_year, num_years, translation)
	#for tracking of program	
	
	#remove these as they aren't needed for all players
	del roster["team"]
	del roster["headers"]
	
	for key_year, year_data in roster.items():
		for row in year_data:
			player_name = row[3]
			player_dob = row[8]
			
			#if player name isn't already in list
			if player_name not in entire_list:
				entire_list.update({player_name: [player_dob, id_num]})
				id_num += 1
			#if the player name is in the list and the birthday matchs, player is already in database (assume there are no 2 players with the same name and date of birth
			elif player_name in entire_list:
				if player_dob in entire_list[player_name]:
					# print("same player")
					continue
			#player name matches, but birthday doesn't, 2 separate players
			else:
				# print("same name")
				entire_list.update( {player_name: [player_dob, id_num]} )
				id_num += 1

with open("all_players.csv", "w", newline='') as writeFile:
	writer = csv.writer(writeFile)
	
	for player_name, player_dob_id in entire_list.items():
		writer.writerow([player_name, player_dob_id[1]])

writeFile.close()
		
		

		
		
		
