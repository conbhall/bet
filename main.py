from src.data.mlb_data_collection import scrape_player_data, format_player_url, convert_raw_to_csv
from src.utilities.mlb_player_verification import mlb_player_verification, mlb_name_formatter

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

        # Using formatted URL, create DataFrame and temp CSV file for storing raw stats
        try: 
            player_raw_stats_df = scrape_player_data(formatted_player_key, year)
        except:
            print(f"No data found for {formatted_name} in {year}.")
            return
        
        player_raw_stats_csv = convert_raw_to_csv(player_raw_stats_df)

    else:
        print(f"No data found for {formatted_name} in {year}: {formatted_name} was or is not active.")

    return

if __name__ == "__main__":
    main()
