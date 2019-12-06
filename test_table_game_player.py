from get_roster import player_stats_handler
from get_roster import get_home_away
from get_roster import split_score
from get_roster import get_player_id_list
import csv
import json

# player_list = {"Tom Brady": 1153}
# player_dict = get_player_id_list()
start_year = 2018
num_years = 1


# main_list = player_stats_handler(player_dict, start_year, num_years)

with open("player_data_list.json") as readFile:
    main_list = json.load(readFile)
readFile.close()



entire_list = list()

# with open('player_data_list.json', 'w') as fp:
#     json.dump(main_list, fp)
# fp.close()


for player_name, year_n_data in main_list.items():
      

    year = year_n_data[0]
    data = year_n_data[1]

    if(data == None):
        print("data none")
    else:

        for table_type, head_n_type_data in data.items():

            headers = head_n_type_data["headers"]
            type_data = head_n_type_data["data"]

            for game_data in type_data:
                #[home_team, away_team]
                home_away_arr = get_home_away(game_data[1], game_data[2])
                game_date = game_data[0]

                game_score_str = game_data[-1]

                #[home_score, away_score]
                score_arr = split_score(game_score_str)
                
                #[date, home_team, away_team, home_score, away_score, year]
                new_entry = [game_data[0], home_away_arr[0], home_away_arr[1], score_arr[0], score_arr[1], year]

                if(new_entry not in entire_list):
                    entire_list.append(new_entry)
            


# print(entire_list)

#now write to file
with open("temp_game_translation.csv", "w", newline='') as writeFile:
    writer = csv.writer(writeFile)
    
    writer.writerows(entire_list)

writeFile.close()