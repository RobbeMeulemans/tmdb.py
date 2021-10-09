# Modules
import requests
from requests.structures import CaseInsensitiveDict
import json
from prettytable import PrettyTable
import time

# PrettyTable setup
prettytable = PrettyTable()
prettytable.field_names = ["Movie Name", "Release Date"]

# Funtions
def json_data(token, movie):
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + token
    movie_search = "https://api.themoviedb.org/3/search/movie?query="
    # Replaces spaces in titles with "-"
    if movie.find(" "):
        movie.replace(" ", "-")
    movie_search += movie
    json_data = requests.get(movie_search, headers=headers).json()
    return json_data

# Variables
bearer_token = input("Bearer Token: ")
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + bearer_token
movie = input("Movie: ")

# Main
while movie != "exit":

    # Call function
    current_variables = json_data(bearer_token, movie)

    # Error when invalid Bearer Token + check until token is right
    while "status_code" in current_variables:
        print("Invalid Bearer Token")
        time.sleep(0.5)
        bearer_token = input("Re-enter Bearer Token: ")
        current_variables = json_data(bearer_token,movie)

    # Error when invalid movie name
    if len(current_variables["results"]) == 0:
        print("Movie not found")
    else:
        # Extracting movie name and release date
        for movie in current_variables["results"]:
            name = movie["original_title"]
            release = movie["release_date"]
            # Add values to table
            prettytable.add_row([name, release])
        print(prettytable)
    movie = input("Movie: ")

