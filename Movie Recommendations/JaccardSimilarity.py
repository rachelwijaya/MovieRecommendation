# import csv files
import numpy as np
import pandas as pd

movies_df = pd.read_csv('movies.csv', low_memory=False)
user_ratings_df = pd.read_csv('user_ratings.csv', low_memory=False)
# Dataset is now stored in a Pandas Dataframe

from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

#Returns a condensed matrix of all the distances

 # Crosstabulation
movies_genre_df = pd.crosstab(movies_df['title'], movies_df['genres'])

print("\n")

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
distance_df = pd.DataFrame(jaccard_similarity_array,
                           index=movies_genre_df.index,
                           columns=movies_genre_df.index)
distance_df.head()


# short description of how Jaccard Simmilarity works
print("\nJaccard Similarity measures the uniqueness and similarities")
print("between the movie titles and genres by calculating the")
print("similarity between data using a formula, ranging from 0 to 1.")
print("The closer to 1, the more similar it is.")

#Find a similar movie
movie_name = input("\nEnter a movie title: ")

# Find the values for the movie
# movie_name_genres = movies_genre_df[movies_genre_df.index == movie_name]
jaccard_similarity_series = distance_df.loc[movie_name]

# Sort these values from highest to lowest
ordered_similarities = jaccard_similarity_series.sort_values(ascending = False)

# Print the results
print("\nHere is your personalized movie recommendation:")
print(ordered_similarities.head())