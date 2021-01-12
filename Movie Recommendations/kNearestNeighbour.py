import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix # convert into array matrix
from sklearn.neighbors import NearestNeighbors # unsupervised learning

# create dataframes from csv files
movies_df = pd.read_csv('movies.csv', usecols=['movieId','title'], dtype={'movieId': 'int32', 'title': 'str'})
rating_df = pd.read_csv('user_ratings.csv', usecols=['userId', 'movieId', 'rating'], dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

# print("Movies Dataframe:\n", movies_df.head(10))
# print("User Rating Dataframe:\n", rating_df.head(10))

# Merge two of the dataframes on movieId as this is a common feature
knnDf = pd.merge(rating_df, movies_df, on='movieId')

movie_rated_df = knnDf.dropna(axis=0, subset=['title'])
# select title as the set that we want
# count the amount of ratings done of each movie, reset index so that title is not the index
# This ensures that if let's say a movie has only 1 user who rates it a 5 stars, doesn't skew the data
movie_rated_count = (movie_rated_df.groupby(by=['title'])["rating"]).count().reset_index().rename(columns={'rating':'ratingCount'})[['title', 'ratingCount']]


rateTotalMovieCount = movie_rated_df.merge(movie_rated_count, left_on = 'title', right_on = 'title', how = 'left')

# Create pivot matrix
threshold = 30
rate_popular_movie = rateTotalMovieCount.query('ratingCount >= @threshold')
movie_features_pivot = rate_popular_movie.pivot_table(index ='title', columns='userId', values='rating').fillna(0)

model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
movie_features_df_matrix = csr_matrix(movie_features_pivot.values)
model_knn.fit(movie_features_df_matrix)

NearestNeighbors(algorithm='brute', leaf_size=30, metric='cosine', metric_params=None, n_jobs=None, n_neighbors=4, p=1.5, radius=1.0)

# short description of how k-Nearest Neighbour works
print("\nk-Nearest Neighbour (kNN) works by finding the distances between")
print("a predicted data and all the examples in the data, specifying how")
print("many neighbours to take in (K) closest to the predicted data, then")
print("recommends the movies that are close by distance.")
print("\nIn this case, it assumes the similarity between the movies and")
print("classifies them into categories based on other users' input")

user_movie = input("\nPlease enter a movie: ")
index = movie_features_pivot.index.get_loc(user_movie)
distances, indices = model_knn.kneighbors(movie_features_pivot.iloc[index, :].values.reshape(1, -1), n_neighbors = 6)


for i in range(0, len(distances.flatten())):
    if i == 0:
        print("\nHere is your personalized movie recommendation:")
        print("~ Based on {0} ~\n".format(movie_features_pivot.index[index]))
    else:
        print("{0}: {1}, with distance of {2}:".format(i, movie_features_pivot.index[indices.flatten()[i]], distances.flatten()[i]))