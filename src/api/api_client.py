import statsapi

#Player ID
def fetch_players(player_name):

    return statsapi.lookup_player(player_name)

#Team_ID
def fetch_teams(team_name):

    return statsapi.lookup_team(team_name)

def fetch_last_game_pk(team_id):

    return statsapi.last_game(team_id)

def fetch_next_game_pk(team_id):

    return statsapi.next_game(team_id)

def fetch_schedule(team_id, start_date, end_date):

    return statsapi.schedule(team=team_id, start_date=start_date, end_date=end_date)

def fetch_season_start_date(year):

    return statsapi.get('season',{'seasonId':year,'sportId':1})['seasons'][0]['regularSeasonStartDate']

def fetch_season_end_date(year):

    return statsapi.get('season',{'seasonId':year,'sportId':1})['seasons'][0]['regularSeasonEndDate']

def fetch_team_player_id(player_id):
    player_info = statsapi.get('people',{'personIds':player_id,'sportId':1})
    return player_info


