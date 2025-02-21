# Reikalavimai:
#     • Galimybė pridėti naują filmą į festivalio programą.
#     • Kiekvienas filmas turi turėti šiuos atributus (gali turėti ir daugiau):
#         ◦ Pavadinimas
#         ◦ Trukmė (minutėmis)
#         ◦ Žanras (drama, komedija ir t.t.)
#         ◦ Režisierius
#         ◦ Išleidimo metai
#         ◦ Amžiaus reitingas (pvz., "N-13", "N-18")



import modules.classes as mov
import services.data_handler as file
import datetime

def add_movie():
    add = True
    while add:
        name = input("Įveskite filmo pavadinimą: ")
        try:
            while True:
                length = int(input("Įveskite filmo trukmę (minutės): "))
                break
        except ValueError:
            print("Neteisinga įvestis, įveskite filmo trukmę (minutėmis)")
        genre = input("Filmo žanras:")
        director = input("Režisierius: ")

        while True:
            release_year = (input("Išleidimo metai YYYY: "))
            check_year = len(release_year)
            if check_year == 4:
                try:
                    year = int(release_year)        
                    if year >= 1888 and year < datetime.datetime.now().year:
                        release_year = year
                        break
                    else:
                        print("Nekorektiškai įvesti filmo išleidimo metai")
                except ValueError:
                    print("Nekorektiškai įvesti duomenys. Išleidimo metai privalo būti sveikas skaičius (YYYY)")        
            else:
                print("Nekorektiškai įvesti filmo išleidimo metai")

        while True:
            try:
                age_rating = int(input("Filmas rekomenduojamas nuo (?) metų: "))
                break
            except ValueError:
                print("Neteisinga įvestis, įveskite amžiaus reitingą skaičiais.")
    
        
        if "ani" in genre.lower(): #tikrina ar tai animacija/animacinis/anime
            region = input("Įveskite regioną: ")
            movie = mov.Amimated_movie(name,length,genre,director,release_year,age_rating,region)
            file.save_movies(movie)

        elif "dok" in genre.lower() or "doc" in genre.lower():
            subject = input("Įveskite dokumentikos temą: ")
            movie = mov.Documentarie(name,length,genre,director,release_year,age_rating,subject)
            file.save_movies(movie)
        else:
            movie = mov.Movie(name,length,genre,director,release_year,age_rating)
            file.save_movies(movie)

        check = True
        while check:
            option = input("Ar norite tęsti Taip/Ne? ")
            if option.lower() == "taip":
                add = True
                break
            elif option.lower() == "ne":
                add = False
                file.save_movies(movie)
            else:
                print("Ar norite tęsti? Taip/Ne")


def remove_movie():
    pass

def update_movie():
    pass

def show_movie_list():
    pass

def search_movies():
    pass

def show_schedule():
    pass

def exit():
    pass

add_movie()