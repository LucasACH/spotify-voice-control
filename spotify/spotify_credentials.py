import os
import csv

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
