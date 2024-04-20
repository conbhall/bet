import pandas as pd
import tempfile

from src.data.mlb_data_collection import scrape_player_data, scrape_platoon_data, scrape_hmvis_data, scrape_stad_data

def mlb_raw_stats_cleaner(df):
    df.rename(columns={
        'team_game_num': 'game_num',
        'team_homeORaway': 'Home',
        #'opp_ID': 'OPP',
        'batting_avg': 'BA',
        'onbase_perc': 'OBP',
        'slugging_perc': 'SLG',
        'onbase_plus_slugging': 'OPS',
    }, inplace=True)

    all_columns = df.columns.tolist()

    columns_to_keep = ['game_num', 'Home', 'AB', 'R', 'H', 'RBI', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS']

    columns_to_drop = [column for column in all_columns if column not in columns_to_keep]

    correct_columns_df = df.drop(columns_to_drop, axis=1)

    correct_columns_df['Home'] = correct_columns_df['Home'].apply(lambda x: True if x == '' else False)

    correct_columns_df['game_num'] = list(range(1, len(df) + 1))
    
    correct_columns = correct_columns_df.columns.tolist()

    for column in correct_columns:
        if correct_columns_df[column].dtypes == object:
            correct_columns_df[column] = pd.to_numeric(correct_columns_df[column], errors='coerce')

    return correct_columns_df


def mlb_platoon_raw_stats_cleaner(df):
    df.rename(columns={
        'split_name': 'pitcher_type',
        'batting_avg': 'BA',
        'onbase_perc': 'OBP',
        'slugging_perc': 'SLG',
        'onbase_plus_slugging': 'OPS',
        'batting_avg_bip': 'BAbip'
    }, inplace=True)

    all_columns = df.columns.tolist()

    columns_to_keep = ['pitcher_type', 'AB', 'R', 'H', 'RBI', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'TB', 'BAbip']

    columns_to_drop = [column for column in all_columns if column not in columns_to_keep]

    correct_columns_df = df.drop(columns_to_drop, axis=1)

    clean_df = correct_columns_df.drop(correct_columns_df.index.difference([0, 1]))

    clean_df['pitcher_type'] = [0, 1]
    # 0 = RHP, 1 = LHP

    clean_columns = clean_df.columns.tolist()

    for column in clean_columns:
        if clean_df[column].dtypes == object:
            clean_df[column] = pd.to_numeric(clean_df[column], errors='coerce')

    return clean_df


def mlb_hmvis_raw_stats_cleaner(df):
    df.rename(columns={
        'split_name': 'home',
        'batting_average': 'BA',
        'onbase_perc': 'OBP',
        'slugging_perc': 'SLG',
        'onbase_plus_slugging': 'OPS',
        'batting_avg_bip': 'BAbip'
    }, inplace=True)

    all_columns = df.columns.tolist()

    columns_to_keep = ['home', 'AB', 'R', 'H', 'RBI', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'TB', 'BAbip']

    columns_to_drop = [column for column in all_columns if column not in columns_to_keep]

    correct_columns_df = df.drop(columns_to_drop, axis=1)

    correct_columns_df['home'] = [True, False]

    correct_columns = correct_columns_df.columns.tolist()

    for column in correct_columns:
        if correct_columns_df[column].dtypes == object:
            correct_columns_df[column] = pd.to_numeric(correct_columns_df[column], errors='coerce')

    return correct_columns_df


def mlb_stad_raw_stats_cleaner(df):
    df.rename(columns={
        'split_name': 'game_time',
        'batting_average': 'BA',
        'onbase_perc': 'OBP',
        'slugging_perc': 'SLG',
        'onbase_plus_slugging': 'OPS',
        'batting_avg_bip': 'BAbip'
    }, inplace=True)

    all_columns = df.columns.tolist()

    columns_to_keep = ['game_time', 'AB', 'R', 'H', 'RBI', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'TB', 'BAbip']

    columns_to_drop = [column for column in all_columns if column not in columns_to_keep]

    correct_columns_df = df.drop(columns_to_drop, axis=1)

    clean_df = correct_columns_df.drop(correct_columns_df.index.difference([0, 1]))
    
    clean_df['game_time'] = [0, 1]
    # 0 = Night Games, 1 = Day Games.
    
    correct_columns = clean_df.columns.tolist()

    for column in correct_columns:
        if clean_df[column].dtypes == object:
            clean_df[column] = pd.to_numeric(clean_df[column], errors='coerce')

    return clean_df


def construct_clean_df(formatted_name, formatted_player_key, year):
        
        try: 
            player_raw_stats_df = scrape_player_data(formatted_player_key, year)
            player_clean_stats_df = mlb_raw_stats_cleaner(player_raw_stats_df)
        except:
            print(f"No data found for {formatted_name} in {year}.")
        
        try:
            platoon_raw_stats_df = scrape_platoon_data(formatted_player_key, year)
            platoon_clean_stats_df = mlb_platoon_raw_stats_cleaner(platoon_raw_stats_df)
        except:
            print(f"No platoon-data found for {formatted_name} in {year}.")
        
        try:
            hmvis_raw_stats_df = scrape_hmvis_data(formatted_player_key, year)
            hmvis_clean_stats_df = mlb_hmvis_raw_stats_cleaner(hmvis_raw_stats_df)
        except:
            print(f"No hmvis-data found for {formatted_name} in {year}.")
        
        try:
            stad_raw_stats_df = scrape_stad_data(formatted_player_key, year)
            stad_clean_stats_df = mlb_stad_raw_stats_cleaner(stad_raw_stats_df)
            
        except:
            print(f"No stad-data found for {formatted_name} in {year}.")   

        clean_df = pd.concat([player_clean_stats_df, platoon_clean_stats_df, hmvis_clean_stats_df, stad_clean_stats_df], axis=1)

        return clean_df


def convert_df_to_csv(df):

    if not df.empty:

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            df.to_csv(tmp_file.name, index=False)
            print(f"Temporary CSV file created at {tmp_file.name}")
            temp_csv_path = tmp_file.name

        return temp_csv_path
    else:
        print("No data was found.")
        return None