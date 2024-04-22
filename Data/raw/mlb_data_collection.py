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

    #totals_row = soup.find('tfoot').find('tr')

    if table_rows:

        #if totals_row:
        #    table_rows.append(totals_row)

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
    

def scrape_platoon_data(formatted_player_key, year):
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

                    return platoon_df
    return Exception


def scrape_hmvis_data(formatted_player_key, year):
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

                    return hmvis_df
    return Exception


def scrape_stad_data(formatted_player_key, year):
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

                    return stad_df
                
    return Exception
    
