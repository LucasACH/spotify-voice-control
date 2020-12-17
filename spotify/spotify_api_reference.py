import requests
from spotify.error_handling import *


class SpotifyPlayer:
    """Web API Reference
    ---
    Web API endpoints enable external applications to access
    the Spotify catalog and user data. The endpoints are
    arranged in a structure defined by an object model.
    <https://developer.spotify.com/documentation/web-api/reference/>
    ---
    """

    def __init__(self, access_token):
        self.access_token = access_token

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": ("Bearer {access_token}").format(
                access_token=access_token
            ),
        }
    
    def available_devices(self):
        """Get information about a user’s available devices.
        ---
        Returns:
            requests.models.Response: A successful request will return a 200 OK
            response code with a json payload that contains the device objects.
            When no available devices are found, the request will return a 200
            OK response with an empty devices list.
        API reference: <https://developer.spotify.com/console/get-users-available-devices/>
        ---
        """

        response = requests.get("https://api.spotify.com/v1/me/player/devices", headers=self.headers)

        if check_for_errors(response.status_code):
            return response
    

    def current_playback(self, market: str=None, additional_types: str=None):
        """Get information about the user’s current playbackstate,includingtrack or episode, progress, and active device.
        ---
        Args:
            market (str, optional): An ISO 3166-1 alpha-2 country code or the
            string from_token. Provide this parameter if you want to apply
            Track Relinking. Defaults to None.
            
            additional_types (str, optional): A comma-separated list of item
            types that your client supports besides the default track type.
            Valid types are: track and episode. Defaults to None.
       
        Returns:
            requests.models.Response: A successful request will return a 200
            OK response code with a json payload that contains information
            about the current playback. The information returned is for the
            last known state, which means an inactive device could be returned
            if it was the last one to execute playback. When no available
            devices are found, the request will return a 200 OK response but
            with no data populated.
        API reference: <https://developer.spotify.com/console/get-user-player/>
        ---
        """

        params = (
            ("market", market),
            ("additional_types", additional_types),
        )

        response = requests.get("https://api.spotify.com/v1/me/player", headers=self.headers, params=params)

        if check_for_errors(response.status_code):
            return response
        

    
    def pause_playback(self, device_id: str=None):
        """Pause playback on the user’s account.
        ---
        Args:
            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-pause/>
        ---
        """

        params = (("device_id", device_id),)
        
        response = requests.put("https://api.spotify.com/v1/me/player/pause", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response


    def resume_playback(self, device_id: str=None):
        """Resume a User's Playback
        ---

        Args:
            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-play/>
        ---
        """

        params = (("device_id", device_id),)
        
        response = requests.put("https://api.spotify.com/v1/me/player/play", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response
    

    def start_playback(self, context_uri: str, device_id: str=None, position: int=0, position_ms: int=0):
        """[summary]
        ---
        Args:
            context_uri (str): [description]

            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

            position (int, optional): Indicates from where in the context
            playback should start. Only available when context_uri corresponds
            to an album or playlist object, or when the uris parameter is used.
            Defaults to 0.

            position_ms (int, optional): The position in milliseconds to seek to.
            Must be a positive number. Passing in a position that is greater
            than the length of the track will cause the player to start
            playing the next song. Defaults to 0.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-play/>
        ---
        """

        params = (
            ("device_id", device_id),
        )

        data = ("{\"context_uri\":\"%s\", \"offset\":{\"position\":%d}, \"position_ms\":%d}") % (context_uri, position, position_ms)
    
        response = requests.put('https://api.spotify.com/v1/me/player/play', headers=self.headers, params=params, data=data)

        if check_for_errors(response.status_code):
            return response


    def next_track(self, device_id: str=None):
        """Skip User's Playback To Next Track
        ---

        Args:
            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/post-next/>
        ---
        """

        params = (
            ("device_id", device_id),
        )

        response = requests.post("https://api.spotify.com/v1/me/player/next", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response


    def previous_track(self, device_id: str=None):
        """Skip User's Playback To Previous Track
        ---

        Args:
            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/post-previous/>
        ---
        """

        params = (
            ("device_id", device_id),
        )

        response = requests.post("https://api.spotify.com/v1/me/player/previous", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response
    

    def transfer_playback(self, device_id: str):
        """Transfer playback to a new device and determine if it should start playing.
        ---
        Args:
            device_id (str): string containing the ID of the device on which
            playback should be started/transferred.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-user-player/>
        ---
        """

        data = ("{\"device_ids\":[\"%s\"], \"play\": true}") % (device_id)

        response = requests.put('https://api.spotify.com/v1/me/player', headers=self.headers, data=data)

        if response.status_code == 502:
            pass
        else:
            check_for_errors(response.status_code)
            return response


    def seek_to_position(self, position_ms: int, device_id: str=None):
        """Seeks to the given position in the user’s currently playing track.
        ---
        Args:
            position_ms (int): The position in milliseconds to seek to.
            Must be a positive number. Passing in a position that is greater
            than the length of the track will cause the player to start
            playing the next song.

            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-seek/>
        ---
        """

        params = (
            ("position_ms", {position_ms}),
            ("device_id", {device_id}),
        )
        
        response = requests.put("https://api.spotify.com/v1/me/player/seek", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response
    

    def set_repeat_mode(self, state: str="track", device_id: str=None):
        """Set the repeat mode for the user’s playback.
        ---
        Args:
            state (str, optional): track, context or off.
              - "track" will repeat the current track.
              - "context" will repeat the current context.
              - "off" will turn repeat off.
            Defaults to "context".

            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-repeat/>
        ---
        """

        params = (
            ("state", state),
            ("device_id", device_id),
        )
        
        response = requests.put("https://api.spotify.com/v1/me/player/repeat", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response
    

    def toggle_shuffle(self, state: bool=True, device_id: str=None):
        """Toggle shuffle on or off for user’s playback.
        ---
        Args:
            state (bool, optional): True or False.
              True: Shuffle user’s playback.
              False: Do not shuffle user’s playback.
            Defaults to True.

            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-shuffle/>
        ---
        """

        params = (
            ("state", state),
            ("device_id", device_id),
        )

        response = requests.put("https://api.spotify.com/v1/me/player/shuffle", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response


    def set_volume(self, volume_percent: int=100, device_id: str=None):
        """Set the volume for the user’s current playback device.
        ---
        Args:
            volume_percent (int, optional): The volume to set. Must be a value
            from 0 to 100 inclusive. Defaults to 100.

            device_id (str, optional): The id of the device this command is
            targeting. If not supplied, the user’s currently active device
            is the target. Defaults to None.

        Returns:
            requests.models.Response: A completed request will return a 204 NO
            CONTENT response code, and then issue the command to the player.
            Due to the asynchronous nature of the issuance of the command, you
            should use the Get Information About The User’s Current Playback
            endpoint to check that your issued command was handled correctly
            by the player.

            If the device is not found, the request will return 404 NOT FOUND
            response code. 
            
            If the user making the request is non-premium, a 403 FORBIDDEN
            response code will be returned.
        API reference: <https://developer.spotify.com/console/put-volume/>
        ---
        """
        params = (
            ("volume_percent", volume_percent),
            ("device_id", device_id),
        )
        
        response = requests.put("https://api.spotify.com/v1/me/player/volume", headers=self.headers, params=params)
        
        if check_for_errors(response.status_code):
            return response


    def search(self, query: str, query_type: str="track,artist", market: str=None, limit: int=20, offset: int=0, include_external: str=None):
        """Get Spotify Catalog information about albums, artists, playlists, tracks, shows or episodes that match a keyword string.
        ---
        Args:
            query (str): Search query keywords and optional field filters and
            operators.

            query_type (str, optional): A comma-separated list of item types
            to search across.
            Valid types are: album , artist, playlist, track, show and
            episode.
            Search results include hits from all the specified item types.
            Defaults to "track,artist".

            market (str, optional): An ISO 3166-1 alpha-2 country code or the
            string from_token.If a country code is specified, only content
            that is playable inthat market is returned. Defaults to None.

            limit (int, optional): Maximum number of results to return.
              - Maximum: 50
            Note: The limit is applied within each type, not on the total
            response. Defaults to 20.

            offset (int, optional): The index of the first result to return.
              - Default: 0 (the first result).
              - Maximum offset (including limit): 2,000.
            Use with limit to get the next page of search results.
            Defaults to 0.

            include_external (str, optional): Possible values: audio
            If include_external=audio is specified the response will include
            any relevant audio content that is hosted externally.
            By default external content is filtered out from responses.
            Defaults to None.

        Returns:
            requests.models.Response: 
                On success:
                    In the response header the HTTP status code is 200 OK.
                    For each type provided in the type parameter, the response
                    body contains an array of artist objects / simplified album
                    objects / track objects / simplified show objects / simplified
                    episode objects wrapped in a paging object in JSON.
                    
                On error:
                    The header status code is an error code.
                    The response body contains an error object.
        API reference: <https://developer.spotify.com/console/get-search-item/>
        ---
        """
        params = (
            ("q", query),
            ("type", query_type),
            ("market", market),
            ("limit", limit),
            ("offset", offset),
            ("include_external", include_external),
        )

        response = requests.get("https://api.spotify.com/v1/search", headers=self.headers, params=params)

        if check_for_errors(response.status_code):
            return response




# print(spotify.available_devices().json())
# print(spotify.current_playback().content)
# spotify.pause_playback()
# spotify.resume_playback()
# spotify.start_playback("spotify:album:5v7PsESglCFeVcb7wNEWIW", "423bdf7dc0a1479a84e953fe61c486fa865a4247")
# spotify.next_track("423bdf7dc0a1479a84e953fe61c486fa865a4247")
# spotify.previous_track("423bdf7dc0a1479a84e953fe61c486fa865a4247")
# spotify.seek_to_position(position_ms=50000)
# spotify.set_repeat_mode()
# spotify.toggle_shuffle()
# spotify.set_volume(100)

# search = spotify.search("parcels", limit=1, query_type="track").json()
# print(search["tracks"]["items"][0]["album"]["uri"])


# for item in search["tracks"]["items"]:
#     print(item["album"]["uri"])

