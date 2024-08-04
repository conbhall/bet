from src.data.prelim_umpire_data import load_umpire_data
from src.data.prelim_venue_data import load_venue_data

import pandas as pd

players = []

dates = []

def main():
    ump_data = load_umpire_data()
    venue_data = load_venue_data()
    print(ump_data)
    print(venue_data)

    complete_date_dfs = []

    for date in dates:
        all_player_data = []
        for player in players:
            complete_player_df = create_complete_player_df(date, player)
            all_player_data.append(complete_player_df)
        combined_player_df = pd.concat(all_player_data, ignore_index=True)
        complete_date_dfs.append(combined_player_df)

    empty_df = pd.DataFrame(columns=combined_player_df.columns)

    complete_data = []

    for df in complete_date_dfs:
        complete_data.append(df)
        complete_data.append(empty_df)
    
    complete_df = pd.concat(complete_df, ignore_index=True)

    print(complete_df)

    return

if __name__ == "__main__":
    main()
