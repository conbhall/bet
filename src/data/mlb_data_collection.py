import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import tempfile
import os

def format_player_url(formatted_player_key, year):

    return f'https://www.baseball-reference.com/players/gl.fcgi?id={formatted_player_key}&t=b&year={year}#batting_gamelogs'


def scrape_player_data(search_url):

    response = requests.get(search_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    table_rows = soup.find_all('tr', id=lambda x: x and x.startswith('batting_gamelogs'))

    totals_row = soup.find('tfoot').find('tr')

    if table_rows:

        if totals_row:
            table_rows.append(totals_row)

        data = []

        for row in table_rows:

            row_data = {}
            for td in row.find_all('td'):

                stat_type = td['data-stat']

                stat_value = td.text

                row_data[stat_type] = stat_value

            if row_data:
                data.append(row_data)

        df = pd.DataFrame(data)

        return df
    
    else:
        return Exception



def convert_raw_to_csv(player_raw_data_df):

    if not player_raw_data_df.empty:

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            player_raw_data_df.to_csv(tmp_file.name, index=False)
            print(f"Temporary CSV file created at {tmp_file.name}")
            temp_csv_path = tmp_file.name

        return temp_csv_path
    else:
        print("No data was found.")
        return None
    
