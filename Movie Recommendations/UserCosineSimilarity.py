# import csv files
import numpy as np
import pandas as pd

movies_df = pd.read_csv('movies.csv', low_memory=False)
user_ratings_df = pd.read_csv('user_ratings.csv', low_memory=False)
# Dataset is now stored in a Pandas Dataframe

from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

ratings = pd.merge(movies_df, user_ratings_df).drop(['genres', 'timestamp'], axis=1)
userRatings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')

# Remove movies that have less than 10 user's rating (that are not NaN) and fill NaN values with 0
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0, axis=1)

# similarity Matrix
item_similarity_df = userRatings.corr(
    method='pearson')  # in-build method of dataframe of standardizing rating given by all user


# Find the similarity between movies
def get_similar(movie_name, rating):
    similar_ratings = item_similarity_df[movie_name] * (rating - 2.5)
    # Scale it based on the rating the user gave
    similar_ratings = similar_ratings.sort_values(ascending=False)
    # print(type(similar_ratings))
    return similar_ratings

# short description of how Cosine Simmilarity works
print("\nCosine Similarity compares the frequency of movies that")
print("appear in other users in order to assume their similarity")
print("to your input")

# Make a recommendation
# sample input for Cally to insert = [("Amazing Spider-Man, The (2012)",5),("Mission: Impossible III (2006)",4),("Toy Story 3 (2010)",2),("2 Fast 2 Furious (Fast and the Furious 2, The) (2003)",4)]
print("\nNOTE: input format, please enter movie name then the rating(out of 5)")
movie_lst = []
n = int(input("Enter number of movies you want to rate : "))

for i in range(0, n):
    ele = [input(), int(input())]
    movie_lst.append(ele)

similar_movies = pd.DataFrame()
for movie, rating in movie_lst:
    similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)

similar_movies.head(10)
print("\nHere is your personalized movie recommendation: \n")
print(similar_movies.sum().sort_values(ascending=False).head(20))