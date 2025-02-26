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

import services.data_handler as file
from datetime import datetime
from colorama import Fore, Back, Style
import modules.Movies as mov
import services.data_handler as file

def add_movie():
    add = True
    while add:
        name = input(Fore.GREEN + "Įveskite filmo pavadinimą\n[Q] - grįžti\n" + Style.RESET_ALL)
        if name.lower() == "q":
            return
        try:
            while True:
                length = int(input(Fore.GREEN + "Įveskite filmo trukmę (minutės): " + Style.RESET_ALL))
                break
        except ValueError:
            print(Back.RED + "Neteisinga įvestis, įveskite filmo trukmę (minutėmis)" + Style.RESET_ALL)
        genre = input(Fore.GREEN + "Filmo žanras: " + Style.RESET_ALL)
        director = input(Fore.GREEN + "Režisierius: " + Style.RESET_ALL)

        while True:
            release_year = (input(Fore.GREEN + "Išleidimo metai YYYY: " + Style.RESET_ALL))
            check_year = len(release_year)
            if check_year == 4:
                try:
                    year = int(release_year)        
                    if year >= 1888 and year < datetime.now().year: #pirmas sukurtas filmas išleistas 1888 metais
                        release_year = year
                        break
                    else:
                        print(Back.YELLOW + "Nekorektiškai įvesti filmo išleidimo metai" + Style.RESET_ALL)
                except ValueError:
                    print(Back.YELLOW + "Nekorektiškai įvesti duomenys. Išleidimo metai privalo būti sveikas skaičius (YYYY)" + Style.RESET_ALL)        
            else:
                print(Back.RED + "Nekorektiškai įvesti filmo išleidimo metai" + Style.RESET_ALL)

        while True:
            try:
                age_rating = int(input(Fore.GREEN + "Rekomenduojamas amžius: " + Style.RESET_ALL))
                break
            except ValueError:
                print("Neteisinga įvestis, įveskite amžiaus reitingą skaičiais.")
    
        
        if "dok" in genre.lower() or "doc" in genre.lower():
            subject = input(Fore.GREEN + "Įveskite dokumentikos temą: " + Style.RESET_ALL)
            movie = mov.Documentarie(name,length,genre,director,release_year,age_rating,subject)
        elif "ani" in genre.lower():
            region = input(Fore.GREEN + "Įveskite regioną: " + Style.RESET_ALL)
            movie = mov.Amimated_movie(name,length,genre,director,release_year,age_rating,region)
        else:
            movie = mov.Movie(name,length,genre,director,release_year,age_rating)

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
            option = input(Fore.YELLOW + "Ar norite tęsti Taip/Ne? " + Style.RESET_ALL)
            if option.lower() == "taip":
                add = True
                break
            elif option.lower() == "ne":
                add = False                
                break
            else:
                print(Fore.YELLOW + "Ar norite tęsti? Taip/Ne" + Style.RESET_ALL)

############################################################################################################################################################################
def remove_movie():
        remove = True
        while remove:
            try:
                movie_list = file.load_movies()
            except FileNotFoundError:
                movie_list = []
            if movie_list == []:
                print(Back.RED + "Filmų sąrašas tuščias" + Style.RESET_ALL)
                remove = False
                break
            show_movie_list()
            search_text = input(Fore.GREEN + "Įveskite norimo pašalinti filmo pavadinimą:\n[Q] - Grįžti\n " + Style.RESET_ALL).lower()
            if search_text.lower() == "q":
                return
            found_movies = []

            for movie in movie_list:
                if search_text in movie.name.lower():
                    found_movies.append(movie)

            if found_movies == []:
                print(Fore.YELLOW + f"Nerastas nei vienas filmas tokiu pavadinimu: {search_text}" + Style.RESET_ALL)
                break

            elif len(found_movies) == 1:
                movie_list.remove(found_movies[0])
                file.save_movies(movie_list)
                print(Fore.CYAN + f"Filmas '{found_movies[0].name}' sėkmingai pašalintas iš sąrašo" + Style.RESET_ALL)
                return
            
            if len(found_movies) > 1:
                print(Fore.YELLOW + f"Rastas ne vienas filmas tokiu pat pavadinimu: {search_text}.\n Pasirinkit filmą kurį norite pašalinti:" + Style.RESET_ALL)
                for i, movie in enumerate(found_movies):
                    print(f"[{i+1}] {repr(movie)}")
                while True:
                    try:
                        choice = int(input(Fore.GREEN + "Pasirinkite norimo ištrinti filmo numerį: " + Style.RESET_ALL))
                        if 1 <= choice <= len(found_movies):
                            movie_to_remove = found_movies[choice - 1]
                            break
                        else:
                            print(Fore.YELLOW + "Neteisingai pasirinktas filmas, pasirinkite filmo numerį iš sąrašo." + Style.RESET_ALL)
                    except ValueError:
                        print(Back.RED + "Neteisinga įvestis." + Style.RESET_ALL) 

            movie_list.remove(movie_to_remove)
            file.save_movies(movie_list)

            print(Fore.CYAN + "Filmas sėkmingai pašalintas iš sąrašo" + Style.RESET_ALL)
            
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
        print(Back.RED + "Filmų sąrašas tuščias" + Style.RESET_ALL)
        return 

    show_movie_list()
    results = search_movies()
    if results == []:
        print(Back.RED + "Nerastas nei vienas filmas pagal paieškos kriterijus" + Style.RESET_ALL)
        return

    if len(results) > 1:
        print(Fore.YELLOW + "Yra daugiau nei vienas filmas tokiu pavadinimu. pasirinkite, kurį filmą norite atnaujinti" + Style.RESET_ALL)
        for i, movie in enumerate(results):
            print(f"[{i+1}] {repr(movie)}")

        while True:
            try:
                choice = int(input(Fore.GREEN + "Įveskite filmo numerį, kurį norite atnaujinti: " + Style.RESET_ALL))
                if 1 <= choice <= len(results):
                    movie_to_update = results[choice - 1]
                    break
                else:
                    print(Fore.YELLOW + "Neteisingas pasirinkimas. Įveskite filmo numerį iš sąrašo." + Style.RESET_ALL)
            except ValueError:
                print(Back.RED + "Neteisinga įvestis, įveskite skaičių" + Style.RESET_ALL)
    else:
        movie_to_update = results[0]                    

    print(Fore.MAGENTA + "Pasirinktas filmas:" + Style.RESET_ALL)
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
        attribute = input(Fore.GREEN + "Kurią informaciją norite atnaujinti?\nPavadinimas - [1]\nTrukmė - [2]\nŽanras - [3]\nRežisierius - [4]\nIšleidimo metai - [5]\nAmžiaus cenzas - [6]\n[Q] - Grįžti\n" + Style.RESET_ALL)
        if attribute.lower() == "q":
                return
        if attribute == "1":
            new_value = input(Fore.GREEN + "Įveskite naują pavadinimą: " + Style.RESET_ALL)
            movie_to_update.name = new_value
            break
        elif attribute == "2":
            while True:
                try:
                    new_value = int(input(Fore.GREEN + "Įveskite filmo trukmę (minutėmis): "+ Style.RESET_ALL))
                    movie_to_update.length = new_value
                    break
                except ValueError:
                    print(Back.RED + "Neteisinga įvestis. Įveskite skaičių."+ Style.RESET_ALL)
            break
        elif attribute == "3":
            new_value = input(Fore.GREEN + "Įveskite filmo žanrą: "+ Style.RESET_ALL)
            movie_to_update.genre = new_value
            break
        elif attribute == "4":
            new_value = input(Fore.GREEN + "Įveskite filmo režisierių: "+ Style.RESET_ALL)
            movie_to_update.director = new_value
            break
        elif attribute == "5":
            while True:
                try:
                    new_value = int(input(Fore.GREEN + "Įveskite filmo išleidimo metus: "+ Style.RESET_ALL))
                    movie_to_update.release_year = new_value
                    break
                except ValueError:
                    print(Back.RED + "Neteisinga įvestis. Įveskite skaičių."+ Style.RESET_ALL)
            break
        elif attribute == "6":
            while True:
                try:
                    new_value = int(input(Fore.GREEN + "Įveskite naują amžiaus cenzą: "+ Style.RESET_ALL))
                    movie_to_update.age_rating = new_value
                    break
                except ValueError:
                    print(Back.RED + "Neteisinga įvestis. Įveskite skaičių."+ Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + "Neteisingas pasirinkimas, pasirinkite atributą iš sąrašo"+ Style.RESET_ALL)
            continue
   
    file.save_movies(movie_list)
    print(Fore.CYAN + "Filmo informacija atnaujinta"+ Style.RESET_ALL)
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
        print(Back.RED + "Filmų sąrašas tuščias" + Style.RESET_ALL)
        return movie_list
        
    
    criteria = input(Fore.GREEN + "Paieškos kriterijus:\n[1] - Pavadinimas\n[2] - Žanras\n[3] - Režisierius\n[4] - Išleidimo metai\n[5] - Amžiaus cenzas\n[Q] - Grįžti\n" + Style.RESET_ALL)
    if criteria.lower() == "q":
        return
    search_text = input(Fore.YELLOW + "Paieškos tekstas: " + Style.RESET_ALL).lower()

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
                print(Fore.YELLOW + "Neteisinga įvestis. Išleidimo metai turi būti skaičius." + Style.RESET_ALL)  
        elif criteria == "5":
            try:
                if int(search_text) == movie.age_rating:
                    results.append(movie)
            except ValueError:
                print(Back.RED + "Neteisinga įvestis. Amžiaus cenzas turi būti skaičius." + Style.RESET_ALL) 
        else:
            print(Back.RED + "Neteisingai pasirinktas paieškos kriterijus" + + Style.RESET_ALL)

    if results != []:
        print(Fore.CYAN + "Paieškos rezultatai:" + Style.RESET_ALL)
        for movie in results:
            print(repr(movie))
    else:
        print(Fore.YELLOW + "Pagal pateiktus paieškos kriterijus filmų nėra" + Style.RESET_ALL)                         

    return results

############################################################################################################################################################################
def rate_movie(guest_name):
    print(Fore.MAGENTA + "Įvertinkite filmą" + Style.RESET_ALL)

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

        if screening_date < datetime.date():
            for movie in movies:
                if movie.name == movie_name and movie not in seen_movies:
                    seen_movies.append(movie)

    if seen_movies == []:
        print(Fore.YELLOW + "Neturite peržiūrėtų filmų, kuriuos galėtumėte vertinti" + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + "Jūsų peržiūrėti filmai:" + Style.RESET_ALL)
    for i, movie in enumerate (seen_movies,1):
        current_score = None
        for score in movie.score_list:
            if score["Vardas"].lower() == guest_name.lower():
                current_score = (f"{score['Balas']}/10")
        print(f"[{i}] {movie.name} (Jūsų įvertinimas: {current_score})")    

    while True:
        try:
            choice = int(input(Fore.GREEN + "Pasirinkite vertinamo filmo numerį\n" + Style.RESET_ALL))
            if 1 <= choice <= len(seen_movies):
                selected_movie = seen_movies[choice -1]
                break
            else:
                print(Fore.YELLOW + "Pasirinkite filmą iš sąrašo\n" + Style.RESET_ALL)
        except ValueError:
            print(Back.RED + "Neteisinga įvestis, įveskite skaičių\n" + Style.RESET_ALL)

    while True:
        try:
            score = int(input(Fore.GREEN + "Įvertinkite filmą nuo 1 iki 10\n" + Style.RESET_ALL))
            if 1 <= score <= 10:
                break
            else:
                print(Fore.YELLOW + "Įvertinimas turi būti tarp 1 ir 10\n" +Style.RESET_ALL)
        except ValueError:
            print(Back.RED + "Netinkama įvestis, įvertinimas privalo būti skaičius\n" + Style.RESET_ALL)

    selected_movie.add_score(guest_name, score)

    file.save_movies(movies)
    print(Fore.CYAN + f"{selected_movie.name} įvertinote {score}" + Style.RESET_ALL)
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
        print(Fore.YELLOW + "Jūs dar neįvertinote nei vieno filmo" + Style.RESET_ALL)
        return
    
    print(Fore.MAGENTA + "Jūsų įvertinti filmai: " + Style.RESET_ALL)
    for i, movie in enumerate(rated_movies,1):
        print(f"[{i}] {movie['Filmo pavadinimas']} Jūsų įvertinimas: {movie['Balas']} Filmo įvertinimų vidurkis: {movie['Vidurkis']:.1f}/10")