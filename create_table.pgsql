create table game_stats(
    Date date, 
    Season int, 
    Week int, 
    team_code varchar(4),
    Opponent varchar(4),
    HomeOrAway varchar(4), 
    Score int, 
    OpponentScore int, 
    Stadium varchar(64),
    PlayingSurface varchar(32), 
    TimeOfPossession varchar(8), 
    FirstDowns int, 
    OffensivePlays int, 
    OffensiveYards int, 
    Touchdowns int, 
    RushingAttempts int, 
    RushingYards int, 
    RushingTouchdowns int, 
    PassingAttempts int, 
    PassingCompletions int, 
    PassingYards int, 
    PassingTouchdowns int, 
    PassingInterceptions int, 
    CompletionPercentage real, 
    Fumbles int, 
    FumblesLost int, 
    TimesSacked int, 
    TimesSackedYards int, 
    Punts int, 
    PuntYards int, 
    Giveaways int, 
    Takeaways int, 
    TurnoverDifferential int, 
    OpponentTimeOfPossession varchar(8), 
    OpponentFirstDowns int,  
    OpponentOffensivePlays int, 
    OpponentOffensiveYards int, 
    OpponentRushingAttempts int,  
    OpponentRushingYards int, 
    OpponentCompletionPercentage real, 
    OpponentPenalties int, 
    OpponentPenaltyYards int, 
    OpponentFumbles int, 
    OpponentFumblesLost int, 
    OpponentTimesSacked int, 
    FieldGoalAttempts int, 
    FieldGoalsMade int, 
    PuntReturns int, 
    PuntReturnYards int, 
    KickReturns int, 
    KickReturnYards int, 
    OpponentPuntReturns int, 
    OpponentPuntReturnYards int, 
    OpponentKickReturns int, 
    OpponentKickReturnYards int, 
    Sacks int, 
    SackYards int, 
    TeamName varchar(32), 
    DayOfWeek varchar(8), 
    Day date, 
    DateTime timestamp,
    primary key(season, week, team_code)
);

create table games (
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    Network varchar(16), 
    Weather varchar(64), 
    Description varchar(512), 
    Wind varchar(8), 
    Away_Score int, 
    Home_Score int, 
    Temp varchar(4),
    primary key(year, week, home_team, away_team)
)

create table games_to_stats (
    season int,
    week int, 
    home_team varchar(4), 
    away_team varchar(4),
    year int,
    team_code varchar(4),
    foreign key (year, week, home_team, away_team) references games,
    foreign key (season, week, team_code) references game_stats
) ;

create table teams (
    team_code varchar(4), 
    Name varchar(16), 
    Conference varchar(8), 
    Division varchar(8), 
    FullName varchar(32), 
    HeadCoach varchar(64), 
    OffensiveCoordinator varchar(64), 
    DefensiveCoordinator varchar(64), 
    SpecialTeamsCoach varchar(64), 
    OffensiveScheme varchar(32), 
    DefensiveScheme varchar(32), 
    StadiumName varchar(64), 
    Year int,
    primary key (team_code, year)
)

create table coaches (
    cname varchar(64),
    cid int,
    primary key(cid)
) ;

create table team_coach (
    cid int, 
    team_code varchar(4), 
    ctype varchar(32),
    year int,
    foreign key (cid) references coaches,
    foreign key (team_code, year) references teams
) ;

create table players (
    pname varchar(64),
    pname_abbr varchar(32),
    primary key(pname)
) ;

create table team_players (
    year int,
    pname varchar(64),
    pname_abbr varchar(32),
    team_code varchar(4),
    position varchar(32),
    foreign key(team_code, year) references teams,
    foreign key(pname) references players
) ;

create view stats_weather as
select	gs.*, case when g.weather is null then 'Dome' else g.weather end as weather, g.description, g.wind, g.temp
from	game_stats gs
		join games g on(g.year,g.week,g.home_team) = (gs.season, gs.week, gs.team_code) or (g.year,g.week,g.away_team) = (gs.season, gs.week, gs.team_code)

create table pass (
    pname varchar(64),
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    attempts int,
    completions int, 
    percentage real, 
    yards int, 
    yards_per_attempt real, 
    touchdowns int, 
    touchdown_percentage real, 
    interceptions int, 
    interception_percentage real, 
    long varchar(10), 
    sack int, 
    loss int, 
    rate real,
    foreign key(year, week, home_team, away_team) references games,
    foreign key(pname) references players
)

create table rushing (
    pname varchar(64),
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    attempts int, 
    yards int,
    average real,
    long varchar(10), 
    touchdown int,
    fd int,
    foreign key(year, week, home_team, away_team) references games,
    foreign key(pname) references players
);

create table receiving (
    pname varchar(64),
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    receiving int,
    attempts int, 
    yards int,
    average real,
    long varchar(10), 
    touchdown int,
    fd int,
    targets int,
    yards_after_catch int,
    foreign key(year, week, home_team, away_team) references games,
    foreign key(pname) references players
);

create table defense (
    pname varchar(64),
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    interceptions int,
    yards int,
    average real,
    long varchar(10), 
    touchdown int,
    solo int,
    assists int,
    total int,
    sack real,
    yards_lost real,
    foreign key(year, week, home_team, away_team) references games,
    foreign key(pname) references players
);

create table scoring (
    pname varchar(64),
    Year int, 
    Week int, 
    Home_Team varchar(4), 
    Away_Team varchar(4), 
    total int,
    rushing int,
    punting int,
    kick_return int,
    pass_return int,
    interception_return int,
    field_goal_return int,
    extra_point varchar(5),
    field_goal varchar (5),
    conversion int,
    safety int,
    points int,
    foreign key(year, week, home_team, away_team) references games,
    foreign key(pname) references players
);