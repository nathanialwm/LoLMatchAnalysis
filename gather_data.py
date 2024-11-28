from key import KEY, my_id
import requests
import json
import pandas as pd
import sqlite3 

# Set up API request Base URL and Headers which includes API key
BASE_URL = "https://americas.api.riotgames.com/lol/"
HEADERS = {"X-Riot-Token": KEY}

# Get last 75 ranked matches
last_75_matches = requests.get(BASE_URL + "match/v5/matches/by-puuid/" + my_id + "/ids?type=ranked&start=0&count=75", headers=HEADERS).json() 
match_data_list = [] # List containing full match data for each match in last 75 for player

for match in last_75_matches:
    # Iterates over each match in last_75_matches and fetches the match data
    # appends the match data to match_data_list in json format
    # checks for valid response and handles errors
    try:
        response = requests.get(BASE_URL + "match/v5/matches/" + match, headers=HEADERS)
    
        if response.status_code == 200:
            match_data = response.json()
            match_data_list.append(match_data)
        else:
            print(f"Error fetching match data for match ID {match}: {response.status_code}")

    except Exception as e:
        print(f"Error fetching match data for match ID {match}: {e}")

# Create DataFrame and export to CSV
df = pd.json_normalize(match_data_list) 
df.to_csv("matches.csv", index=False)
df.to_sql("matches", con=sqlite3.connect("lol_match_data.db"), if_exists="replace", index=False)