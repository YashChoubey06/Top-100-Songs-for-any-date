from bs4 import BeautifulSoup
import requests

year = input("Which year do you wanna travel to? (Please use YYYY-MM-DD format): ")

header = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/", header)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

all_songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in all_songs]
print(song_names)