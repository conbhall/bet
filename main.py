from src.data.data_collection import scrape_player_data, format_player_url, convert_raw_to_csv

def main():
    # Entry point for the entire program

    # Asking user for player name
    first_name = input("Enter Player's First Name: ").lower()
    last_name = input("Enter Player's Last Name: ").lower()

    # Modify player names to meet formatting for data-scraping URL
    url = format_player_url(first_name, last_name)

    # Using formatted URL, create DataFrame and temp CSV file for storing raw stats
    player_raw_stats_df = scrape_player_data(url)
    player_raw_stats_csv = convert_raw_to_csv(player_raw_stats_df)

    return

if __name__ == "__main__":
    main()
