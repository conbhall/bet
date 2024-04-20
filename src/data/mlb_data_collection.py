import requests
from bs4 import BeautifulSoup, Comment
import csv
import pandas as pd
import tempfile
import os

def format_player_url(formatted_player_key, year):

    return f'https://www.baseball-reference.com/players/gl.fcgi?id={formatted_player_key}&t=b&year={year}#batting_gamelogs'


def scrape_player_data(formatted_player_key, year):

    search_url = format_player_url(formatted_player_key, year)

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
        df_platoon = scrape_platoon_data(df, formatted_player_key, year)
        df_hmvis = scrape_hmvis_data(df_platoon, formatted_player_key, year)
        df_final = scrape_stad_data(df_hmvis, formatted_player_key, year)

        return df_final
    
    else:
        return Exception
    

def scrape_platoon_data(df, formatted_player_key, year):
    url = f'https://www.baseball-reference.com/players/split.fcgi?id={formatted_player_key}&t=b&year={year}#plato'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for comment in comments:
        if 'id="plato"' in comment:
            comment_soup = BeautifulSoup(comment, 'html.parser')

            table = comment_soup.find('table', id='plato')

            if table:
                body = table.find('tbody')

                data = []

                if body:
                    rows = body.find_all('tr')

                    for row in rows:
                        row_data = {}

                        for cell in row.find_all(['td', 'th']):
                            column_name = cell['data-stat']

                            cell_data = cell.get_text()

                            row_data[column_name] = cell_data
                        
                        if row_data:
                            data.append(row_data)
                    
                    platoon_df = pd.DataFrame(data)
                    combined_df = pd.concat([df, platoon_df], axis=1)
                    return combined_df
    return Exception


def scrape_hmvis_data(df, formatted_player_key, year):
    url = f'https://www.baseball-reference.com/players/split.fcgi?id={formatted_player_key}&t=b&year={year}#hmvis'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for comment in comments:
        if 'id="hmvis"' in comment:
            comment_soup = BeautifulSoup(comment, 'html.parser')

            table = comment_soup.find('table', id='hmvis')

            if table:
                body = table.find('tbody')

                data = []

                if body:
                    rows = body.find_all('tr')

                    for row in rows:
                        row_data = {}

                        for cell in row.find_all(['td', 'th']):
                            column_name = cell['data-stat']

                            cell_data = cell.get_text()

                            row_data[column_name] = cell_data

                        if row_data:
                            data.append(row_data)
                    
                    hmvis_df = pd.DataFrame(data)
                    combined_df = pd.concat([df, hmvis_df], axis=1)
                    return combined_df
    return Exception


def scrape_stad_data(df, formatted_player_key, year):
    url = f'https://www.baseball-reference.com/players/split.fcgi?id={formatted_player_key}&t=b&year={year}#stad#'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for comment in comments:
        if 'id="stad"' in comment:
            comment_soup = BeautifulSoup(comment, 'html.parser')

            table = comment_soup.find('table', id='stad')

            if table:
                body = table.find('tbody')

                data = []

                if body:
                    rows = body.find_all('tr')

                    for row in rows:
                        row_data = {}

                        for cell in row.find_all(['td', 'th']):
                            column_name = cell['data-stat']

                            cell_data = cell.get_text()

                            row_data[column_name] = cell_data

                        if row_data:
                            data.append(row_data)
                    
                    stad_df = pd.DataFrame(data)
                    combined_df = pd.concat([df, stad_df], axis=1)
                    return combined_df
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
    
