def jaccard():
    import JaccardSimilarity

def cosine():
    pass

def userCosine():
    import UserCosineSimilarity

def kNN():
    import kNearestNeighbour

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
        2: userCosine,
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
