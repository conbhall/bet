from src.data.prelim_umpire_data import load_umpire_data
from src.data.prelim_venue_data import load_venue_data
from src.data.complete_player_data import create_complete_player_df

import pandas as pd

players = ['Shohei Ohtani', 'Alec Burleson', 'Jurickson Profar', 'Jose Altuve', 'William Contreras', 'Bryce Harper', 'Aaron Judge', 'Juan Soto', 'Gunnar Henderson', 'Vladimir Guerrero Jr.',]

dates = ["2024-07-31", "2024-08-02", "2024-08-04"]

def main():
    ump_data = load_umpire_data()
    venue_data = load_venue_data()
    #print(ump_data)
    #print(venue_data)

    complete_date_dfs = []

    for date in dates:
        all_player_data = []
        for player in players:
            complete_player_df = create_complete_player_df(date, player, ump_data, venue_data)
            all_player_data.append(complete_player_df)
        combined_player_df = pd.concat(all_player_data, ignore_index=True)
        complete_date_dfs.append(combined_player_df)

    complete_data = []

    for df in complete_date_dfs:
        complete_data.append(df)
        complete_data.append(pd.DataFrame([[pd.NA] * len(df.columns)], columns=df.columns))
    
    complete_df = pd.concat(complete_data, ignore_index=True)

    complete_df.to_csv(r'G:\Repos\bet\complete_data.csv', index=False)

    return

if __name__ == "__main__":
    main()
