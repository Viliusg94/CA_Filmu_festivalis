import os
import sys

# Absoliutus pathas iki admin_menu failo (nuo pat disko) __file__ nurodo kelią iki failo ir nuiima paskutinį lygį. 
#be os.path.dirname pathas gaunasi c:\..\..\Desktop\CA_Filmu_festivalis\models\functions.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# pasiima vienu lygiu aukščiau esančią direktoriją (jau gaunasi root)
project_root = os.path.dirname(current_dir)
# print(project_root)

# prideda pathą iki root direktorijos, kad būtų galima paprasčiau importuoti kitus failus
sys.path.append(project_root)

import modules.classes as cls
import services.data_handler as file
from datetime import datetime, timedelta
import services.movie_handler as mov

def add_movie_to_schedule():
    try:
        movie_list = file.load_movies()
    except FileNotFoundError:
        movie_list = []
    if movie_list == []:
        print("Filmų sąrašas tuščias")
        return

    mov.show_movie_list()

    results = mov.search_movies()
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
            # if f_screening_date < datetime.now().date():             #Del filmu vertinimo galimai reiks nuimt sita ifa
            #     print("Peržiūros data negali būti praeities data")   #antra eilute, kad geriau matytusi komentaras :D
                # continue
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
        #tikrinta tos pačios dienos filmus ir sukonvertuoja į datetime objektus palyginimui
        if movie.screening_date == f_screening_date:
            existing_time = datetime.combine(f_screening_date, movie.screening_time) #nauja data + ezistuojančio seanso laikas
            new_time = datetime.combine(f_screening_date, f_screening_time) #nauja data + editintas laikas
            movie_duration = timedelta(minutes=movie_to_schedule.length)
            #tikrinama ar nesidubliuoja laikai
            if (existing_time <= new_time < existing_time + timedelta(minutes=movie.movie.length) or new_time <= existing_time < new_time + movie_duration):
                print(f"Peržiūros laikas sutampa su filmu: {movie.movie.name}")
                return

    screening_list.append(screening_entry)
    file.save_schedule(screening_list)
    print("Filmas sėkmingai įtrauktas į tvarkaraštį")


############################################################################################################################################################################
def show_schedule():
    try:
        screening_list = file.load_schedule()
    except FileNotFoundError:
        screening_list = []
    if screening_list == []:
        print("Tvarkaraštis tuščias")
        return
    

    
    current_date = None
    for i, entry in enumerate(screening_list, 1):
        if entry.screening_date != current_date:
            current_date = entry.screening_date
            print(f"\n{entry.screening_date.strftime('%Y-%m-%d')}:")
        
        end_time = (datetime.combine(entry.screening_date, entry.screening_time) + timedelta(minutes=entry.movie.length)).time()
        
        print(f"[{i}] Seansas: {entry.screening_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {entry.movie.name} ({entry.movie.length} min) Laisvų vietų {entry.available_seats}/{entry.total_seats}")
############################################################################################################################################################################
def edit_schedule():
    try:
        screening_list = file.load_schedule()
    except FileNotFoundError:
        screening_list = []
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

    action_choice = input("Pasirinkite veiksmą:\n[1] - Redaguoti seansą\n[2] - Pašalinti seansą\n")

    if action_choice == "1":#Atnaujinti
        edit = input("Ką norite pakeisti?\n[1] - Datą\n[2] - Laiką\n[3] - Rodomą filmą\n")

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
                        # Tikrina ar tai ne tas pats seansas kurį koreguojame IR ar ta pati data
                        if movie != entry_to_edit and movie.screening_date == f_edit_date:
                            existing_time = datetime.combine(f_edit_date, movie.screening_time) #Dabartinis seanso laikas
                            new_time = datetime.combine(f_edit_date,entry_to_edit.screening_time) #Naujas seanso laikas
                            movie_duration = timedelta(minutes=entry_to_edit.movie.length) # Filmo trukmė
                        #Tikrina ar seansų laikas nesidubliuoja
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
                        if movie != entry_to_edit and movie.screening_date == entry_to_edit.screening_date: #ar ne tas pats seansas kurį redaguojam ir ar seansas vyksta tą pačią dieną
                            existing_time = datetime.combine(entry_to_edit.screening_date, movie.screening_time) #Dabartinis seanso laikas
                            new_datetime = datetime.combine(entry_to_edit.screening_date, f_edit_time) #Naujas seanso laikas
                            movie_duration = timedelta(minutes=entry_to_edit.movie.length) #Filmo trukmė
                            #   senas laikas       naujas laikas    senas laikas + trukmė                                 naujas laikas     senas laikas    naujas laikas + trukmė
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
            mov.show_movie_list()
            results = mov.search_movies()
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
############################################################################################################################################################################
def reserve_seats(guest_name):
    try:
        scheduled_movies = file.load_schedule()
    except FileNotFoundError:
        scheduled_movies = []
    if scheduled_movies == []:
        print("Tvarkaraštis tuščias")
        return

    show_schedule()

    while True:
        try:
            choice = int(input("Pasirinkite seanso numerį: "))
            if 1 <= choice <= len(scheduled_movies):
                selected_screening = scheduled_movies[choice -1]

                # if selected_screening.screening_date < datetime.now().date():
                #     print("Seansas jau praėjo. Į šį seansą rezervuotis vietų nebegalima")
                #     continue

                if selected_screening.available_seats <= 0:
                    print("Atsiprašome, šiam seansui nebeliko laisvų vietų, pasirinkite kitą seansą")
                    continue 
               
                try:
                    guests = file.load_guests()
                except FileNotFoundError:
                    guests = []
                reservation_exists = False
                for guest in guests:
                    if guest.name.lower() == guest_name.lower():
                        for reservation in guest.reservations:
                            if reservation["Seanso data"] == selected_screening.screening_date and reservation ["Seanso laikas"] == selected_screening.screening_time:
                                print("Vieta šiam seansui jau rezervuota")
                                reservation_exists = True
                                break

                        if reservation_exists == False:
                            reservation = {
                                "Filmo pavadinimas":selected_screening.movie.name,
                                "Seanso data":selected_screening.screening_date,
                                "Seanso laikas":selected_screening.screening_time
                            }
                            guest.reservations.append(reservation)
                            selected_screening.available_seats -=1
    
                            file.save_schedule(scheduled_movies)
                            file.save_guests(guests)
                            print("Rezervacija sekminga!")

                        return
                break
            else:
                print("Pasirinkite seanso numerį iš sąrašo")
        except ValueError:
            print("Neteisinga įvestis, įveskite skaičių")

    

############################################################################################################################################################################
def show_reservations(guest_name):
    try:
        guests = file.load_guests()
    except FileNotFoundError:
        guests = []
    current_guest = None
    for guest in guests:
        if guest.name.lower() == guest_name.lower():
            current_guest = guest
            break

    if current_guest.reservations == []:
        print("Šiuo metu neturite rezervacijų")
        return
    
    print("Jūsų rezervacijos: ")
    for i, reservation in enumerate(current_guest.reservations, 1):
        print(f"[{i}] Rezervacija:{reservation['Filmo pavadinimas']} {reservation['Seanso data']} {reservation ['Seanso laikas'].strftime('%H:%M')}")

############################################################################################################################################################################
def cancel_reservation(guest_name):
    try:
        guests = file.load_guests()
    except FileNotFoundError:
        guests = []

    current_guest = None
    for guest in guests:
        if guest.name.lower() == guest_name.lower():
            current_guest = guest
            break

    if current_guest.reservations == None:
        print("Neturite aktyvių rezervacijų")

    show_reservations(guest_name)

    while True:
        try:
            choice = int(input("Įveskite norimos atšaukti rezervacijos numerį\n"))
            if 1 <= choice <= len(current_guest.reservations):
                selected_reservation = current_guest.reservations[choice -1]
                break
            else:
                print("Pasirinkite rezervacijos numerį iš rezervacijų sąrašo")
        except ValueError:
            print("Neteisinga įvestis, įveskite skaičių")

    try:
        screening_list = file.load_schedule()
    except FileNotFoundError:
        screening_list = []

    for movie in screening_list:
        if movie.movie.name == selected_reservation["Filmo pavadinimas"] and movie.screening_date == selected_reservation["Seanso data"] and movie.screening_time == selected_reservation["Seanso laikas"]:
            movie.available_seats +=1
            break
    
    current_guest.reservations.remove(selected_reservation)

    file.save_schedule(screening_list)
    file.save_guests(guests)

    print("Rezervacija sekmingai atšaukta")
    