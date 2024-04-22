import src.api.api_client as api
import datetime

def find_player_id(player_name):
    try:
        player_id = api.fetch_players(player_name)
        return player_id[0]['id']
    except:
        print(f"Player stats for '{player_name}' not available.")
        return None
    
def find_team_player_id(player_id):
    team_id = api.fetch_team_player_id(player_id)
    return team_id
    

def find_team_id(team_name):
    try:
        team_id = api.fetch_teams(team_name)
        return team_id[0]['id']
    except:
        print(f"Team stats for '{team_name}' are not available.")
        return None
    
def generate_schedule(year, team_id):

    start_date = api.fetch_season_start_date(year)

    if int(year) == datetime.date.today().year:
        end_date = datetime.date.today() + datetime.timedelta(days=1)
    else:
        end_date = api.fetch_season_end_date(year)
    
    schedule_data = api.fetch_schedule(team_id, start_date, end_date)

    return schedule_data
