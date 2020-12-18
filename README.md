<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://avatars3.githubusercontent.com/u/73149577?s=460&u=1baa1defb9904624d7aad76ec37dc76d2b230c0a&v=4" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Spotify Voice Control</h3>

  <p align="center">
    Manage spotify playback state with voice control.
    <br />
    <a href="https://github.com/LucasACH/spotify-virtual-assistant"><strong>Explore the docs »</strong></a>
  </p>
</p>

<!-- PREREQUISITES -->
### Prerequisites

* [Spotify account](https://www.spotify.com/)
* [Spotify App](https://developer.spotify.com/documentation/general/guides/app-settings/)
* [Python 3.6.8](https://www.python.org/downloads/release/python-368/)
* Microphone


### Installation

1. Save Client Id, Client Secret and Redirect Uri as [variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) in your os enviroment. You can find them in your [Dashboard](https://developer.spotify.com/dashboard/applications)
   ```sh
   SPOTIFY_CLIENT_ID = client_id
   SPOTIFY_CLIENT_SECRET = client_secret
   SPOTIFY_REDIRECT_URI = redirect_uri
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/LucasACH/spotify-virtual-assistant.git
   ```
3. Activate python virtual enviroment
   ```sh
   venv\Scripts\activate.bat
   ```


<!-- USAGE EXAMPLES -->
## Usage

To start using the voice control make sure to have spotify open on at least one device.
  ```sh
  python app.py
  ```

You can now use these voice commands for changing your current spotify playback state

| Voice command   | Action
| ------|-----
| *spotify pause* 	| Pause playback on the user’s account
| *spotify play* 	| Resume a user's playback
| *spotify next song* 	| Skip user's playback to next track
| *spotify previous song* 	| Skip user's playback to previous track
| *spotify set volume to [volume %]* 	| Set the volume for the user’s current playback device
| *spotify set repeat mode on* 	| Set the repeat mode on for the user’s playback
| *spotify set repeat mode off* 	| Set the repeat mode off for the user’s playback
| *spotify turn on shuffle mode* 	| Toggle shuffle on for user’s playback
| *spotify turn off shuffle mode* 	| Toggle shuffle off for user’s playback
| *spotify current song name* 	| Get information about a user’s current song
| *spotify devices* 	| Get information about a user’s available devices
| *spotify transfer playback to [computer or smartphone]* 	| Transfer playback to a new device and determine if it should start playing.


<!-- CONTACT -->
## Contact

Lucas Achaval <br />
<br />
<img src="https://logos-marcas.com/wp-content/uploads/2020/11/Gmail-Logo.png" width="30"> achaval.lucas@gmail.com
<br />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Stack_Overflow_icon.svg/768px-Stack_Overflow_icon.svg.png" width="30"> [LucasACH](https://stackoverflow.com/users/14665518/lucasach)
