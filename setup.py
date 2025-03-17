from setuptools import setup, find_packages

setup(
    name="taylorify",
    version="0.1",
    packages=find_packages(),
    install_requires=["spotipy", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "taylorify=taylorify.taylorify:replace_in_all_playlists",
        ],
    },
    author="Millenna Dibuk (Buki) Seid",
    description="Automatically replace Taylor Swift songs with Taylor's Version in all Spotify playlists.",
)
