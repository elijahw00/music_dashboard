import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='d7a7dbcb06af46f5852e67b9e81f8f50',
    client_secret='222d9a8c53014b6ab3bfcf0b2d6bed05',
    redirect_uri='http://127.0.0.1:8501/',
    scope=['user-library-read', 'playlist-modify-public']
))

# Test authentication
current_user = sp.current_user() #get current user details
print(f"Authenticated as: {current_user['display_name']}")

def get_songs_by_mood(mood):
    if mood == 'happy':
        valence = 0.7 #a higher valence corresponds to a happier mood
    elif mood == 'angry':
        valence = 0.2 #a lower valence corresponds to a more angry mood
    else:
        valence = 0.5 #neutral valence
    
    # Search for tracks with the specified valence
    results = sp.recommendations(seed_genres=['chill'], target_valence=valence, limit=10)

    songs = []
    for track in results['tracks']:
                songs.append({
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'url': track['external_urls']['spotify'],
                    'image': track['album']['images'][0]['url']
                })
    return songs