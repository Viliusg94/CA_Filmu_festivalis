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

def save_movies(movies):
    with open("movies.pickle", "wb") as file:
        pickle.dump(movies, file)

def load_guests():
    try:
        with open("users.pickle", "rb") as file:
            guests = pickle.load(file)
        return guests
    except FileNotFoundError:
        guests = []
        return guests
    
def save_guests(guests):
    with open("users.pickle", "wb") as file:
        pickle.dump(guests, file)


def load_schedule():
    try:
        with open ("schedule.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        schedule = []
        return schedule

def save_schedule(schedule):
    with open("schedule.pickle", "wb") as file:
        pickle.dump(schedule, file)
