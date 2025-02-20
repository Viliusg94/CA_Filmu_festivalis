import pickle


def load_movies():
    try:
        with open("movies.pickle", "rb") as file:
            budget = pickle.load(file)
        return budget
    except FileNotFoundError:
        movies = []
        return movies


def load_guests():
    try:
        with open("users.pickle", "rb") as file:
            budget = pickle.load(file)
        return budget
    except FileNotFoundError:
        guests = []
        return guests


def save_file(festival):
    with open("guests.pickle", "wb") as file:
        pickle.dump(festival, file)