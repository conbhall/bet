import requests
from bs4 import BeautifulSoup


def mlb_player_verification(first_name, last_name):
    initial = last_name[:1]

    full_name = f'{first_name[0].upper()}{first_name[1:]} {last_name[0].upper()}{last_name[1:]}'

    url = f'https://www.baseball-reference.com/players/{initial}/'
    headers = {'User_Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    initial_section = soup.find('div', class_="section_content", id="div_players_")

    if initial_section:
        active_players = initial_section.find_all('b')
        for players in active_players:
            player = players.find('a')
            if full_name == player.get_text():
                player_link = player['href']
                return player_link[11:20]
        
    return None


def mlb_name_formatter(first_name, last_name):
    return f'{last_name[:1].upper()}{last_name[1:]}, {first_name[:1].upper()}{first_name[1:]}'




