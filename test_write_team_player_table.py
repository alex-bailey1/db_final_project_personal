from get_roster import write_team_player_table
from get_roster import get_only_one_pos

#not all the websites abreviations are correct, this changes the real abbreviation to the websites version {actual_abrev: website_abrv}
team_abrev_translation = {'ari': 'arz', 'atl': 'atl', 'bal': 'bal', 'buf': 'buf', 'car': 'car', 'chi': 'chi', 'cin': 'cin', 'cle': 'cle', 'dal': 'dal', 'den': 'den', 'det': 'det', 'gb': 'gb', 'hou': 'hou', 'ind': 'ind', 'jax': 'jac', 'kc': 'kc', 'mia': 'mia', 'min': 'min', 'ne': 'ne', 'no': 'no', 'nyg': 'nyg', 'nyj': 'nyj', 'oak': 'oak', 'phi': 'phi', 'pit': 'pit', 'sf': 'sf', 'sea': 'sea', 'tb': 'tb', 'ten': 'ten', 'was': 'was'}
start_year = 2018
num_years = 1

return_val = write_team_player_table(team_abrev_translation, start_year, num_years)