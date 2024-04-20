# bet
Structure:

BET/
|
|-- venv/       # Virtual Environment
|
|-- Data/       # Directory to store raw and processed data
|   |-- raw/
|   |-- processed/
|
|-- Notebooks/   # Directory for storing potential Jupyter Notebooks for data management
|
|-- src/        # Directory for Source Code
|   |-- data/
|   |   |-- mlb_data_collection.py      # Scrapes baseball-reference.com and creates a temp csv file containing batting stats and other miscellaneous stats for players in any season they were active. WIP
|   |-- features/
|   |-- models/
|   |-- utilities/
|   |   |-- mlb_player_verification.py  # Verifies requested player is currently active, and returns formatted player name and formatted player URL key.                   
|
|-- TestCode/   # Holds test code. Not important or necessary.
|
|-- main.py     # Entry point for the program
|
|-- .gitignore  # To include the venv directory and other files that should not be committed # DO NOT EDIT!!!
|
|-- README.md   # Project documentation

Ideas:
**Raw Data Collection:
    - Need a way to ensure player entered has measurable data for that year.
    - Means need to create a list of all active MLB players and check if on list before formatting?
    - Probably an easier way to do this.
    - Also need a way to ensure each url is formatted in the correct way to yield stats for that player
    - For example: buschmi leads to Mike Busch (retired) and not Michael Bush
    - Mike Busch is bushmi01 and Michael Busch is buschmi02.
    - Also no need to even attempt to search for players that
        - a. aren't currently in MLB
        - b. don't show up in books
    - Proposed solution: Create another scraper to run on program startup to pull names of all either
        - a. Larger set: MLB players on current rosters at run time
        - b. Smaller set: MLB players that have existing lines for that day
        - (b) could require too much specification, but would allow for less data storage
        - (a) seems most ideal for now, however still need a way to ensure player requested returns that players data
        - i.e. differentiate between duplicate names.
        - Probably best end goal to be pull all names of players on major MLB books and store in a temp list/csv file
        - Check inputted name against list to ensure it is on it.
        - Attempt to pull data using main url formatting.
        - Determine how to verify data is for the correct player.
        - Perhaps prompt for team or some other easily identifiable characteristic if further specification is needed.

Data Scraped
**Used primarily for testing:
    - Date
    - Team
    - Opposing Team (as for now)
    - Score Result
    - Next Matchup
    - Next Matchup Starting Pitcher
    - Next Matchup Pitcher Stats
    - Next Matchup Game Times
    - Next Matchup Home or Away
    - Next Matchup Opposing Team Record
**Data Used For over/under hits props:
    -*Player Overall Stats Averages / Per Game
        - At Bats (AB)
        - Runs (R)
        - Hits (H)
        - Runs Batted In (RBI)
        - Walks / Base on Balls (BB)
        - Strikeouts (SO)
        - Batting Average (BA)
        - On Base Percentage (OBP)
        - Slugging Percentage (SLG)
        - On Base + Slugging Percentage (OPS)
        - Total Bases (TB)*
        - Average Leverage Index (aLI) [for now]*
        - Daily Fantasy Points DraftKings (DFS(DK))*
        - Daily Fantasy Points FanDuel (DFS(FD))*
        - Position (Pos)*
    - 
    -*Pitching Stats
    - * VS Right Handed Pitcher (RHP)
        - At Bats (AB_RHP)
        - Runs (R_RHP)
        - Hits (H_RHP)
        - Walks / Base on Balls (BB_RHP)
        - Strikeouts (SO_RHP)
        - Batting Average (BA_RHP)
        - On Base Percentage (OBP_RHP)
        - Slugging Percentage (SLG_RHP)
        - On Base + Slugging Percentage (OPS_RHP)
        - Total Bases (TB_RHP)
        - Batting Average on Balls in Play (BAbip_RHP)
    - * VS Left Handed Pitcher (LHP)
        - At Bats (AB_LHP)
        - Runs (R_LHP)
        - Hits (H_LHP)
        - Walks / Base on Balls (BB_LHP)
        - Strikeouts (SO_LHP)
        - Batting Average (BA_LHP)
        - On Base Percentage (OBP_LHP)
        - Slugging Percentage (SLG_LHP)
        - On Base + Slugging Percentage (OPS_LHP)
        - Total Bases (TB_LHP)
        - Batting Average on Balls in Play (BAbip_LHP)
    - * VS Right Handed Starting Pitcher (RHS)
        - At Bats (AB_RHS)
        - Runs (R_RHS)
        - Hits (H_RHS)
        - Walks / Base on Balls (BB_RHS)
        - Strikeouts (SO_RHS)
        - Batting Average (BA_RHS)
        - On Base Percentage (OBP_RHS)
        - Slugging Percentage (SLG_RHS)
        - On Base + Slugging Percentage (OPS_RHS)
        - Total Bases (TB_RHS)
        - Batting Average on Balls in Play (BAbip_RHS)
     * VS Left Handed Starting Pitcher (LHS)
        - At Bats (AB_LHS)
        - Runs (R_LHS)
        - Hits (H_LHS)
        - Walks / Base on Balls (BB_LHS)
        - Strikeouts (SO_LHS)
        - Batting Average (BA_LHS)
        - On Base Percentage (OBP_LHS)
        - Slugging Percentage (SLG_LHS)
        - On Base + Slugging Percentage (OPS_LHS)
        - Total Bases (TB_LHS)
        - Batting Average on Balls in Play (BAbip_LHS)
    - 
    -*Home or Away Stats
    - * Home Stats (HO)
        - At Bats (AB_HO)
        - Runs (R_HO)
        - Hits (H_HO)
        - Walks / Base on Balls (BB_HO)
        - Strikeouts (SO_HO)
        - Batting Average (BA_HO)
        - On Base Percentage (OBP_HO)
        - Slugging Percentage (SLG_HO)
        - On Base + Slugging Percentage (OPS_HO)
        - Total Bases (TB_HO)
        - Batting Average on Balls in Play (BAbip_HO)
    - * Away Stats (AW)
        - At Bats (AB_AW)
        - Runs (R_AW)
        - Hits (H_AW)
        - Walks / Base on Balls (BB_AW)
        - Strikeouts (SO_AW)
        - Batting Average (BA_AW)
        - On Base Percentage (OBP_AW)
        - Slugging Percentage (SLG_AW)
        - On Base + Slugging Percentage (OPS_AW)
        - Total Bases (TB_AW)
        - Batting Average on Balls in Play (BAbip_AW)
    - 
    -*Game Time Stats (STAD)
    - * Night Games (NI)
        - At Bats (AB_NI)
        - Runs (R_NI)
        - Hits (H_NI)
        - Walks / Base on Balls (BB_NI)
        - Strikeouts (SO_NI)
        - Batting Average (BA_NI)
        - On Base Percentage (OBP_NI)
        - Slugging Percentage (SLG_NI)
        - On Base + Slugging Percentage (OPS_NI)
        - Total Bases (TB_NI)
        - Batting Average on Balls in Play (BAbip_NI)
    - * Day Games (DAY)
        - At Bats (AB_DAY)
        - Runs (R_DAY)
        - Hits (H_DAY)
        - Walks / Base on Balls (BB_DAY)
        - Strikeouts (SO_DAY)
        - Batting Average (BA_DAY)
        - On Base Percentage (OBP_DAY)
        - Slugging Percentage (SLG_DAY)
        - On Base + Slugging Percentage (OPS_DAY)
        - Total Bases (TB_DAY)
        - Batting Average on Balls in Play (BAbip_DAY)