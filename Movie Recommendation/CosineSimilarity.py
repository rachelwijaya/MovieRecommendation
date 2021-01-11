import pandas as pd
import numpy as np
import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

movies_df = pd.read_csv('movies.csv', low_memory=False)
user_ratings_df = pd.read_csv('user_ratings.csv', low_memory=False)
# Dataset is now stored in a Pandas Dataframe

#helper functions
cv = CountVectorizer()

def get_title_from_index(index):
 return movies_df[movies_df.index == index]["title"].values[0]

def get_index_from_title(title):
 return movies_df[movies_df.title == title]["index"].values[0]

#selecting the feature
features = ['title', 'genres']
for feature in features:
 movies_df[feature] = movies_df[feature].fillna('')

#combining all selected features into one column
def combined_features(row):
    try:
        return row['title'] + " " + row['genres']
    except:
        print("Error:", row)

movies_df["index"] = range(len(movies_df))
movies_df["combined_features"] = movies_df.apply(combined_features,axis=1)
                                                    #will pass each row individually instead of columns

print("\ncombined features: ")
print(movies_df["combined_features"].head())

def recommendedMovieList(user_movie):
    #creating a count matrix from the combined column
    count_matrix = cv.fit_transform(movies_df["combined_features"])

    #finding the cosine similarity value from the count matrix
    cosine_sim = cosine_similarity(count_matrix)

    #getting the movieId from its title
    movie_index = get_index_from_title(user_movie)

    #getting a list of similar movies by calculating their similarity scores
    similar_movies = list(enumerate(cosine_sim[movie_index]))

    #sorting the similarity scores in descending order
    return sorted(similar_movies, key=lambda x:x[1], reverse=True)

# short description of how Cosine Simmilarity works
print("\nCosine Similarity compares the frequency of words that appear in")
print("the movie titles in order to see how similar they are to your input")

#asking for user input
user_movie = input("\nPlease enter a movie: ")

t1 = time.perf_counter()
movie_list = recommendedMovieList(user_movie)

#printing the titles of 5 movies that are found to be similar
print("\n Here is your personalized movie recommendation:")
i = 0
for movie in movie_list:
  print(get_title_from_index(movie[0]))
  i += 1
  if i > 5:
   break
t2 = time.perf_counter()
print('\nTime_elapsed: ', t2-t1)
