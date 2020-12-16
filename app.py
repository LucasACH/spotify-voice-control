from spotify.spotify_credentials import SpotifyCredentials
from spotify.spotify_auth import AuthorizationCodeFlow
from spotify.spotify_api_reference import SpotifyPlayer
from spotify.error_handling import *
import speech_recognition as sr
from assistant_engine import VirtualAssistant


credentials = SpotifyCredentials()
access_token = credentials.Tokens().access_token
refresh_token = credentials.Tokens().refresh_token

auth = AuthorizationCodeFlow(credentials.client_id,
                            credentials.client_secret,
                            credentials.redirect_uri)

spotify = SpotifyPlayer(access_token)
listener = sr.Recognizer()
spotify_speech = VirtualAssistant()



# Check if access token still valid
# Get active device (step 1 can be done by checking active device)



def listen():
    if access_token == None:
        auth.request_authorization_and_token()
    else:
        try:
            available_devices = spotify.available_devices().json()
            current_playback = spotify.current_playback().json()
            device_id = current_playback["device"]["id"]
            available_devices_dict = {}

            for device in available_devices["devices"]:
                if device["type"] == "Computer":
                    available_devices_dict.update({"computer":device["id"]})
                elif device["type"] == "Smartphone":
                    available_devices_dict.update({"smartphone":device["id"]})

            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    user_voice = listener.listen(source, timeout=2, phrase_time_limit=4)
                    command = listener.recognize_google(user_voice, language="en-US")
                    command = command.lower()

                    if "spotify" in command:
                        command = command.replace("spotify ", "")
                        print(command)

                        if "devices" in command:
                            total_devices = len(available_devices_dict.keys())
                            if total_devices > 1:
                                return spotify_speech.talk("You have %d available devices." % (total_devices))
                            else:
                                return spotify_speech.talk("You have one available device.")
                        
                        if "song name" in command:
                            song_name = current_playback ["item"]["name"]
                            artist_name = current_playback ["item"]["album"]["artists"][0]["name"]
                            return spotify_speech.talk(("You are listening to %s from %s") % (song_name, artist_name))
                        
                        if "transfer playback" in command:
                            command = command.split()
                            for device in command:
                                if device == "computer":
                                    try:
                                        if device_id == available_devices_dict["computer"]:
                                            return spotify_speech.talk("You are already listening in your computer")
                                        else:
                                            spotify_speech.talk("Transfering playback to computer")
                                            return spotify.transfer_playback(available_devices_dict["computer"])
                                    except KeyError:
                                        return spotify_speech.talk("You don't have any computer available")
                                if device == "smartphone":
                                    try:
                                        if device_id == available_devices_dict["smartphone"]:
                                            return spotify_speech.talk("You are already listening in your smartphone")
                                        else:
                                            spotify_speech.talk("Transfering playback to smartphone")
                                            return spotify.transfer_playback(available_devices_dict["smartphone"])
                                    except:
                                        return spotify_speech.talk("You don't have any smartphone available")

                        if "play" == command:
                            return spotify.resume_playback(device_id)

                        if "pause" == command:
                            return spotify.pause_playback(device_id)

                        if "volume" in command:
                            volume = [int(s) for s in command.split() if s.isdigit()]
                            spotify_speech.talk(("Volume set to %d") % (volume[0]))
                            return spotify.set_volume(volume[0], device_id)

                        if "set repeat mode on" == command:
                            spotify_speech.talk("Repeat mode is on")
                            return spotify.set_repeat_mode(device_id=device_id)
                        
                        if "set repeat mode off" == command:
                            spotify_speech.talk("Repeat mode is off")
                            return spotify.set_repeat_mode("off", device_id)
                        
                        if "turn on shuffle mode" == command:
                            spotify_speech.talk("Shuffle mode is on")
                            return spotify.toggle_shuffle(True, device_id)
                        
                        if "turn off shuffle mode" == command:
                            spotify_speech.talk("Shuffle mode is off")
                            return spotify.toggle_shuffle(False, device_id)
                        
                        if "next track" in command:
                            return spotify.next_track(device_id)
                        
                        if "previous track" in command:
                            return spotify.previous_track(device_id)

                    else:
                        pass

            except:
                pass

        except Unauthorized:
            auth.request_token_with_refresh_token(refresh_token)



if __name__ == "__main__":
    pass
