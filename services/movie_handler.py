import sys
import os
############################################################################################################################################################################
# Absoliutus pathas iki admin_menu failo (nuo pat disko) __file__ nurodo kelią iki failo ir nuiima paskutinį lygį. 
#be os.path.dirname pathas gaunasi c:\..\..\Desktop\CA_Filmu_festivalis\services\movie_handler.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# pasiima vienu lygiu aukščiau esančią direktoriją (jau gaunasi root)
project_root = os.path.dirname(current_dir)
# print(project_root)

# prideda pathą iki root direktorijos, kad būtų galima paprasčiau importuoti kitus failus
sys.path.append(project_root)

import modules.classes as cls
import services.data_handler as file
from datetime import datetime


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
        genre = input("Filmo žanras: ")
        director = input("Režisierius: ")

        while True:
            release_year = (input("Išleidimo metai YYYY: "))
            check_year = len(release_year)
            if check_year == 4:
                try:
                    year = int(release_year)        
                    if year >= 1888 and year < datetime.now().year: #pirmas sukurtas filmas išleistas 1888 metais
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
                age_rating = int(input("Rekomenduojamas amžius: "))
                break
            except ValueError:
                print("Neteisinga įvestis, įveskite amžiaus reitingą skaičiais.")
    
        
        if "dok" in genre.lower() or "doc" in genre.lower():
            subject = input("Įveskite dokumentikos temą: ")
            movie = cls.Documentarie(name,length,genre,director,release_year,age_rating,subject)
        elif "ani" in genre.lower():
            region = input("Įveskite regioną: ")
            movie = cls.Amimated_movie(name,length,genre,director,release_year,age_rating,region)
        else:
            movie = cls.Movie(name,length,genre,director,release_year,age_rating)

        try:
            movies = file.load_movies()
        except FileNotFoundError:
            movies = []    

        if isinstance(movies, list):
            movies.append(movie)
        else:
            movies = [movie] #Jei failas neužsikrovė, pridedamas movie objektas į movies listą

        file.save_movies(movies)


        check = True
        while check:
            option = input("Ar norite tęsti Taip/Ne? ")
            if option.lower() == "taip":
                add = True
                break
            elif option.lower() == "ne":
                add = False                
                break
            else:
                print("Ar norite tęsti? Taip/Ne")

############################################################################################################################################################################
def remove_movie():
        remove = True
        while remove:
            try:
                movie_list = file.load_movies()
            except FileNotFoundError:
                movie_list = []
            if movie_list == []:
                print("Filmų sąrašas tuščias")
                remove = False
                break

            search_text = input("Įveskite norimo pašalinti filmo pavadinimą: ").lower()
            found_movies = []

            for movie in movie_list:
                if search_text in movie.name.lower():
                    found_movies.append(movie)

            if found_movies == []:
                print(f"Nerastas nei vienas filmas tokiu pavadinimu: {search_text}")
                break

            elif len(found_movies) == 1:
                movie_list.remove(found_movies[0])
                file.save_movies(movie_list)
                print(f"Filmas '{found_movies[0].name}' sėkmingai pašalintas iš sąrašo")
                return
            
            if len(found_movies) > 1:
                print(f"Rastas ne vienas filmas tokiu pat pavadinimu: {search_text}.\n Pasirinkit filmą kurį norite pašalinti:")
                for i, movie in enumerate(found_movies):
                    print(f"[{i+1}] {repr(movie)}")
                while True:
                    try:
                        choice = int(input("Pasirinkite norimo ištrinti filmo numerį: "))
                        if 1 <= choice <= len(found_movies):
                            movie_to_remove = found_movies[choice - 1]
                            break
                        else:
                            print("Neteisingai pasirinktas filmas, pasirinkite filmo numerį iš sąrašo.")
                    except ValueError:
                        print("Neteisinga įvestis.")

            movie_list.remove(movie_to_remove)
            file.save_movies(movie_list)

            print("Filmas sėkmingai pašalintas iš sąrašo")
            
            ##Testavimui
            # check = True
            # while check:
            #     option = input("Ar norite tęsti Taip/Ne? ")
            #     if option.lower() == "taip":
            #         remove = True
            #         break
            #     elif option.lower() == "ne":
            #         remove = False                
            #         break
            # else:
            #     print("Ar norite tęsti? Taip/Ne")

            
############################################################################################################################################################################
def update_movie():
    try:
        movie_list = file.load_movies()
    except FileNotFoundError:
        movie_list = []
    if movie_list == []:
        print("Filmų sąrašas tuščias")
        return 

    show_movie_list()
    results = search_movies()
    if results == []:
        print("Nerastas nei vienas filmas pagal paieškos kriterijus")
        return

    if len(results) > 1:
        print("Yra daugiau nei vienas filmas tokiu pavadinimu. pasirinkite, kurį filmą norite atnaujinti")
        for i, movie in enumerate(results):
            print(f"[{i+1}] {repr(movie)}")

        while True:
            try:
                choice = int(input("Įveskite filmo numerį, kurį norite atnaujinti: "))
                if 1 <= choice <= len(results):
                    movie_to_update = results[choice - 1]
                    break
                else:
                    print("Neteisingas pasirinkimas. Įveskite filmo numerį iš sąrašo.")
            except ValueError:
                print("Neteisinga įvestis, įveskite skaičių")
    else:
        movie_to_update = results[0]                    

    print("Pasirinktas filmas:")
    print(repr(movie_to_update))


    # Pakeičiama seno objekto reikšmė nauju objektu prieš keičiant atributą
    for i, movie in enumerate(movie_list):
            if (movie.name == movie_to_update.name and 
                movie.length == movie_to_update.length and 
                movie.genre == movie_to_update.genre and 
                movie.director == movie_to_update.director and 
                movie.release_year == movie_to_update.release_year and 
                movie.age_rating == movie_to_update.age_rating):
               
                movie_list[i] = movie_to_update
                break

    while True:
        attribute = input("Kurią informaciją norite atnaujinti?\nPavadinimas - [1]\nTrukmė - [2]\nŽanras - [3]\nRežisierius - [4]\nIšleidimo metai - [5]\nAmžiaus cenzas - [6]\n")
        
        if attribute == "1":
            new_value = input("Įveskite naują pavadinimą: ")
            movie_to_update.name = new_value
            break
        elif attribute == "2":
            while True:
                try:
                    new_value = int(input("Įveskite filmo trukmę (minutėmis): "))
                    movie_to_update.length = new_value
                    break
                except ValueError:
                    print("Neteisinga įvestis. Įveskite skaičių.")
            break
        elif attribute == "3":
            new_value = input("Įveskite filmo žanrą: ")
            movie_to_update.genre = new_value
            break
        elif attribute == "4":
            new_value = input("Įveskite filmo režisierių: ")
            movie_to_update.director = new_value
            break
        elif attribute == "5":
            while True:
                try:
                    new_value = int(input("Įveskite filmo išleidimo metus: "))
                    movie_to_update.release_year = new_value
                    break
                except ValueError:
                    print("Neteisinga įvestis. Įveskite skaičių.")
            break
        elif attribute == "6":
            while True:
                try:
                    new_value = int(input("Įveskite naują amžiaus cenzą: "))
                    movie_to_update.age_rating = new_value
                    break
                except ValueError:
                    print("Neteisinga įvestis. Įveskite skaičių.")
            break
        else:
            print("Neteisingas pasirinkimas, pasirinkite atributą iš sąrašo")
            continue
   
    file.save_movies(movie_list)
    print("Filmo informacija atnaujinta")
    print(repr(movie_to_update))
############################################################################################################################################################################
def show_movie_list():
    try:
        movie_list = file.load_movies()
    except FileExistsError:
        movie_list = []
    if movie_list:
        for i,movie in enumerate(movie_list,1):
            print(f"[{i}] {repr(movie)}") 

############################################################################################################################################################################        
def search_movies():
    try:
        movie_list = file.load_movies()
    except FileNotFoundError:
        movie_list = []
    if movie_list == []:
        print("Filmų sąrašas tuščias")
        return movie_list
        
    
    criteria = input("Paieškos kriterijus:\n[1] - Pavadinimas\n[2] - Žanras\n[3] - Režisierius\n[4] - Išleidimo metai\n[5] - Amžiaus cenzas\n")
    search_text = input("Paieškos tekstas: ").lower()

    results = []
    for movie in movie_list:
        if criteria == "1":
            if search_text in movie.name.lower():
                results.append(movie)
        elif criteria == "2":
            if search_text in movie.genre.lower():
                results.append(movie)
        elif criteria == "3":
            if search_text in movie.director.lower():
                results.append(movie)
        elif criteria == "4":
            try:
                if int(search_text) == movie.release_year:
                    results.append(movie)
            except ValueError:
                print("Neteisinga įvestis. Išleidimo metai turi būti skaičius.")
        elif criteria == "5":
            try:
                if int(search_text) == movie.age_rating:
                    results.append(movie)
            except ValueError:
                print("Neteisinga įvestis. Amžiaus cenzas turi būti skaičius.")
        else:
            print("Neteisingai pasirinktas paieškos kriterijus")

    if results != []:
        print("Paieškos rezultatai:")
        for movie in results:
            print(repr(movie))
    else:
        print("Pagal pateiktus paieškos kriterijus filmų nėra")                         

    return results

############################################################################################################################################################################
def rate_movie(guest_name):
    print("Įvertinkite filmą")

    try:
        movies = file.load_movies()
    except FileNotFoundError:
        movies = []
    try:
        guests = file.load_guests()
    except FileNotFoundError:
        guests = []

    current_guest = None
    for guest in guests:
        if guest.name.lower() == guest_name.lower():
            current_guest = guest
            break

    seen_movies = []

    for reservation in current_guest.reservations:
        movie_name = reservation["Filmo pavadinimas"]
        screening_date = reservation["Seanso data"]

        if screening_date < datetime.now().date():
            for movie in movies:
                if movie.name == movie_name and movie not in seen_movies:
                    seen_movies.append(movie)

    if seen_movies == []:
        print("Neturite peržiūrėtų filmų, kuriuos galėtumėte vertinti")
        return

    print("Jūsų peržiūrėti filmai:")
    for i, movie in enumerate (seen_movies,1):
        current_score = None
        for score in movie.score_list:
            if score["Vardas"].lower() == guest_name.lower():
                current_score = (f"{score['Balas']}/10")
        print(f"[{i}] {movie.name} (Jūsų įvertinimas: {current_score})")    

    while True:
        try:
            choice = int(input("Pasirinkite vertinamo filmo numerį\n"))
            if 1 <= choice <= len(seen_movies):
                selected_movie = seen_movies[choice -1]
                break
            else:
                print("Pasirinkite filmą iš sąrašo\n")
        except ValueError:
            print("Neteisinga įvestis, įveskite skaičių\n")

    while True:
        try:
            score = int(input("Įvertinkite filmą nuo 1 iki 10\n"))
            if 1 <= score <= 10:
                break
            else:
                print("Įvertinimas turi būti tarp 1 ir 10\n")
        except ValueError:
            print("Netinkama įvestis, įvertinimas privalo būti skaičius\n")

    selected_movie.add_score(guest_name, score)

    file.save_movies(movies)
    print(f"{selected_movie.name} įvertinote {score}")
############################################################################################################################################################################
def show_guest_ratings(guest_name):
    try:
        movies_list = file.load_movies()
        if not isinstance(movies_list,list):
            movies_list = [movies_list]
    except FileNotFoundError:
        movies_list = []

    rated_movies = []

    for movie in movies_list:
        for score in movie.score_list:
            if score["Vardas"].lower() == guest_name.lower():
                rated_movies.append({
                    "Filmo pavadinimas":movie.name,
                    "Balas":score["Balas"],
                    "Vidurkis":movie.average_score
                })

    if rated_movies == []:
        print("Jūs dar neįvertinote nei vieno filmo")
        return
    
    print("Jūsų įvertinti filmai: ")
    for i, movie in enumerate(rated_movies,1):
        print(f"[{i}] {movie['Filmo pavadinimas']} Jūsų įvertinimas: {movie['Balas']} Filmo įvertinimų vidurkis: {movie['Vidurkis']:.1f}/10")