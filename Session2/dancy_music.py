# Using the Spotify dataset to get some dancy music!
import numpy as np
import pandas as pd

song_df = pd.read_csv("genres_v2.csv")

median_danceability = song_df.danceability.median()
median_valence = song_df.valence.median()
genre_filter = ["Pop", "Hiphop", "RnB"]

happy_dancy_songs = song_df[
    (song_df.valence > median_valence) & (song_df.danceability > median_danceability)
]

filtered_happy_dancy_songs = happy_dancy_songs[
    happy_dancy_songs.genre.isin(genre_filter)
]

myplaylist = filtered_happy_dancy_songs.sample(n=5)

print("\nMy Five Song Playlist is:")

for idx, row in myplaylist.iterrows():
    print("\t%s" % row.song_name)
