
class Movie:
    def __init__(self, name, length, genre, director, release_year, age_rating):
        self.name = name
        self.length = length
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.age_rating = age_rating
        pass

class Documentarie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, subject):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.subject = subject


class Amimated_movie(Movie):
    def __init__(self, name, length, genre, director, release_year, age_rating, region):
        super().__init__(name, length, genre, director, release_year, age_rating)
        self.region = region

# Reikalavimai:
#     • Galimybė pridėti naują filmą į festivalio programą.
#     • Kiekvienas filmas turi turėti šiuos atributus (gali turėti ir daugiau):
#         ◦ Pavadinimas
#         ◦ Trukmė (minutėmis)
#         ◦ Žanras (drama, komedija ir t.t.)
#         ◦ Režisierius
#         ◦ Išleidimo metai
#         ◦ Amžiaus reitingas (pvz., "N-13", "N-18")