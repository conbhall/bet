from src.data.prelim_umpire_data import load_umpire_data
from src.data.prelim_venue_data import load_venue_data
from src.data.complete_player_data import create_complete_player_df
from src.data.load_dates import load_dates, load_dates_between_months, load_dates_between

import pandas as pd
import time

#players = ['Shohei Ohtani', 'Alec Burleson', 'Jurickson Profar', 'Jose Altuve', 'William Contreras', 'Bryce Harper', 'Aaron Judge', 'Juan Soto', 'Gunnar Henderson', 'Vladimir Guerrero Jr.',]
players = ['Bryce Harper', 'Kyle Schwarber', 'Alec Bohm', 'Trea Turner']

#dates = ["2024-07-31", "2024-08-02", "2024-08-04"]
dates = load_dates_between('2024-03-28', '2024-08-05')

def main():
    ump_data = load_umpire_data()
    venue_data = load_venue_data()
    #print(ump_data)
    #print(venue_data)

    complete_date_dfs = []

    i = 0

    for date in dates:
        all_player_data = []
        for player in players:
            time.sleep(5)
            if i % 4 == 0:
                time.sleep(5)
                #Need to change how long between in order to not maximize requests.
                #Probably by using a VPN to change IP Address
            try:
                complete_player_df = create_complete_player_df(date, player, ump_data, venue_data)
                all_player_data.append(complete_player_df)
                i += 1
            except:
                print(f'No data found for {player} on {date}.')
                i += 1
        if len(all_player_data) > 0:
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
