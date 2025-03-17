import streamlit as st
from taylorify.taylorify import replace_songs_in_playlist, replace_in_all_playlists

# Streamlit UI
st.title(" Taylorify: Upgrade Your Spotify Playlists to Taylor’s Version")

st.write("Automatically replace stolen versions of Taylor's songs with Taylor's Version!\n")

st.write("Don't worry! The order of your songs will remain the same and will only affect Taylor Swift songs that have an existing Taylor's Version! (:")

st.write("Come back and update your playlists again after Rep TV and Debut TV come out!")
# User selects mode
mode = st.radio("Choose an option:", ["Update a single playlist", "Update all playlists"])

if mode == "Update a single playlist":
    st.write("This will update a specific playlist using the playlist URL")
    playlist_id = st.text_input("Enter your Spotify Playlist URL or ID:")

    if st.button("Upgrade My Playlist"):
        if playlist_id:
            replace_songs_in_playlist(playlist_id)
            st.success("Playlist updated successfully! Happy Streaming! (:")
        else:
            st.error("⚠️ Please enter a valid Playlist ID or URL.")

elif mode == "Update all playlists":
    st.write("This will find and update all playlists in your Spotify account.")

    if st.button("Upgrade All My Playlists"):
        replace_in_all_playlists()
        st.success("All playlists updated successfully! Happy Streaming! (:")

st.write("Made with ❤️ By Buki for Swifties 🎤")

col1, col2 = st.columns(2)

with col1:
    if st.button("📷 Follow on Instagram"):
        st.markdown("[Click Here](https://www.instagram.com/bukillah)", unsafe_allow_html=True)

with col2:
    if st.button("🎵 Follow on TikTok"):
        st.markdown("[Click Here](https://www.tiktok.com/@bukillahs_playground)", unsafe_allow_html=True)
