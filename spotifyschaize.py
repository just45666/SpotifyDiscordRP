# some libs
import time
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from pypresence import Presence

# spotify creds
SPOTIPY_CLIENT_ID = 'your_spotify_client'
SPOTIPY_CLIENT_SECRET = 'your_spotify_secret'
SPOTIPY_REDIRECT_URI = 'https://localhost:8080' #or your redirect uri

# discord creds
DISCORD_CLIENT_ID = 'your_discord_client'

# spotify setup
scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# discord crap
discord_rpc = Presence(DISCORD_CLIENT_ID)
discord_rpc.connect()

# main shiz
while True:
    try:
        current_track = sp.current_user_playing_track()
        if current_track is not None:
            song_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            # update DiscordRP
            discord_rpc.update(state=song_name, details=f"by {artist_name}")
        time.sleep(15)  # sleep 15 sec bcuz API bs
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# disconnect
discord_rpc.close()
