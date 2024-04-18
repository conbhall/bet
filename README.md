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
|   |   |-- data_collection.py      # Scrapes baseball-reference.com and creates a temp csv file containing batting stats for players in 2024 season. WIP
|   |-- features/
|   |-- models/
|   |-- utilities/
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
