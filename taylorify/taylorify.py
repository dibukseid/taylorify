from .utils import get_spotify_client

sp = get_spotify_client()


def find_taylors_version(original_song_name, artist="Taylor Swift"):
    """Find Taylor’s Version of a song, handling cases with featured artists and ensuring correct album selection."""
    search_query = f"{original_song_name} Taylor's Version artist:{artist}"
    results = sp.search(q=search_query, limit=20, type="track")  

    for track in results['tracks']['items']:
        track_name = track['name']
        track_artists = [a['name'].lower() for a in track['artists']] 
        album_name = track['album']['name'].lower()

        # Debugging output

        #handle fearless separately since it doesn't work
        if "taylor swift" in track_artists and album_name == "fearless (taylor's version)":
            return track['id']
        
        #same with Red but specifically doesn't work for features 
        if "taylor swift" in track_artists and album_name == "red (taylor's version)":
            return track['id']
        
        # Ensure Taylor Swift is in the artist list (allowing for featured artists)
        if "taylor swift" in track_artists and "taylor's version" in track_name.lower():
            
            
            # If it's any other Taylor’s Version album, return it
            return track['id']

    return None  # If no valid Taylor’s Version is found, return None




def replace_songs_in_playlist(playlist_id):
    """Replace Taylor Swift songs with Taylor's Version while keeping the original order."""
    playlist_tracks = sp.playlist_tracks(playlist_id)
    track_positions = {}  # Store original positions

    for index, item in enumerate(playlist_tracks['items']):
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        track_id = track['id']

        # Only process songs by Taylor Swift (changed to include features)
        if "taylor swift" in artist_name.lower():
            new_version_id = find_taylors_version(track_name)

            if new_version_id:
                print(f"Replacing {track_name} with Taylor's Version at position {index+1}...")
                
                # Store the original position so the playlist is not changed 
                track_positions[new_version_id] = index
                
                # Remove the old song
                sp.playlist_remove_all_occurrences_of_items(playlist_id, [track_id])
                
                sp.playlist_add_items(playlist_id, [new_version_id], position=index)
            else:
                print(f"No Taylor's Version found for {track_name}, skipping.")

    print("\n 🥳 Playlist update complete! \n")



def replace_in_all_playlists():
    """Replace Taylor Swift songs with Taylor's Version in all playlists owned by the user."""
    user_id = sp.current_user()["id"]  # Get the current user's Spotify ID
    playlists = sp.current_user_playlists()

    for playlist in playlists["items"]:
        playlist_id = playlist["id"]
        playlist_name = playlist["name"]
        owner_id = playlist["owner"]["id"]

        # Only modify playlists that the user owns
        if owner_id == user_id:
            print(f"🔍 Processing your playlist: {playlist_name}")
            replace_songs_in_playlist(playlist_id)
        else:
            print(f"⏩ Skipping '{playlist_name}' (not owned by you)")

    print("\n🎶 All playlists updated successfully!")


