import pandas as pd

#Calculate all probabilites P(song|genre, (popularity>.50)) that are used for basic song compatibility
def song_query_agent(csv):
    song_attr = pd.read_csv(csv)

    #Initial state
    CPTs = {}

    all_genres = song_attr['Class'].tolist()
    for genre in all_genres:
        genre_sum = (song_attr['Class'] == genre).sum()
        #Calculate subsequent states
        for index, row in song_attr.iterrows():
            #Check if forthcoming state matches with rule/condition
            if any(pd.isna(getattr(row, col)) for col in song_attr.columns):
                #Update CPT as the agent's action
                CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = 0
                continue
            if (int(row.Popularity) > 0.50):
                CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = (1+row.Popularity)/genre_sum
            else:
                CPTs[str(getattr(row, "Track Name")) + "|" + str(genre)] = (row.Popularity)/genre_sum
    return CPTs

print(song_query_agent("train.csv"))