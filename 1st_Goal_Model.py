import pandas as pd

song_attr = pd.read_csv("train.csv")

CPTs = {}

#Calculate all probabilites P(song|genre, (popularity>.50)) that are used for basic song compatibility
all_genres = song_attr['Class'].tolist()
for genre in all_genres:
    genre_sum = (song_attr['Class'] == genre).sum()
    for index, row in song_attr.iterrows():
        if any(pd.isna(getattr(row, col)) for col in song_attr.columns):
            CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = 0
            continue
        if (int(row.Popularity) > 0.50):
            CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = (1+row.Popularity)/genre_sum
        else:
            CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = (row.Popularity)/genre_sum

# Display the first few rows
print(df.head())