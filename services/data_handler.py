import pickle
import os

# Absoliutus pathas iki admin_menu failo (nuo pat disko) __file__ nurodo kelią iki failo ir nuiima paskutinį lygį. 
#be os.path.dirname pathas gaunasi c:\..\..\Desktop\CA_Filmu_festivalis\services\movie_handler.py
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)

def load_movies():
    try:
        with open(os.path.join(data_dir, "movies.pickle"), "rb") as file:
            try:
                movies = pickle.load(file)
            except EOFError:
                movies = []
        return movies
    except FileNotFoundError:
        movies = []
        return movies

def save_movies(movies):
    with open(os.path.join(data_dir, "movies.pickle"), "wb") as file:
        pickle.dump(movies, file)

def load_guests():
    try:
        with open(os.path.join(data_dir, "guests.pickle"), "rb") as file:
            try:
                guests = pickle.load(file)
            except EOFError:
                guests = []
        return guests
    except FileNotFoundError:
        guests = []
        return guests
    
def save_guests(guests):
    with open(os.path.join(data_dir, "guests.pickle"), "wb") as file:
        pickle.dump(guests, file)

def load_schedule():
    try:
        with open(os.path.join(data_dir, "schedule.pickle"), "rb") as file:
            try:
                schedule = pickle.load(file)
            except EOFError:
                schedule = []
        return schedule
    except FileNotFoundError:
        schedule = []
        return schedule

def save_schedule(schedule):
    with open(os.path.join(data_dir, "schedule.pickle"), "wb") as file:
        pickle.dump(schedule, file)