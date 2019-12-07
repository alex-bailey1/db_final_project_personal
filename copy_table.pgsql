COPY game_stats(Date, Season, Week, team_code, Opponent, HomeOrAway, Score, OpponentScore, Stadium, PlayingSurface, TimeOfPossession, FirstDowns, OffensivePlays, OffensiveYards, Touchdowns, RushingAttempts, RushingYards, RushingTouchdowns, PassingAttempts, PassingCompletions, PassingYards, PassingTouchdowns, PassingInterceptions, CompletionPercentage, Fumbles, FumblesLost, TimesSacked, TimesSackedYards, Punts, PuntYards, Giveaways, Takeaways, TurnoverDifferential, OpponentTimeOfPossession, OpponentFirstDowns, OpponentOffensivePlays, OpponentOffensiveYards, OpponentRushingAttempts, OpponentRushingYards, OpponentCompletionPercentage, OpponentPenalties, OpponentPenaltyYards, OpponentFumbles, OpponentFumblesLost, OpponentTimesSacked, FieldGoalAttempts, FieldGoalsMade, PuntReturns, PuntReturnYards, KickReturns, KickReturnYards, OpponentPuntReturns, OpponentPuntReturnYards, OpponentKickReturns, OpponentKickReturnYards, Sacks, SackYards, TeamName, DayOfWeek, Day, DateTime) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\game_stats_short.csv' CSV HEADER DELIMITER ','; 

--COPY home_game_stats(Date, Season, Week, team_code, Opponent, HomeOrAway, Score, OpponentScore, Stadium, PlayingSurface, TimeOfPossession, FirstDowns, OffensivePlays, OffensiveYards, Touchdowns, RushingAttempts, RushingYards, RushingTouchdowns, PassingAttempts, PassingCompletions, PassingYards, PassingTouchdowns, PassingInterceptions, CompletionPercentage, Fumbles, FumblesLost, TimesSacked, TimesSackedYards, Punts, PuntYards, Giveaways, Takeaways, TurnoverDifferential, OpponentTimeOfPossession, OpponentFirstDowns, OpponentOffensivePlays, OpponentOffensiveYards, OpponentRushingAttempts, OpponentRushingYards, OpponentCompletionPercentage, OpponentPenalties, OpponentPenaltyYards, OpponentFumbles, OpponentFumblesLost, OpponentTimesSacked, FieldGoalAttempts, FieldGoalsMade, PuntReturns, PuntReturnYards, KickReturns, KickReturnYards, OpponentPuntReturns, OpponentPuntReturnYards, OpponentKickReturns, OpponentKickReturnYards, Sacks, SackYards, TeamName, DayOfWeek, Day, DateTime) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\home_stats.csv' CSV HEADER DELIMITER ','; 

COPY games(Year, Week, Home_Team, Away_Team, Network, Weather, Description, Wind, Away_Score, Home_Score, Temp) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\game_weather.csv' CSV HEADER DELIMITER ','; 

COPY teams(team_code, Name, Conference, Division, FullName, HeadCoach, OffensiveCoordinator, DefensiveCoordinator, SpecialTeamsCoach, OffensiveScheme, DefensiveScheme, StadiumName, Year) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\team_data_2018.csv' CSV HEADER DELIMITER ','; 

COPY teams(team_code, Name, Conference, Division, FullName, HeadCoach, OffensiveCoordinator, DefensiveCoordinator, SpecialTeamsCoach, OffensiveScheme, DefensiveScheme, StadiumName, Year) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\team_missing_years.csv' CSV HEADER DELIMITER ','; 

insert into teams values('SD','Chargers','','','','','','','','','','',2013);
insert into teams values('SD','Chargers','','','','','','','','','','',2014);
insert into teams values('SD','Chargers','','','','','','','','','','',2015);
insert into teams values('SD','Chargers','','','','','','','','','','',2016);
insert into teams values('SD','Chargers','','','','','','','','','','',2017);
insert into teams values('STL','Rams','','','','','','','','','','',2013);
insert into teams values('STL','Rams','','','','','','','','','','',2014);
insert into teams values('STL','Rams','','','','','','','','','','',2015);
insert into teams values('DAL','Cowboys','','','','','','','','','','',2013);

COPY coaches(cname, cid) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\table_coach.csv' CSV HEADER DELIMITER ','; 

COPY team_coach( cid, team_code, ctype, year ) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\table_coach_team.csv' CSV HEADER DELIMITER ','; 

copy players( pname, pname_abbr ) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\players.csv' CSV HEADER DELIMITER ','; 

copy team_players( year,pname, pname_abbr, team_code, position ) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\team_players.csv' CSV HEADER DELIMITER ','; 

copy games_to_stats( season, year, week, home_team, team_code, away_team ) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\group_code\nfl_database\finished_csvs\game_to_stats.csv' CSV HEADER DELIMITER ','; 

copy players( pname, pname_abbr ) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_players_altered.csv' CSV HEADER DELIMITER ','; 

copy pass(pname, year, week, home_team, away_team, attempts, completions, percentage, yards, yards_per_attempt, touchdowns, touchdown_percentage, interceptions, interception_percentage, long, sack, loss, rate) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_passing.csv' CSV HEADER DELIMITER ',';

copy rushing(pname, year, week, home_team, away_team, attempts, yards, average, long, touchdown, fd) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_rushing.csv' CSV HEADER DELIMITER ',';

copy receiving(pname, year, week, home_team, away_team, receiving, yards, average, long, touchdown, fd, targets, yards_after_catch) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_receiving.csv' CSV HEADER DELIMITER ',';

copy defense(pname, year, week, home_team, away_team, interceptions, yards, average, long, touchdown, solo, assists, total, sack, yards_lost) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_defense.csv' CSV HEADER DELIMITER ',';

copy punting(pname, year, week, home_team, away_team, number, yards, average, long, touchback, in_20, out_of_bounds, fair_catch, down, blocked, net, return, yards_return, touchdown) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_punting.csv' CSV HEADER DELIMITER ',';


copy scoring(pname, year, week, home_team, away_team, total, rushing, punting, kick_return, pass_return, interception_return, field_goal_return, extra_point, field_goal, conversion, safety, points) FROM 'C:\Users\alex\Documents\_PSU\CS 586 intro db\final_project\db_final_project_personal\db_final_project_personal\table_scoring.csv' CSV HEADER DELIMITER ',';