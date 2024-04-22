import src.utilities.id_collection as util
import src.api.api_client as api
from Data.processed.mlb_data_processing import convert_df_to_csv
import statsapi
import pandas as pd


def main():
    team_or_player = input(f"Team or Player: ").lower()

    while team_or_player not in ['team', 'player']:
        team_or_player = input(f"Please input either 'team' or 'player': ").lower()
    
    if team_or_player == 'team':
        team_name = input(f"Input Team Name/Abbrev/City: ").lower()
        team_id = util.find_team_id(team_name)
    else:
        first_name = input(f"Input Player's First Name: ")
        last_name = input(f"Input Player's Last Name: ")
        player_name = f'{first_name.lower()} {last_name.lower()}'
        player_id = util.find_player_id(player_name)
        team_id = util.find_team_player_id(player_id)
        print(team_id)
    
    year = input(f"Input Requested Year: ")

    schedule_data = util.generate_schedule(year, team_id)

    schedule_df = pd.DataFrame(schedule_data)

    #convert_df_to_csv(schedule_df)



if __name__ == "__main__":
    main()
