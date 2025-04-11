import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Streamlit Cloud will redirect to your app URL
REDIRECT_URI = "https://musicmoods.streamlit.app"

# Define scopes for personalized data
SCOPE = "user-read-private user-top-read user-library-read"

auth_manager = SpotifyOAuth(
    client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
    client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
    redirect_uri="https://musicmoods.streamlit.app",
    scope="user-read-private user-top-read user-library-read",
    show_dialog=True  # always prompt login
)

sp = spotipy.Spotify(auth_manager=auth_manager)

def get_current_user():
    return sp.current_user()

def get_songs_by_mood(mood):
    if mood == 'happy':
        valence = 0.7
    elif mood == 'angry':
        valence = 0.2
    else:
        valence = 0.5

    top_genres = ['chill', 'pop', 'indie']

    results = sp.recommendations(seed_genres=top_genres, target_valence=valence, limit=10)

    songs = []
    for track in results['tracks']:
        songs.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify'],
            'image': track['album']['images'][0]['url']
        })
    
    return songs