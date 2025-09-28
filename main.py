from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

year = input("Which year do you wanna travel to? (Please use YYYY-MM-DD format): ")

header = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"}

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="https://example.com",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("SPOTIFY_CLIENT_ID"),
    )
)

user_id = sp.current_user()["id"]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/",
                        headers=header)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

all_songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in all_songs]

YYYY = year.split("-")[0]

song_uris = []
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{YYYY}", type="track", limit=1)
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"❌ Song not found on Spotify: {song}")
print(song_uris)