import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

# Read csv files to create dataframes
movies_df = pd.read_csv("movies.csv", dtype={'movieId': 'int32', 'title': 'str'})
print((movies_df.head()))
user_ratings_df = pd.read_csv("user_ratings.csv")

# Returns a condensed matrix of all the distances

# Crosstabulation
movies_genre_df = pd.crosstab(movies_df['title'], movies_df['genres'])

# Find distance between all items
# WARNING: please be patient, calculating this is going to take a minute or two
jaccard_distances = pdist(movies_genre_df.values, metric='jaccard')
print(jaccard_distances)

# Get the data into a rectangular shape based on the previous matrix
square_jaccard_distances = squareform(jaccard_distances)
print(square_jaccard_distances)

# Convert the distances to a square matrix
jaccard_similarity_array = 1 - square_jaccard_distances
print(jaccard_similarity_array)

# Create a dataframe for the distance of each book according to its genre
distance_df = pd.DataFrame(jaccard_similarity_array,index=movies_genre_df.index, columns=movies_genre_df.index)
distance_df.head()

# Find a similar movie
movie_name = input("Enter a movie title: ")

# Find the values for the movie
# movie_name_genres = movies_genre_df[movies_genre_df.index == movie_name]
jaccard_similarity_series = distance_df.loc[movie_name]

# Sort these values from highest to lowest
ordered_similarities = jaccard_similarity_series.sort_values(ascending=False)

# Print the results
print("\nMovies you would like:")
print(ordered_similarities.head())