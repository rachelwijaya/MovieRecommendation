
import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

def jaccard():
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
    distance_df = pd.DataFrame(jaccard_similarity_array, index=movies_genre_df.index, columns=movies_genre_df.index)
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

def cosine():
    pass

def kNN():
    import numpy as np
    import pandas as pd
    from scipy.sparse import csr_matrix  # convert into array matrix
    from sklearn.neighbors import NearestNeighbors  # unsupervised learning

    # create dataframes from csv files
    movies_df = pd.read_csv('movies.csv', usecols=['movieId', 'title'], dtype={'movieId': 'int32', 'title': 'str'})
    rating_df = pd.read_csv('user_ratings.csv', usecols=['userId', 'movieId', 'rating'],
                            dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

    # print("Movies Dataframe:\n", movies_df.head(10))
    # print("User Rating Dataframe:\n", rating_df.head(10))

    # Merge two of the dataframes on movieId as this is a common feature
    knnDf = pd.merge(rating_df, movies_df, on='movieId')

    movie_rated_df = knnDf.dropna(axis=0, subset=['title'])
    # select title as the set that we want
    # count the amount of ratings done of each movie, reset index so that title is not the index
    # This ensures that if let's say a movie has only 1 user who rates it a 5 stars, doesn't skew the data
    movie_rated_count = \
    (movie_rated_df.groupby(by=['title'])["rating"]).count().reset_index().rename(columns={'rating': 'ratingCount'})[
        ['title', 'ratingCount']]

    rateTotalMovieCount = movie_rated_df.merge(movie_rated_count, left_on='title', right_on='title', how='left')

    # Create pivot matrix
    threshold = 30
    rate_popular_movie = rateTotalMovieCount.query('ratingCount >= @threshold')
    movie_features_pivot = rate_popular_movie.pivot_table(index='title', columns='userId', values='rating').fillna(0)

    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    movie_features_df_matrix = csr_matrix(movie_features_pivot.values)
    model_knn.fit(movie_features_df_matrix)

    NearestNeighbors(algorithm='brute', leaf_size=30, metric='cosine', metric_params=None, n_jobs=None, n_neighbors=4,
                     p=1.5, radius=1.0)

    user_movie = input("Please enter a movie: ")
    index = movie_features_pivot.index.get_loc(user_movie)
    distances, indices = model_knn.kneighbors(movie_features_pivot.iloc[index, :].values.reshape(1, -1), n_neighbors=6)

    for i in range(0, len(distances.flatten())):
        if i == 0:
            print("Recommendations for {0}:\n".format(movie_features_pivot.index[index]))
        else:
            print("{0}: {1}, with distance of {2}:".format(i, movie_features_pivot.index[indices.flatten()[i]],
                                                           distances.flatten()[i]))

def content_menu():

    print("\n")
    print(20 * "-", "CONTENT-BASED ALGORITHM", 20 * "-")

    # Options
    print("1. Jaccard Simillarity")
    print("2. Cosine Similarity")
    print("3. Exit")

    print(67 * "-")

    choice1 = int(input("\nPlease choose your preferable action [1-3]: \n"))

    choice1_dict = {
        1: jaccard,
        2: cosine,
        3: exit,
    }

    choice1_dict[choice1]()


def user_menu():

    print("\n")
    print(25 * "-", "USER-BASED ALGORITHM", 25 * "-")

    # Options
    print("1. k-Nearest Neighbour")
    print("2. Cosine Similarity")
    print("3. Exit")

    print(67 * "-")

    choice2 = int(input("\nPlease choose your preferable action [1-3]: \n"))

    choice2_dict = {
        1: kNN,
        2: cosine,
        3: exit,
    }

    choice2_dict[choice2]()


# Main Menu Function

def main_menu():

    print("\n We are going to analyze several different algorithms used in Recommendation Engines. \n")

    print(30 * "-", "MAIN MENU", 30 * "-")

    # Options
    print("1. Display content-based recommendations")
    print("2. Display user-based recommendations")
    print("3. Exit")

    print(67 * "-")

    choice = int(input("\nPlease choose your preferable action [1-3]: \n"))

    choice_dict = {
        1: content_menu,
        2: user_menu,
        3: exit,
    }

    choice_dict[choice]()


if __name__ == "__main__":
    print("----------------------" + \
          "Analysis of Algorithms" + \
          "----------------------")

main_menu()
