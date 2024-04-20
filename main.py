import pandas as pd

from src.data.mlb_data_collection import scrape_player_data, scrape_platoon_data, scrape_hmvis_data, scrape_stad_data
from src.utilities.mlb_player_verification import mlb_player_verification, mlb_name_formatter
from src.data.mlb_data_processing import mlb_raw_stats_cleaner, mlb_platoon_raw_stats_cleaner, mlb_hmvis_raw_stats_cleaner, mlb_stad_raw_stats_cleaner, construct_clean_df, convert_df_to_csv

def main():
    # Entry point for the entire program

    # Asking user for player name
    first_name = input("Enter Player's First Name: ").lower()
    last_name = input("Enter Player's Last Name: ").lower()
    year = int(input("Enter Year: "))

    formatted_name = mlb_name_formatter(first_name, last_name)

    formatted_player_key = mlb_player_verification(first_name, last_name, year)

    if formatted_player_key:

        print(f"Gathering Raw Data for {formatted_name}...")

        clean_df = construct_clean_df(formatted_name, formatted_player_key, year)

        clean_df_csv = convert_df_to_csv(clean_df)

    else:
        print(f"No data found for {formatted_name} in {year}: {formatted_name} was or is not active.")

    return

if __name__ == "__main__":
    main()
