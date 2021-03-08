import pandas as pd

df = pd.read_csv(r'sp_analysis.csv')
type_of_music = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'valence']
tempo = df['tempo'].mean()
genre_num = ['acousticness', 0]

for genre in type_of_music:
    mean = df[genre].mean()
    if mean > genre_num[1]:
        genre_num[0] = genre
        genre_num[1] = mean

most_popular_song = df['popularity'].max()
total_songs = df['track_number'].count()
album_with_most_songs = df.groupby(['album']).count()

print(total_songs, "songs")
print(genre_num[0], "common genre")
