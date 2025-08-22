import json 
import os
import base64
from dotenv import load_dotenv
from requests import post 
from requests import get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.text)
    token = json_result.get("access_token")
    return token

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No results found.")
        return None
    
    return json_result[0]

def get_top_tracks(token, artist_id, country="US", limit=5):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={country}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]

    if result.status_code != 200:
        print("Error fetching top tracks:", result.status_code)
        return []

    return json_result[:limit]

def format_duration(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

def main():
    token = get_token()
    while True:
        artist_name = input("\nEnter an artist name (or 'quit' to exit): ").strip()
        if artist_name.lower() == "quit":
            break

        artist = search_artist(token, artist_name)
        if artist is None:
            continue

        print(f"\nArtist: {artist['name']}")
        print(f"Followers: {artist['followers']['total']:,}")
        print(f"Genres: {', '.join(artist['genres']) if artist['genres'] else 'N/A'}")
        print(f"Popularity: {artist['popularity']} / 100")

        top_tracks = get_top_tracks(token, artist["id"])
        if not top_tracks:
            print("No top tracks available.")
            continue

        print("\nTop Tracks:")
        for i, track in enumerate(top_tracks, 1):
            name = track["name"]
            album = track["album"]["name"]
            release = track["album"]["release_date"]
            duration = format_duration(track["duration_ms"])
            popularity = track["popularity"]
            preview = track["preview_url"] or "N/A"
            print(f"{i}. {name} ({album}, {release})")
            print(f"   Duration: {duration}, Popularity: {popularity}, Preview: {preview}")

if __name__ == "__main__":
    main()
