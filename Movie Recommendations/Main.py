def jaccard():
    import JaccardSimilarity

def cosine():
    import CosineSimilarity

def userCosine():
    import UserCosineSimilarity

def kNN():
    import kNearestNeighbour

def content_menu():

    print("\n")
    print(20 * "-", "CONTENT-BASED ALGORITHM", 20 * "-")

    print("\nYou are in the content-based algorithm section.")
    print("\nHere are two algorithms you can choose to implement in this")
    print("recommendation system\n")

    # Options
    print("1. Jaccard Simillarity")
    print("2. Cosine Similarity")
    print("3. Exit")

    print(67 * "-")

    choice1 = int(input("\nPlease choose your preferable action [1-3]: "))

    choice1_dict = {
        1: jaccard,
        2: cosine,
        3: exit,
    }

    choice1_dict[choice1]()


def user_menu():

    print("\n")
    print(25 * "-", "USER-BASED ALGORITHM", 25 * "-")

    print("\nYou are in the user-based algorithm section.")
    print("This type of algorithm is also known as 'Collaborative Filtering'")
    print("Here are two algorithms you can choose to implement in this")
    print("recommendation system\n")

    # Options
    print("1. k-Nearest Neighbour")
    print("2. Cosine Similarity")
    print("3. Exit")

    print(67 * "-")

    choice2 = int(input("\nPlease choose your preferable action [1-3]: "))

    choice2_dict = {
        1: kNN,
        2: userCosine,
        3: exit,
    }

    choice2_dict[choice2]()


# Main Menu Function

def main_menu():

    print("\n In this project, we are going to analyze several different")
    print("algorithms used in Recommendation Engines. \n")

    print(30 * "-", "MAIN MENU", 30 * "-")

    print("\n")
    print("Content Based Algorithms will filter data generate data according to")
    print("a description of the item and a profile of the user's preferences.")
    print("In this case, the movies are generated based on 'genre' category.")

    print("\n")
    print("User Based Algorithms will filter data and generate suggestions")
    print("according to assumptions that people who agreed in the past will agree")
    print("in the future, and that they will like similar kinds of items as they ")
    print("liked in the past")

    # Options
    print("\n")
    print("1. Display content-based recommendations")
    print("2. Display user-based recommendations")
    print("3. Exit")

    print(67 * "-")

    choice = int(input("\nPlease choose your preferable action [1-3]: "))

    choice_dict = {
        1: content_menu,
        2: user_menu,
        3: exit,
    }

    choice_dict[choice]()


if __name__ == "__main__":

    print("\n")
    print("----------------------" + \
          "Analysis of Algorithms" + \
          "----------------------")

main_menu()