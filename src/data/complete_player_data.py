import pandas as pd
import papermill as pm
import nbformat

def create_complete_player_df(date, player, umpire_data, venue_data):

    player_first_name_param, player_last_name_param = player.split(' ', 1)
    date_param = date
    umpire_data_param = umpire_data
    venue_data_param = venue_data

    pm.execute_notebook(
        r'G:\Repos\bet\src\data\stats.ipynb',
        r'G:\Repos\bet\output_notebook.ipynb',
        parameters=dict(player_first_name_param=player_first_name_param, 
                        player_last_name_param=player_last_name_param, 
                        date_param=date_param, 
                        umpire_data_param=umpire_data_param, 
                        venue_data_param=venue_data_param
                        )
    )

    complete_df = pd.read_csv(r'G:\Repos\bet\output_data.csv')

    return complete_df
