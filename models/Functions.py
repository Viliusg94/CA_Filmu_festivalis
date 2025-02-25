# Reikalavimai:
#     • Galimybė pridėti naują filmą į festivalio programą.
#     • Kiekvienas filmas turi turėti šiuos atributus (gali turėti ir daugiau):
#         ◦ Pavadinimas
#         ◦ Trukmė (minutėmis)
#         ◦ Žanras (drama, komedija ir t.t.)
#         ◦ Režisierius
#         ◦ Išleidimo metai
#         ◦ Amžiaus reitingas (pvz., "N-13", "N-18")

import sys
import os

# Absoliutus pathas iki admin_menu failo (nuo pat disko) __file__ nurodo kelią iki failo ir nuiima paskutinį lygį. 
#be os.path.dirname pathas gaunasi c:\..\..\Desktop\CA_Filmu_festivalis\models\admin_menu.py
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# pasiima vienu lygiu aukščiau esančią direktoriją (jau gaunasi root)
project_root = os.path.dirname(current_dir)
print(project_root)

# prideda pathą iki root direktorijos, kad būtų galima paprasčiau importuoti kitus failus
sys.path.append(project_root)

import modules.classes as cls
import services.data_handler as file
from datetime import datetime, timedelta


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
                    if year >= 1888 and year < datetime.datetime.now().year: #pirmas sukurtas filmas išleistas 1888 metais
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
    
        
        if "ani" in genre.lower(): #tikrina ar tai animacija/animacinis/anime
            region = input("Įveskite regioną: ")
            movie = cls.Amimated_movie(name,length,genre,director,release_year,age_rating,region)

        elif "dok" in genre.lower() or "doc" in genre.lower():
            subject = input("Įveskite dokumentikos temą: ")
            movie = cls.Documentarie(name,length,genre,director,release_year,age_rating,subject)
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


def remove_movie():
        remove = True
        while remove:
            movie_list = file.load_movies()
            if movie_list == []:
                print("Filmų sąrašas tuščias")
                remove = False
                break

            search_text = input("Įveskite norimo pašalinti filmo pavadinimą: ").lower()
            found_movies = []
            for movie in movie_list:
                if search_text in movie.name.lower():
                    found_movies.append(movie)

            if not found_movies:
                print(f"Nerastas nei vienas filmas tokiu pavadinimu: {search_text}")
                break

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

            check = True
            while check:
                option = input("Ar norite tęsti Taip/Ne? ")
                if option.lower() == "taip":
                    remove = True
                    break
                elif option.lower() == "ne":
                    remove = False                
                    break
            else:
                print("Ar norite tęsti? Taip/Ne")

            

def update_movie():
    movie_list = file.load_movies()
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
    # index = movie_list.index(movie_to_update)
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
    # movie_list[index] = movie_to_update
    file.save_movies(movie_list)
    print("Filmo informacija atnaujinta")
    print(repr(movie_to_update))

def show_movie_list():
    movie_list = file.load_movies()
    if movie_list:
        for movie in movie_list:
            print(repr(movie)) 

        
def search_movies():
    movie_list = file.load_movies()
    if movie_list == []:
        print("Filmų sąrašas tuščias")
        return movie_list
        
    
    criteria = input("Pagal ką ieškosite?\nPavadinimas - [1]\nŽanras - [2]\nRežisierius - [3]\nIšleidimo metai - [4]\nAmžiaus cenzas - [5]\n")
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

def add_movie_to_schedule():
    movie_list = file.load_movies()
    if movie_list == []:
        print("Filmų sąrašas tuščias")
        return

    show_movie_list()

    results = search_movies()
    if results == []:
        print ("Nerastas nei vienas filmas")
        return
    
    if len(results) > 1:
        print("Pasirinkite filmą kurį norite įtraukti į tvarkaraštį: ")
        for i, movie in enumerate(results):
            print(f"[{i+1}] {repr(movie)}")

        while True:
            try:
                choice = int(input("Įveskite filmo numerį: "))
                if 1 <= choice <= len(results):
                    movie_to_schedule = results[choice -1]
                    break
                else:
                    print("Pasirinkite filmo numerį iš sąrašo")
            except ValueError:
                print("Neteisinga įvestis, įveskite filmo numerį")
    else:
        movie_to_schedule = results[0]


    while True:
        try:
            screening_date = input("Įveskite datą formatu (YYYY-MM-DD): ")
            f_screening_date = datetime.strptime(screening_date, "%Y-%m-%d").date()
            if f_screening_date < datetime.now().date():
                print("Peržiūros data negali būti praeities data")
                continue
            break
        except ValueError:
            print("Neteisingas datos formatas, įveskite datą formatu YYYY-MM-DD")

    while True:
        try:
            screening_time = input("Įveskite laiką formatu (HH:MM): ")
            f_screening_time = datetime.strptime(screening_time, "%H:%M").time()
            break
        except ValueError:
            print("Neteisingas laiko formatas, įveskite laiką formatu HH:MM")

    screening_entry = cls.Schedule(movie_to_schedule, f_screening_date, f_screening_time)
    screening_list = file.load_schedule()

    for movie in screening_list:
        #tikrinta tos pačios dienos filmus ir sukonvertuoja į palyginamą formatą
        if movie.screening_date == f_screening_date:
            existing_time = datetime.combine(f_screening_date, movie.screening_time) #Senas laikas 
            new_time = datetime.combine(f_screening_date, f_screening_time) #editintas laikas
            movie_duration = timedelta(minutes=movie_to_schedule.length)
            #tikrinama ar nesidubliuoja laikai
            if (existing_time <= new_time < existing_time + timedelta(minutes=movie.movie.length) or new_time <= existing_time < new_time + movie_duration):
                print(f"Peržiūros laikas sutampa su filmu: {movie.movie.name}")
                return

    screening_list.append(screening_entry)
    file.save_schedule(screening_list)
    print("Filmas sėkmingai įtrauktas į tvarkaraštį")



def show_schedule():
    screening_list = file.load_schedule()
    if screening_list == []:
        print("Tvarkaraštis tuščias")
        return
    

    
    current_date = None
    for i, entry in enumerate(screening_list, 1):
        if entry.screening_date != current_date:
            current_date = entry.screening_date
            print(f"\n{entry.screening_date.strftime('%Y-%m-%d')}:")
        
        end_time = (datetime.combine(entry.screening_date, entry.screening_time) + timedelta(minutes=entry.movie.length)).time()
        
        print(f"[{i}] Seansas: {entry.screening_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {entry.movie.name} ({entry.movie.length} min)")

def edit_schedule():
    screening_list = file.load_schedule()
    if screening_list == []:
        print("Tvarkaraštis tuščias")
        return
    
    show_schedule()

    while True:
        try:
            choice = int(input("Įveskite redaguojamo seanso numerį: "))
            if 1 <= choice <= len(screening_list):
                entry_to_edit = screening_list[choice -1]
                break
            else:
                print("Neteisingai parinktas seanso numeris, pasirinkite seanso numerį iš sąrašo")
        except ValueError:
            print("Neteisinga įvestis, pasirinkite skaičių iš pateikto sąrašo")

    action_choice = input("Pasirinkite veiksmą:\nRedaguoti seansą - [1]\nPašalinti seansą - [2]\n")

    if action_choice == "1":#Atnaujinti
        edit = input("Ką norite pakeisti?\nDatą - [1]\nLaiką - [2]\nRodomą filmą - [3]\n")

        if edit == "1": #data
            while True:
                try:
                    edit_date = input("Įveskite naują datą (YYYY-MM-DD): ")
                    f_edit_date = datetime.strptime(edit_date, "%Y-%m-%d").date()
                    if f_edit_date < datetime.now().date():
                        print("Seansas negali būti pakeistas į praeities datą")
                        continue

                    overlap = False
                    for movie in screening_list: 
                        if movie != entry_to_edit and movie.screening_date == f_edit_date:
                            existing_time = datetime.combine(f_edit_date, movie.screening_time) #senas laikas
                            new_time = datetime.combine(f_edit_date,entry_to_edit.screening_time) #data į kurią keičiama 
                            movie_duration = timedelta(minutes=entry_to_edit.movie.length) # Filmo trukmė

                            if (existing_time <= f_edit_date < existing_time + timedelta(minutes=movie.movie.length) or new_time <= existing_time < new_time + movie_duration):
                                print (f"Šitu laiku jau rodomas filmas {movie.movie.name}")
                                overlap = True
                                break

                    if overlap == False:
                        entry_to_edit.screening_date = f_edit_date
                        print("Seanso data sėkmingai atnaujinta")
                        break
                except ValueError:
                    print("Neteisingas datos formatas, įveskite datą formatu (YYYY-MM-DD)")                

        elif edit == "2": #laikas
            while True:
                try:
                    edit_time = input("Įveskite seanso laiką (HH:MM): ")
                    f_edit_time = datetime.strptime(edit_time, "%H:%M").time()

                    overlap = False
                    for movie in screening_list:
                        if movie != entry_to_edit and movie.screening_date == entry_to_edit.screening_date:
                            existing_time = datetime.combine(entry_to_edit.screening_date, movie.screening_time)
                            new_datetime = datetime.combine(entry_to_edit.screening_date, f_edit_time)
                            movie_duration = timedelta(minutes=entry_to_edit.movie.length)

                            if (existing_time <= new_datetime < existing_time + timedelta(minutes=movie.movie.length) or new_datetime <= existing_time < new_datetime + movie_duration):
                                print(f"Šiuo laiku jau rodomas filmas {movie.movie.name}")
                                overlap = True
                                break
                    
                    if overlap == False:
                        entry_to_edit.screening_time = f_edit_time
                        print("Seanso laikas sėkmingai atnaujintas")
                        break
                except ValueError:
                    print("Neteisingas laiko formatas, įveskite laiką formatu (HH:MM)")

        elif edit == "3": #filmas
            show_movie_list()
            results = search_movies()
            if results != []:
                if len(results) > 1:
                    for i, movie in enumerate(results,1):
                        print(f"[{i}] {repr(movie)}")

                    while True:
                        try:
                            movie_choice = int(input("Pasirinkite filmą iš sąrašo: "))
                            if 1 <= movie_choice <= len(results):
                                entry_to_edit.movie = results[movie_choice -1]
                                print(f"{results[movie_choice]} sėkmingai pakeistas į {entry_to_edit.movie}")
                                break
                        except ValueError:
                            print("Neteisinga įvestis, įveskite skaičių")
                else:
                    entry_to_edit = results[0]
            else:
                print("Nerasta filmų pagal paieškos kriterijus")
                return
    
    elif action_choice == "2": #Trinti
        screening_list.remove(entry_to_edit)
        print("Seansas sėkimingai pašalintas")

    else:
        print("Netinkama įvestis, rinkitės iš funkcijų sąrašo")

    file.save_schedule(screening_list)
    return

def end_program():
    print("Viso gero!")
    exit()


def reserve_tickets():
    pass

def rate_movie():
    pass

# add_movie()
# show_movie_list()
# update_movie()
# remove_movie()
# add_movie_to_schedule()
# show_schedule()
# edit_schedule()