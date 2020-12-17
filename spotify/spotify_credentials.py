import os
import csv
from datetime import datetime

now = datetime.now()


class SpotifyCredentials(object):
    """App credentials for requesting access token
    ---
    Set Up Your Account: <https://developer.spotify.com/documentation/web-api/quick-start/>
    """

    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")

    class Tokens(object):
        
        @property
        def access_token(self):
            """Client access token
            ---
            """
            try:
                with open("spotify/tokens.csv") as tokens_database:
                    tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
                    return tokens_database_reader["access_token"]
            except KeyError:
                return None

        @property
        def expires_in(self):
            """When the access token is going to expire
            ---
            """
            try:
                with open("spotify/tokens.csv") as tokens_database:
                    tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
                    requested_on = tokens_database_reader["requested_on"]
                    requested_on = datetime.strptime(requested_on, "%Y-%m-%d %H:%M:%S.%f")
                    difference = now - requested_on 
                    return 3600 - difference.total_seconds()

            except KeyError:
                return None
        
        @property
        def refresh_token(self):
            """Client refresh token
            ---
            """
            try:
                with open("spotify/tokens.csv") as tokens_database:
                    tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
                    return tokens_database_reader["refresh_token"]
            except KeyError:
                return None
