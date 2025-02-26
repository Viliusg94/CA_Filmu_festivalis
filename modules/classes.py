class Movie:
    def __init__(self, name, length, genre, director, release_year, age_rating):
        self.name = name
        self.length = length
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.age_rating = age_rating
        self.score_list = []
        self.average_score = 0.0
    
    def add_score(self, guest_name, score):
    
        for s in self.score_list:
            if s["Vardas"] == guest_name:
                s["Balas"] = score
                break
        else: 
            self.score_list.append({"Vardas": guest_name, "Balas": score})
        
        if self.score_list:
            self.average_score = sum(s["Balas"] for s in self.score_list) / len(self.score_list)
            

    def __repr__(self):
        return (f"Filmas - Pavadinimas:{self.name}, Trukmė: {self.length} min, Žanras:{self.genre}, Režisierius:{self.director}, Išleidimo metai:{self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}")

class Documentarie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, subject):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.subject = subject

    def __repr__(self):
        return (f"Dokumentinis filmas - Pavadinimas: {self.name}, Trukmė - {self.length} min, Žanras: {self.genre}, Režisierius: {self.director}, Išleidimo metai: {self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}, Tema: {self.subject}")

class Amimated_movie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, region):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.region = region

    def __repr__(self):
        return (f"Animacinis filmas - Pavadinimas: {self.name}, Trukmė - {self.length} min, Žanras: {self.genre}, Režisierius: {self.director}, Išleidimo metai: {self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}, Regijonas: {self.region}")

class Schedule:
    def __init__(self, movie, screening_date, screening_time, seats=10):
        self.movie = movie
        self.screening_date = screening_date
        self.screening_time = screening_time
        self.total_seats = seats
        self.available_seats = seats
        self.reservations = []
    
    def __repr__(self):
        return (f"Filmų tvarkaraštis:\n{self.movie.name}, Data - {self.screening_date}, Laikas - {self.screening_time}, Laisvos vietos {self.available_seats}")

class Admin:
        pass

class Guest:
    def __init__(self, name):
        self.name = name
        self.reservations = []

    def __repr__(self):
        return (f"Žiūrovas: {self.name}")
