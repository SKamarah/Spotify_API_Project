import requests

#Reference to Spotify's create playlist API
#Access Token that allows a user to use API
SPOTIFY_CREATE_PLAYLISTS_URL = "https://api.spotify.com/v1/users/31bqvovehavga6adndylwwjchrxe/playlists"
ACCESS_TOKEN = "BQC85ZWY-B2gHgxZh4DRUBHpscCPRbWXsjQ3OrOiLemNWL8QX3grGwi12GjXIj7EmXdfTIn07MUQsMRgVEDiEpLncj7DMc3gWbP5QmLQYoeaF9KMnSYm0Y895TjMHeu1UeXk3jGR_WYjj_N1l32TI3wg9kiPaCvsl-9pS1T2KIOougsDwc-pOx1T8rRLY3RNAW-NaYx0ShC75ENg2ZqINAUhfAntfe1J"
#Creating playlist by making request out to endpoint
def create_playlist(name ,public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLISTS_URL,
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist(
        name ="Young Thug Essentials",
        public = True)

    print(f"Playlist: {playlist}")

if __name__ == "__main__":
    main()