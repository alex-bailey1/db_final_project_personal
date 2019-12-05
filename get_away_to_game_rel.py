import csv

def get_home_to_game_rel():
    rel_list = list()

    with open("game_weather.csv", "r") as readFile:
        csv_reader = csv.reader(readFile, delimiter=",")

        # print(csv_reader)
        
		
        for row in csv_reader:
            rel_list.append([row[0], row[0], row[1], row[2], row[2], row[3]])

    readFile.close()

    with open("table_home_to_game.csv", "w", newline='') as writeFile:
        writer = csv.writer(writeFile)
		
        writer.writerows(rel_list)

    writeFile.close()


def get_away_to_game_rel():
    rel_list = list()

    with open("game_weather.csv", "r") as readFile:
        csv_reader = csv.reader(readFile, delimiter=",")

        # print(csv_reader)
        
		
        for row in csv_reader:
            rel_list.append([row[0], row[0], row[1], row[3], row[3], row[2]])

    readFile.close()

    with open("table_away_to_game.csv", "w", newline='') as writeFile:
        writer = csv.writer(writeFile)
		
        writer.writerows(rel_list)

    writeFile.close()

get_away_to_game_rel()