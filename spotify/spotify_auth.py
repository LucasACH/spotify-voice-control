import requests
from spotify.spotify_credentials import SpotifyCredentials
import webbrowser
from base64 import b64encode as _b64encode
import csv

def b64encode(msg: str) -> str:
        """Encode a unicode string in base-64."""
        return _b64encode(msg.encode()).decode()

def save_access_and_refresh(access_token, refresh_token):
    """Save requested client tokens to file
    ---
    Args:
        access_token (str): requested client access_token
        refresh_token (str): requested client refresh_token
    """
    with open("spotify/tokens.csv", "w", newline = "\n") as tokens_database:
        writer = csv.DictWriter(tokens_database, fieldnames = ["token", "id"])
        writer.writerow({"token":"access_token", "id":access_token})
        writer.writerow({"token":"refresh_token", "id":refresh_token})

def update_access_token(access_token):
    """Update access token from file
    ---
    Args:
        access_token (str): requested client new access_token
    """

    refresh_token = ""
    with open("spotify/tokens.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames = ["token", "id"])
        for row in reader:
            rows = list(row.values())
            if rows[0] == "refresh_token":
                refresh_token = row
    
    with open("spotify/tokens.csv", "w", newline = "\n") as tokens_database:
        writer = csv.DictWriter(tokens_database, fieldnames = ["token", "id"])
        writer.writerow({"token":"access_token", "id":access_token})
        writer.writerow(refresh_token)
    

def authorization_code(redirect_uri, redirected):
    """Get code from authorization url
    ---
    Args:
        redirect_uri (str): client redirect uri
        redirected (str): redirected url after accepting authorization
    """
    authorization_code = redirected.replace(redirect_uri.lower() + "/?code=", "")
    return authorization_code
    


class AuthorizationCodeFlow:
    """Authorization for getting access token
    ---
    This flow is suitable for long-running applications in which the user
    grants permission only once. It provides an access token that can be
    refreshed. Since the token exchange involves sending your secret key,
    perform this on a secure location, like a backend service, and not from
    a client such as a browser or from a mobile app.
    """

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.client_secret = client_secret

        token = b64encode(self.client_id + ":" + self.client_secret)
        self.headers = {
            "Authorization": f"Basic {token}",
        }

        self.AUTH_URL = "https://accounts.spotify.com/authorize"
        self.TOKEN_URL = "https://accounts.spotify.com/api/token"

    
    def request_authorization_and_token(self):
        """
        Request authorization
        """
        scopes = "user-read-playback-state, user-modify-playback-state, user-read-currently-playing"

        params = (
            ("client_id", self.client_id),
            ("redirect_uri", self.redirect_uri),
            ("response_type", "code"),
            ("show_dialog",True),
            ("scope", scopes),
        )

        response = requests.get(self.AUTH_URL, params=params)
        dialog_url = response.url
        webbrowser.open(dialog_url)
        redirected = input("Please paste redirect URL: ").strip()
        self.request_token_with_authorization_code(authorization_code(self.redirect_uri, redirected))
    

    def request_token_with_authorization_code(self, authorization_code):
        """
        Request access token after authorization accept
        """
        data = {
            "grant_type": "authorization_code",
            "code": f"{authorization_code}",
            "redirect_uri": self.redirect_uri
        }

        response = requests.post(self.TOKEN_URL, headers=self.headers, data=data)
        response_json = response.json()

        access_token = response_json["access_token"]
        refresh_token = response_json["refresh_token"]

        save_access_and_refresh(access_token, refresh_token)

        message = ("""
        Tokens added to file:
            - access_token: %s
            - refresh_token: %s
        """) % (access_token, refresh_token)
        print(message)

        return response
    

    def request_token_with_refresh_token(self, refresh_token):
        """
        Use refresh token for generating new access token if expired
        """
        data = {
            "grant_type": "refresh_token",
            "refresh_token": f"{refresh_token}"
        }

        response = requests.post(self.TOKEN_URL, headers=self.headers, data=data)
        response_json = response.json()
        
        access_token = response_json["access_token"]

        update_access_token(access_token)

        message = ("""
        Refreshed access token added to file:
            - access_token: %s
        """) % (access_token)
        print(message)

        return response

