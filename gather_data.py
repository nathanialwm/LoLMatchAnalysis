from key import KEY, my_id
import requests
import json
import pandas as pd
import sqlite3 

# Set up API request Base URL and Headers which includes API key
BASE_URL = "https://americas.api.riotgames.com/lol/"
HEADERS = {"X-Riot-Token": KEY}

def get_matches(type, count) -> list:
    # Gets the last 75 matches for the player
    # Takes match type(string) and count(int) as arguments
    return requests.get(f"{BASE_URL}match/v5/matches/by-puuid/{my_id}/ids?type={type}&start=0&count={count}", headers=HEADERS).json()

last_75 = get_matches("ranked", 75)
match_data_list = [] # List containing full match data for each match in determined match type and count for player

for match in last_75:
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


print(match_data_list)