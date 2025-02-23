import pickle

def load_movies():
    try:
        with open("movies.pickle", "rb") as file:
            try:
                movies = pickle.load(file)
            except EOFError:
                movies = []
        return movies
    except FileNotFoundError:
        movies = []
        return movies

def load_guests():
    try:
        with open("users.pickle", "rb") as file:
            guests = pickle.load(file)
        return guests
    except FileNotFoundError:
        guests = []
        return guests

def save_movies(movies):
    with open("movies.pickle", "wb") as file:
        pickle.dump(movies, file)

def save_guests(guests):
    with open("users.pickle", "wb") as file:
        pickle.dump(guests, file)