from spotify.spotify_credentials import SpotifyCredentials
from spotify.spotify_auth import AuthorizationCodeFlow
from spotify.spotify_api_reference import SpotifyPlayer
from spotify.error_handling import *
import speech_recognition as sr
from assistant_engine import VirtualAssistant


listener = sr.Recognizer()
spotify_speech = VirtualAssistant()


selected_device = ""
spotify = ""

def app():
    global spotify
    global selected_device
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.pause_threshold = 1
            user_voice = listener.listen(source, timeout=0)
            command = listener.recognize_google(user_voice, language="en-US")
            command = command.lower()
            
            if "spotify" in command:
                command = command.replace("spotify ", "")
                print(command)
                
                if "play" == command:
                    try:
                        return spotify.resume_playback(selected_device)
                    except Unauthorized:
                        init()
                    
                
                if "pause" == command:
                    try:
                        return spotify.pause_playback(selected_device)
                    except Unauthorized:
                        init()
                
                if "volume" in command:
                    volume = [int(s) for s in command.split() if s.isdigit()]
                    spotify_speech.talk(("Setting volume to %d") % (volume[0]))
                    
                    try:
                        return spotify.set_volume(volume[0], selected_device)
                    except Unauthorized:
                        init()

                if "set repeat mode on" == command:
                    spotify_speech.talk("Setting repeat mode on")
                    try:
                        return spotify.set_repeat_mode(device_id=selected_device)
                    except Unauthorized:
                        init()
                
                if "set repeat mode off" == command:
                    spotify_speech.talk("Setting repeat mode off")
                    try:
                        return spotify.set_repeat_mode("off", selected_device)
                    except Unauthorized:
                        init()
                
                if "turn on shuffle mode" == command:
                    spotify_speech.talk("Setting shuffle mode on")
                    try:
                        return spotify.toggle_shuffle(True, selected_device)
                    except Unauthorized:
                        init()
                
                if "turn off shuffle mode" == command:
                    spotify_speech.talk("Setting shuffle mode off")
                    try:
                        return spotify.toggle_shuffle(False, selected_device)
                    except Unauthorized:
                        init()
                
                if "next song" in command:
                    try:
                        return spotify.next_track(selected_device)
                    except Unauthorized:
                        init()
                
                if "previous song" in command:
                    try:
                        return spotify.previous_track(selected_device)
                    except Unauthorized:
                        init()

                if "song name" in command:
                    try:
                        current_playback = spotify.current_playback().json()
                        song_name = current_playback ["item"]["name"]
                        artist_name = current_playback ["item"]["album"]["artists"][0]["name"]
                        return spotify_speech.talk(("You are listening to %s from %s") % (song_name, artist_name))
                    except Unauthorized:
                        init()
        
                if "devices" in command:
                    try:
                        available_devices = spotify.available_devices().json()
                        available_devices = available_devices["devices"]
                        total_available_devices = len(available_devices)
            
                        if total_available_devices > 1:
                            return spotify_speech.talk("You have %d available devices." % (total_available_devices))
                        else:
                            return spotify_speech.talk("You have one available device.")
                    except Unauthorized:
                        init()

                if "transfer playback" in command:
                    command = command.split()
                    
                    try:
                        available_devices = spotify.available_devices().json()
                        available_devices = available_devices["devices"]
                        available_devices_dict = {}

                        for device in available_devices:
                            if device["type"] == "Computer":
                                available_devices_dict.update({"computer":device["id"]})
                            elif device["type"] == "Smartphone":
                                available_devices_dict.update({"smartphone":device["id"]})
                    
                        
                        for device in command:
                            if device == "computer":
                                try:
                                    if selected_device == available_devices_dict["computer"]:
                                        return spotify_speech.talk("You are already listening in your computer")
                                    else:
                                        spotify_speech.talk("Transfering playback to computer")
                                        spotify.transfer_playback(available_devices_dict["computer"])
                                        selected_device = available_devices_dict["computer"]

                                except KeyError:
                                    return spotify_speech.talk("You don't have any computer available")

                            if device == "smartphone":
                                try:
                                    if selected_device == available_devices_dict["smartphone"]:
                                        return spotify_speech.talk("You are already listening in your smartphone")
                                    else:
                                        spotify_speech.talk("Transfering playback to smartphone")
                                        spotify.transfer_playback(available_devices_dict["smartphone"])
                                        selected_device = available_devices_dict["smartphone"]
                                        
                                except KeyError:
                                    return spotify_speech.talk("You don't have any smartphone available")
                            
                    except Unauthorized:
                        init()
                
                
    except Exception:
        pass
    
def init():

    credentials = SpotifyCredentials()
    access_token = credentials.Tokens().access_token
    refresh_token = credentials.Tokens().refresh_token
    expires_in = credentials.Tokens().expires_in

    auth = AuthorizationCodeFlow(credentials.client_id,
                                credentials.client_secret,
                                credentials.redirect_uri)

    global spotify
    spotify = SpotifyPlayer(access_token)

    if access_token == None:
        auth.request_authorization_and_token()
        init()

    else:
        try:
            available_devices = spotify.available_devices().json()
            available_devices = available_devices["devices"]
            total_available_devices = len(available_devices)
            global selected_device
            
            # Check for available devices
            if total_available_devices > 1:
                spotify_speech.talk("You have %d available devices. Please choose one!" % (total_available_devices))
                
                # Choose device
                for index in range(total_available_devices):
                    print(f"[{index}] " + available_devices[index]["type"] + ": " + available_devices[index]["name"])
                selected_device = input("Choose device (int): ")
                try:
                    selected_device = int(selected_device)
                    if (int(selected_device) + 1) > total_available_devices:
                        print("Index out of range!")
                        return init()

                    selected_device = available_devices[selected_device]["id"]
                    try:
                        spotify.transfer_playback(selected_device)
                    except Unauthorized:
                        return init()
                    except InternalServerError:
                        pass
                    
                    while True:
                        app()
                except ValueError:
                    print("Type device index. Don't use letters!")
                    return init()
    
            
            if total_available_devices == 0:
                spotify_speech.talk("You have no available devices.")

            else:
                selected_device = available_devices[0]["id"]
                while True:
                    app()
                
        except Unauthorized:
            auth.request_token_with_refresh_token(refresh_token)
            init()

if __name__ == "__main__":
    init()

