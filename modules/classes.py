
class Movie:
    def __init__(self, name, length, genre, director, release_year, age_rating):
        self.name = name
        self.length = length
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.age_rating = age_rating

    def __repr__(self):
        return f"Filmas - Pavadinimas:{self.name}, Trukmė: {self.length} min, Žanras:{self.genre}, Režisierius:{self.director}, Išleidimo metai:{self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}"

class Documentarie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, subject):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.subject = subject

    def __repr__(self):
        return f"Animacinis filmas - Pavadinimas: {self.name}, Trukmė - {self.length} min, Žanras: {self.genre}, Režisierius: {self.director}, Išleidimo metai: {self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}, Tema: {self.subject}"

class Amimated_movie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, region):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.region = region

    def __repr__(self):
        return f"Animacinis filmas - Pavadinimas: {self.name}, Trukmė - {self.length} min, Žanras: {self.genre}, Režisierius: {self.director}, Išleidimo metai: {self.release_year}, Rekomenduojamas amžiaus cenzas: N-{self.age_rating}, Regijonas: {self.region}"


class Admin:
    def __init__(self):
        pass

class Guest:
    def __init__(self):
        pass
