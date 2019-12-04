import json
import csv


def write_coaches():
    coach_id_list = list()
    coach_team_list = list()

    with open("raw_data.json") as json_file:
        data = json.load(json_file)

    i = 0
    
    for item in data:
        #get each of the coaches from the team
        if(item["HeadCoach"] != None):
            if item["HeadCoach"] not in coach_id_list:
                #[coach name, cid]
                coach_id_list.append([item["HeadCoach"], i])
                #[cid, team_code, ctype, year]
                coach_team_list.append([i, item["Key"].lower(), "head coach", item["Year"]])
                i += 1
        if(item["OffensiveCoordinator"] != None):
            if item["OffensiveCoordinator"] not in coach_id_list:
                coach_id_list.append([item["OffensiveCoordinator"], i])
                coach_team_list.append([i, item["Key"].lower(), "offensive coordinator", item["Year"]])
                i += 1
        if(item["DefensiveCoordinator"] != None):
            if item["DefensiveCoordinator"] not in coach_id_list:
                coach_id_list.append([item["DefensiveCoordinator"], i])
                coach_team_list.append([i, item["Key"].lower(), "defensive coordinator", item["Year"]])
                i += 1
        if(item["SpecialTeamsCoach"] != None):
            if item["SpecialTeamsCoach"] not in coach_id_list:
                coach_id_list.append([item["SpecialTeamsCoach"], i])
                coach_team_list.append([i, item["Key"].lower(), "special teams", item["Year"]])
                i += 1
    

    # print(coach_list)
    with open("table_coach.csv", "w", newline='') as writeFile:
        writer = csv.writer(writeFile)
	
        writer.writerows(coach_id_list)

    writeFile.close()

    with open("table_coach_team.csv", "w", newline='') as writeFile:
        writer = csv.writer(writeFile)
	
        writer.writerows(coach_team_list)

    writeFile.close()

# def write_coach_team():

#     coach_id_list = {}

#     with open("all_players.csv", "r") as readFile:
#         csv_reader = csv.reader(readFile, delimiter=",")
        
#         for row in csv_reader:
#             coach_id_list.update({row[0]: row[1]})
    
#     with open("raw_data.json") as json_file:
#         data = json.load(json_file)

#     i = 0
    
#     for item in data:
#         #get each of the coaches from the team
#         if(item["HeadCoach"] != None):
#             coach_id_list[]
#                 coach_list.append([item["HeadCoach"], i])
#                 i += 1
#         if(item["OffensiveCoordinator"] != None):
#             if item["OffensiveCoordinator"] not in coach_list:
#                 coach_list.append([item["OffensiveCoordinator"], i])
#                 i += 1
#         if(item["DefensiveCoordinator"] != None):
#             if item["DefensiveCoordinator"] not in coach_list:
#                 coach_list.append([item["DefensiveCoordinator"], i])
#                 i += 1
#         if(item["SpecialTeamsCoach"] != None):
#             if item["SpecialTeamsCoach"] not in coach_list:
#                 coach_list.append([item["SpecialTeamsCoach"], i])
#                 i += 1


# 	readFile.close()