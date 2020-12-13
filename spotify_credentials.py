import os
import csv

class SpotifyCredentials(object):

    # Variables used for making Spotify API requests
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")

    class Tokens(object):

        # Save token to csv file
        def add_tokens(self, access_token, refresh_token):
            with open("tokens\\tokens.csv", "w", newline = "\n") as tokens_database:
                writer = csv.DictWriter(tokens_database, fieldnames = ["token", "id"])
                writer.writerow({"token":"access_token", "id":access_token})
                writer.writerow({"token":"refresh_token", "id":refresh_token})
            print("Tokens added to file")

        # Get Access Token from csv file
        def get_access_token(self):
            with open("tokens.csv") as tokens_database:
                tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
                return tokens_database_reader["access_token"]
        
        # Get Refresh Token from csv file
        def get_refresh_token(self):
            with open("tokens.csv") as tokens_database:
                tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
                return tokens_database_reader["refresh_token"]


