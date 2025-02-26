import sys
import os
############################################################################################################################################################################
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

# ###########################################################################################################################################################################
# def add_movie():
#     add = True
#     while add:
#         name = input("Įveskite filmo pavadinimą: ")
#         try:
#             while True:
#                 length = int(input("Įveskite filmo trukmę (minutės): "))
#                 break
#         except ValueError:
#             print("Neteisinga įvestis, įveskite filmo trukmę (minutėmis)")
#         genre = input("Filmo žanras: ")
#         director = input("Režisierius: ")

#         while True:
#             release_year = (input("Išleidimo metai YYYY: "))
#             check_year = len(release_year)
#             if check_year == 4:
#                 try:
#                     year = int(release_year)        
#                     if year >= 1888 and year < datetime.now().year: #pirmas sukurtas filmas išleistas 1888 metais
#                         release_year = year
#                         break
#                     else:
#                         print("Nekorektiškai įvesti filmo išleidimo metai")
#                 except ValueError:
#                     print("Nekorektiškai įvesti duomenys. Išleidimo metai privalo būti sveikas skaičius (YYYY)")        
#             else:
#                 print("Nekorektiškai įvesti filmo išleidimo metai")

#         while True:
#             try:
#                 age_rating = int(input("Rekomenduojamas amžius: "))
#                 break
#             except ValueError:
#                 print("Neteisinga įvestis, įveskite amžiaus reitingą skaičiais.")
    
        
#         if "dok" in genre.lower() or "doc" in genre.lower():
#             subject = input("Įveskite dokumentikos temą: ")
#             movie = cls.Documentarie(name,length,genre,director,release_year,age_rating,subject)
#         elif "ani" in genre.lower():
#             region = input("Įveskite regioną: ")
#             movie = cls.Amimated_movie(name,length,genre,director,release_year,age_rating,region)
#         else:
#             movie = cls.Movie(name,length,genre,director,release_year,age_rating)

#         try:
#             movies = file.load_movies()
#         except FileNotFoundError:
#             movies = []    

#         if isinstance(movies, list):
#             movies.append(movie)
#         else:
#             movies = [movie] #Jei failas neužsikrovė, pridedamas movie objektas į movies listą

#         file.save_movies(movies)


#         check = True
#         while check:
#             option = input("Ar norite tęsti Taip/Ne? ")
#             if option.lower() == "taip":
#                 add = True
#                 break
#             elif option.lower() == "ne":
#                 add = False                
#                 break
#             else:
#                 print("Ar norite tęsti? Taip/Ne")

# ############################################################################################################################################################################
# def remove_movie():
#         remove = True
#         while remove:
#             try:
#                 movie_list = file.load_movies()
#             except FileNotFoundError:
#                 movie_list = []
#             if movie_list == []:
#                 print("Filmų sąrašas tuščias")
#                 remove = False
#                 break

#             search_text = input("Įveskite norimo pašalinti filmo pavadinimą: ").lower()
#             found_movies = []

#             for movie in movie_list:
#                 if search_text in movie.name.lower():
#                     found_movies.append(movie)

#             if found_movies == []:
#                 print(f"Nerastas nei vienas filmas tokiu pavadinimu: {search_text}")
#                 break

#             elif len(found_movies) == 1:
#                 movie_list.remove(found_movies[0])
#                 file.save_movies(movie_list)
#                 print(f"Filmas '{found_movies[0].name}' sėkmingai pašalintas iš sąrašo")
#                 return
            
#             if len(found_movies) > 1:
#                 print(f"Rastas ne vienas filmas tokiu pat pavadinimu: {search_text}.\n Pasirinkit filmą kurį norite pašalinti:")
#                 for i, movie in enumerate(found_movies):
#                     print(f"[{i+1}] {repr(movie)}")
#                 while True:
#                     try:
#                         choice = int(input("Pasirinkite norimo ištrinti filmo numerį: "))
#                         if 1 <= choice <= len(found_movies):
#                             movie_to_remove = found_movies[choice - 1]
#                             break
#                         else:
#                             print("Neteisingai pasirinktas filmas, pasirinkite filmo numerį iš sąrašo.")
#                     except ValueError:
#                         print("Neteisinga įvestis.")

#             movie_list.remove(movie_to_remove)
#             file.save_movies(movie_list)

#             print("Filmas sėkmingai pašalintas iš sąrašo")
            
#             ##Testavimui
#             # check = True
#             # while check:
#             #     option = input("Ar norite tęsti Taip/Ne? ")
#             #     if option.lower() == "taip":
#             #         remove = True
#             #         break
#             #     elif option.lower() == "ne":
#             #         remove = False                
#             #         break
#             # else:
#             #     print("Ar norite tęsti? Taip/Ne")

            
# ############################################################################################################################################################################
# def update_movie():
#     try:
#         movie_list = file.load_movies()
#     except FileNotFoundError:
#         movie_list = []
#     if movie_list == []:
#         print("Filmų sąrašas tuščias")
#         return 

#     show_movie_list()
#     results = search_movies()
#     if results == []:
#         print("Nerastas nei vienas filmas pagal paieškos kriterijus")
#         return

#     if len(results) > 1:
#         print("Yra daugiau nei vienas filmas tokiu pavadinimu. pasirinkite, kurį filmą norite atnaujinti")
#         for i, movie in enumerate(results):
#             print(f"[{i+1}] {repr(movie)}")

#         while True:
#             try:
#                 choice = int(input("Įveskite filmo numerį, kurį norite atnaujinti: "))
#                 if 1 <= choice <= len(results):
#                     movie_to_update = results[choice - 1]
#                     break
#                 else:
#                     print("Neteisingas pasirinkimas. Įveskite filmo numerį iš sąrašo.")
#             except ValueError:
#                 print("Neteisinga įvestis, įveskite skaičių")
#     else:
#         movie_to_update = results[0]                    

#     print("Pasirinktas filmas:")
#     print(repr(movie_to_update))


#     # Pakeičiama seno objekto reikšmė nauju objektu prieš keičiant atributą
#     for i, movie in enumerate(movie_list):
#             if (movie.name == movie_to_update.name and 
#                 movie.length == movie_to_update.length and 
#                 movie.genre == movie_to_update.genre and 
#                 movie.director == movie_to_update.director and 
#                 movie.release_year == movie_to_update.release_year and 
#                 movie.age_rating == movie_to_update.age_rating):
               
#                 movie_list[i] = movie_to_update
#                 break

#     while True:
#         attribute = input("Kurią informaciją norite atnaujinti?\nPavadinimas - [1]\nTrukmė - [2]\nŽanras - [3]\nRežisierius - [4]\nIšleidimo metai - [5]\nAmžiaus cenzas - [6]\n")
        
#         if attribute == "1":
#             new_value = input("Įveskite naują pavadinimą: ")
#             movie_to_update.name = new_value
#             break
#         elif attribute == "2":
#             while True:
#                 try:
#                     new_value = int(input("Įveskite filmo trukmę (minutėmis): "))
#                     movie_to_update.length = new_value
#                     break
#                 except ValueError:
#                     print("Neteisinga įvestis. Įveskite skaičių.")
#             break
#         elif attribute == "3":
#             new_value = input("Įveskite filmo žanrą: ")
#             movie_to_update.genre = new_value
#             break
#         elif attribute == "4":
#             new_value = input("Įveskite filmo režisierių: ")
#             movie_to_update.director = new_value
#             break
#         elif attribute == "5":
#             while True:
#                 try:
#                     new_value = int(input("Įveskite filmo išleidimo metus: "))
#                     movie_to_update.release_year = new_value
#                     break
#                 except ValueError:
#                     print("Neteisinga įvestis. Įveskite skaičių.")
#             break
#         elif attribute == "6":
#             while True:
#                 try:
#                     new_value = int(input("Įveskite naują amžiaus cenzą: "))
#                     movie_to_update.age_rating = new_value
#                     break
#                 except ValueError:
#                     print("Neteisinga įvestis. Įveskite skaičių.")
#             break
#         else:
#             print("Neteisingas pasirinkimas, pasirinkite atributą iš sąrašo")
#             continue
   
#     file.save_movies(movie_list)
#     print("Filmo informacija atnaujinta")
#     print(repr(movie_to_update))
# ############################################################################################################################################################################
# def show_movie_list():
#     try:
#         movie_list = file.load_movies()
#     except FileExistsError:
#         movie_list = []
#     if movie_list:
#         for i,movie in enumerate(movie_list,1):
#             print(f"[{i}] {repr(movie)}") 

# ############################################################################################################################################################################        
# def search_movies():
#     try:
#         movie_list = file.load_movies()
#     except FileNotFoundError:
#         movie_list = []
#     if movie_list == []:
#         print("Filmų sąrašas tuščias")
#         return movie_list
        
    
#     criteria = input("Paieškos kriterijus:\n[1] - Pavadinimas\n[2] - Žanras\n[3] - Režisierius\n[4] - Išleidimo metai\n[5] - Amžiaus cenzas\n")
#     search_text = input("Paieškos tekstas: ").lower()

#     results = []
#     for movie in movie_list:
#         if criteria == "1":
#             if search_text in movie.name.lower():
#                 results.append(movie)
#         elif criteria == "2":
#             if search_text in movie.genre.lower():
#                 results.append(movie)
#         elif criteria == "3":
#             if search_text in movie.director.lower():
#                 results.append(movie)
#         elif criteria == "4":
#             try:
#                 if int(search_text) == movie.release_year:
#                     results.append(movie)
#             except ValueError:
#                 print("Neteisinga įvestis. Išleidimo metai turi būti skaičius.")
#         elif criteria == "5":
#             try:
#                 if int(search_text) == movie.age_rating:
#                     results.append(movie)
#             except ValueError:
#                 print("Neteisinga įvestis. Amžiaus cenzas turi būti skaičius.")
#         else:
#             print("Neteisingai pasirinktas paieškos kriterijus")

#     if results != []:
#         print("Paieškos rezultatai:")
#         for movie in results:
#             print(repr(movie))
#     else:
#         print("Pagal pateiktus paieškos kriterijus filmų nėra")                         

#     return results
# ###########################################################################################################################################################################
# def add_movie_to_schedule():
#     try:
#         movie_list = file.load_movies()
#     except FileNotFoundError:
#         movie_list = []
#     if movie_list == []:
#         print("Filmų sąrašas tuščias")
#         return

#     show_movie_list()

#     results = search_movies()
#     if results == []:
#         print ("Nerastas nei vienas filmas")
#         return
    
#     if len(results) > 1:
#         print("Pasirinkite filmą kurį norite įtraukti į tvarkaraštį: ")
#         for i, movie in enumerate(results):
#             print(f"[{i+1}] {repr(movie)}")

#         while True:
#             try:
#                 choice = int(input("Įveskite filmo numerį: "))
#                 if 1 <= choice <= len(results):
#                     movie_to_schedule = results[choice -1]
#                     break
#                 else:
#                     print("Pasirinkite filmo numerį iš sąrašo")
#             except ValueError:
#                 print("Neteisinga įvestis, įveskite filmo numerį")
#     else:
#         movie_to_schedule = results[0]


#     while True:
#         try:
#             screening_date = input("Įveskite datą formatu (YYYY-MM-DD): ")
#             f_screening_date = datetime.strptime(screening_date, "%Y-%m-%d").date()
#             # if f_screening_date < datetime.now().date():             #Del filmu vertinimo galimai reiks nuimt sita ifa
#             #     print("Peržiūros data negali būti praeities data")   #antra eilute, kad geriau matytusi komentaras :D
#                 # continue
#             break
#         except ValueError:
#             print("Neteisingas datos formatas, įveskite datą formatu YYYY-MM-DD")

#     while True:
#         try:
#             screening_time = input("Įveskite laiką formatu (HH:MM): ")
#             f_screening_time = datetime.strptime(screening_time, "%H:%M").time()
#             break
#         except ValueError:
#             print("Neteisingas laiko formatas, įveskite laiką formatu HH:MM")

#     screening_entry = cls.Schedule(movie_to_schedule, f_screening_date, f_screening_time)
#     screening_list = file.load_schedule()

#     for movie in screening_list:
#         #tikrinta tos pačios dienos filmus ir sukonvertuoja į datetime objektus palyginimui
#         if movie.screening_date == f_screening_date:
#             existing_time = datetime.combine(f_screening_date, movie.screening_time) #nauja data + ezistuojančio seanso laikas
#             new_time = datetime.combine(f_screening_date, f_screening_time) #nauja data + editintas laikas
#             movie_duration = timedelta(minutes=movie_to_schedule.length)
#             #tikrinama ar nesidubliuoja laikai
#             if (existing_time <= new_time < existing_time + timedelta(minutes=movie.movie.length) or new_time <= existing_time < new_time + movie_duration):
#                 print(f"Peržiūros laikas sutampa su filmu: {movie.movie.name}")
#                 return

#     screening_list.append(screening_entry)
#     file.save_schedule(screening_list)
#     print("Filmas sėkmingai įtrauktas į tvarkaraštį")


# ############################################################################################################################################################################
# def show_schedule():
#     try:
#         screening_list = file.load_schedule()
#     except FileNotFoundError:
#         screening_list = []
#     if screening_list == []:
#         print("Tvarkaraštis tuščias")
#         return
    

    
#     current_date = None
#     for i, entry in enumerate(screening_list, 1):
#         if entry.screening_date != current_date:
#             current_date = entry.screening_date
#             print(f"\n{entry.screening_date.strftime('%Y-%m-%d')}:")
        
#         end_time = (datetime.combine(entry.screening_date, entry.screening_time) + timedelta(minutes=entry.movie.length)).time()
        
#         print(f"[{i}] Seansas: {entry.screening_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {entry.movie.name} ({entry.movie.length} min) Laisvų vietų {entry.available_seats}/{entry.total_seats}")
# ############################################################################################################################################################################
# def edit_schedule():
#     try:
#         screening_list = file.load_schedule()
#     except FileNotFoundError:
#         screening_list = []
#     if screening_list == []:
#         print("Tvarkaraštis tuščias")
#         return
    
#     show_schedule()

#     while True:
#         try:
#             choice = int(input("Įveskite redaguojamo seanso numerį: "))
#             if 1 <= choice <= len(screening_list):
#                 entry_to_edit = screening_list[choice -1]
#                 break
#             else:
#                 print("Neteisingai parinktas seanso numeris, pasirinkite seanso numerį iš sąrašo")
#         except ValueError:
#             print("Neteisinga įvestis, pasirinkite skaičių iš pateikto sąrašo")

#     action_choice = input("Pasirinkite veiksmą:\n[1] - Redaguoti seansą\n[2] - Pašalinti seansą\n")

#     if action_choice == "1":#Atnaujinti
#         edit = input("Ką norite pakeisti?\n[1] - Datą\n[2] - Laiką\n[3] - Rodomą filmą\n")

#         if edit == "1": #data
#             while True:
#                 try:
#                     edit_date = input("Įveskite naują datą (YYYY-MM-DD): ")
#                     f_edit_date = datetime.strptime(edit_date, "%Y-%m-%d").date()
#                     if f_edit_date < datetime.now().date():
#                         print("Seansas negali būti pakeistas į praeities datą")
#                         continue

#                     overlap = False
#                     for movie in screening_list: 
#                         # 2. Tikrina ar tai ne tas pats seansas kurį koreguojame IR ar ta pati data
#                         if movie != entry_to_edit and movie.screening_date == f_edit_date:
#                             existing_time = datetime.combine(f_edit_date, movie.screening_time) #Dabartinis seanso laikas
#                             new_time = datetime.combine(f_edit_date,entry_to_edit.screening_time) #Naujas seanso laikas
#                             movie_duration = timedelta(minutes=entry_to_edit.movie.length) # Filmo trukmė
#                         #Tikrina ar seansų laikas nesidubliuoja
#                             if (existing_time <= f_edit_date < existing_time + timedelta(minutes=movie.movie.length) or new_time <= existing_time < new_time + movie_duration):
#                                 print (f"Šitu laiku jau rodomas filmas {movie.movie.name}")
#                                 overlap = True
#                                 break

#                     if overlap == False:
#                         entry_to_edit.screening_date = f_edit_date
#                         print("Seanso data sėkmingai atnaujinta")
#                         break
#                 except ValueError:
#                     print("Neteisingas datos formatas, įveskite datą formatu (YYYY-MM-DD)")                

#         elif edit == "2": #laikas
#             while True:
#                 try:
#                     edit_time = input("Įveskite seanso laiką (HH:MM): ")
#                     f_edit_time = datetime.strptime(edit_time, "%H:%M").time()

#                     overlap = False
#                     for movie in screening_list:
#                         if movie != entry_to_edit and movie.screening_date == entry_to_edit.screening_date: #ar ne tas pats seansas kurį redaguojam ir ar seansas vyksta tą pačią dieną
#                             existing_time = datetime.combine(entry_to_edit.screening_date, movie.screening_time) #Dabartinis seanso laikas
#                             new_datetime = datetime.combine(entry_to_edit.screening_date, f_edit_time) #Naujas seanso laikas
#                             movie_duration = timedelta(minutes=entry_to_edit.movie.length) #Filmo trukmė
#                             #   senas laikas       naujas laikas    senas laikas + trukmė                                 naujas laikas     senas laikas    naujas laikas + trukmė
#                             if (existing_time <= new_datetime < existing_time + timedelta(minutes=movie.movie.length) or new_datetime <= existing_time < new_datetime + movie_duration):
#                                 print(f"Šiuo laiku jau rodomas filmas {movie.movie.name}")
#                                 overlap = True
#                                 break
                    
#                     if overlap == False:
#                         entry_to_edit.screening_time = f_edit_time
#                         print("Seanso laikas sėkmingai atnaujintas")
#                         break
#                 except ValueError:
#                     print("Neteisingas laiko formatas, įveskite laiką formatu (HH:MM)")

#         elif edit == "3": #filmas
#             show_movie_list()
#             results = search_movies()
#             if results != []:
#                 if len(results) > 1:
#                     for i, movie in enumerate(results,1):
#                         print(f"[{i}] {repr(movie)}")

#                     while True:
#                         try:
#                             movie_choice = int(input("Pasirinkite filmą iš sąrašo: "))
#                             if 1 <= movie_choice <= len(results):
#                                 entry_to_edit.movie = results[movie_choice -1]
#                                 print(f"{results[movie_choice]} sėkmingai pakeistas į {entry_to_edit.movie}")
#                                 break
#                         except ValueError:
#                             print("Neteisinga įvestis, įveskite skaičių")
#                 else:
#                     entry_to_edit = results[0]
#             else:
#                 print("Nerasta filmų pagal paieškos kriterijus")
#                 return
    
#     elif action_choice == "2": #Trinti
#         screening_list.remove(entry_to_edit)
#         print("Seansas sėkimingai pašalintas")

#     else:
#         print("Netinkama įvestis, rinkitės iš funkcijų sąrašo")

#     file.save_schedule(screening_list)
#     return
# ############################################################################################################################################################################
# def reserve_seats(guest_name):
#     try:
#         scheduled_movies = file.load_schedule()
#     except FileNotFoundError:
#         scheduled_movies = []
#     if scheduled_movies == []:
#         print("Tvarkaraštis tuščias")
#         return

#     show_schedule()

#     while True:
#         try:
#             choice = int(input("Pasirinkite seanso numerį: "))
#             if 1 <= choice <= len(scheduled_movies):
#                 selected_screening = scheduled_movies[choice -1]

#                 # if selected_screening.screening_date < datetime.now().date():
#                 #     print("Seansas jau praėjo. Į šį seansą rezervuotis vietų nebegalima")
#                 #     continue

#                 if selected_screening.available_seats <= 0:
#                     print("Atsiprašome, šiam seansui nebeliko laisvų vietų, pasirinkite kitą seansą")
#                     continue 
               
#                 try:
#                     guests = file.load_guests()
#                 except FileNotFoundError:
#                     guests = []
#                 reservation_exists = False
#                 for guest in guests:
#                     if guest.name.lower() == guest_name.lower():
#                         for reservation in guest.reservations:
#                             if reservation["Seanso data"] == selected_screening.screening_date and reservation ["Seanso laikas"] == selected_screening.screening_time:
#                                 print("Vieta šiam seansui jau rezervuota")
#                                 reservation_exists = True
#                                 break

#                         if reservation_exists == False:
#                             reservation = {
#                                 "Filmo pavadinimas":selected_screening.movie.name,
#                                 "Seanso data":selected_screening.screening_date,
#                                 "Seanso laikas":selected_screening.screening_time
#                             }
#                             guest.reservations.append(reservation)
#                             selected_screening.available_seats -=1
    
#                             file.save_schedule(scheduled_movies)
#                             file.save_guests(guests)
#                             print("Rezervacija sekminga!")

#                         return
#                 break
#             else:
#                 print("Pasirinkite seanso numerį iš sąrašo")
#         except ValueError:
#             print("Neteisinga įvestis, įveskite skaičių")

    

# ############################################################################################################################################################################
# def show_reservations(guest_name):
#     try:
#         guests = file.load_guests()
#     except FileNotFoundError:
#         guests = []
#     current_guest = None
#     for guest in guests:
#         if guest.name.lower() == guest_name.lower():
#             current_guest = guest
#             break

#     if current_guest.reservations == []:
#         print("Šiuo metu neturite rezervacijų")
#         return
    
#     print("Jūsų rezervacijos: ")
#     for i, reservation in enumerate(current_guest.reservations, 1):
#         print(f"[{i}] Rezervacija:{reservation['Filmo pavadinimas']} {reservation['Seanso data']} {reservation ['Seanso laikas'].strftime('%H:%M')}")

# ############################################################################################################################################################################
# def cancel_reservation(guest_name):
#     try:
#         guests = file.load_guests()
#     except FileNotFoundError:
#         guests = []

#     current_guest = None
#     for guest in guests:
#         if guest.name.lower() == guest_name.lower():
#             current_guest = guest
#             break

#     if current_guest.reservations == None:
#         print("Neturite aktyvių rezervacijų")

#     show_reservations(guest_name)

#     while True:
#         try:
#             choice = int(input("Įveskite norimos atšaukti rezervacijos numerį\n"))
#             if 1 <= choice <= len(current_guest.reservations):
#                 selected_reservation = current_guest.reservations[choice -1]
#                 break
#             else:
#                 print("Pasirinkite rezervacijos numerį iš rezervacijų sąrašo")
#         except ValueError:
#             print("Neteisinga įvestis, įveskite skaičių")

#     try:
#         screening_list = file.load_schedule()
#     except FileNotFoundError:
#         screening_list = []

#     for movie in screening_list:
#         if movie.movie.name == selected_reservation["Filmo pavadinimas"] and movie.screening_date == selected_reservation["Seanso data"] and movie.screening_time == selected_reservation["Seanso laikas"]:
#             movie.available_seats +=1
#             break
    
#     current_guest.reservations.remove(selected_reservation)

#     file.save_schedule(screening_list)
#     file.save_guests(guests)

#     print("Rezervacija sekmingai atšaukta")
    
# ###########################################################################################################################################################################
# def rate_movie(guest_name):
#     print("Įvertinkite filmą")

#     try:
#         movies = file.load_movies()
#     except FileNotFoundError:
#         movies = []
#     try:
#         guests = file.load_guests()
#     except FileNotFoundError:
#         guests = []

#     current_guest = None
#     for guest in guests:
#         if guest.name.lower() == guest_name.lower():
#             current_guest = guest
#             break

#     seen_movies = []

#     for reservation in current_guest.reservations:
#         movie_name = reservation["Filmo pavadinimas"]
#         screening_date = reservation["Seanso data"]

#         if screening_date < datetime.now().date():
#             for movie in movies:
#                 if movie.name == movie_name and movie not in seen_movies:
#                     seen_movies.append(movie)

#     if seen_movies == []:
#         print("Neturite peržiūrėtų filmų, kuriuos galėtumėte vertinti")
#         return

#     print("Jūsų peržiūrėti filmai:")
#     for i, movie in enumerate (seen_movies,1):
#         current_score = None
#         for score in movie.score_list:
#             if score["Vardas"].lower() == guest_name.lower():
#                 current_score = (f"{score['Balas']}/10")
#         print(f"[{i}] {movie.name} (Jūsų įvertinimas: {current_score})")    

#     while True:
#         try:
#             choice = int(input("Pasirinkite vertinamo filmo numerį\n"))
#             if 1 <= choice <= len(seen_movies):
#                 selected_movie = seen_movies[choice -1]
#                 break
#             else:
#                 print("Pasirinkite filmą iš sąrašo\n")
#         except ValueError:
#             print("Neteisinga įvestis, įveskite skaičių\n")

#     while True:
#         try:
#             score = int(input("Įvertinkite filmą nuo 1 iki 10\n"))
#             if 1 <= score <= 10:
#                 break
#             else:
#                 print("Įvertinimas turi būti tarp 1 ir 10\n")
#         except ValueError:
#             print("Netinkama įvestis, įvertinimas privalo būti skaičius\n")

#     selected_movie.add_score(guest_name, score)

#     file.save_movies(movies)
#     print(f"{selected_movie.name} įvertinote {score}")
# ############################################################################################################################################################################
# def show_guest_ratings(guest_name):
    # try:
    #     movies_list = file.load_movies()
    #     if not isinstance(movies_list,list):
    #         movies_list = [movies_list]
    # except FileNotFoundError:
    #     movies_list = []

    # rated_movies = []

    # for movie in movies_list:
    #     for score in movie.score_list:
    #         if score["Vardas"].lower() == guest_name.lower():
    #             rated_movies.append({
    #                 "Filmo pavadinimas":movie.name,
    #                 "Balas":score["Balas"],
    #                 "Vidurkis":movie.average_score
    #             })

    # if rated_movies == []:
    #     print("Jūs dar neįvertinote nei vieno filmo")
    #     return
    
    # print("Jūsų įvertinti filmai: ")
    # for i, movie in enumerate(rated_movies,1):
    #     print(f"[{i}] {movie['Filmo pavadinimas']} Jūsų įvertinimas: {movie['Balas']} Filmo įvertinimų vidurkis: {movie['Vidurkis']:.1f}/10")

############################################################################################################################################################################
def guest_registration():
    print("Žiūrovų registracija")
    try:
        guests = file.load_guests()
    except FileNotFoundError:
        guests = []

    while True:
        guest_name = input("Įveskite savo vardą: ").strip()
        if guest_name == "":
            print("Vardas negali būti tuščias, įveskite savo vardą")
            continue

        for guest in guests:
            if guest_name.lower() == guest.name.lower():
                print("Toks žiūrovas jau užregistruotas")
                break
        else:
            new_guest = cls.Guest(guest_name)
            guests.append(new_guest)
            file.save_guests(guests)
            print(f"Žiūrovas {guest_name} užregistruotas į festivalį!")
            break
############################################################################################################################################################################
def guest_login():
    try:
        guests = file.load_guests()
    except FileNotFoundError:
        guests = []

    if guests == []:
        print("Neužregistruotas nei vienas žiūrovas")
        return None

    while True:        
        guest_name = input("Įveskite savo vardą: ").strip()
        if guest_name == "":
            print("Vardas negali būti tuščias")
            continue

        guest_exists = False
        for guest in guests: 
            if guest_name.lower() == guest.name.lower():
                guest_exists = True
                break

        if guest_exists:
            print(f"Sveiki, {str(guest_name).title()}!")
            return (guest_name)
        else: 
            print(f"Žiūrovas {guest_name} nėra registruotas, prašome užsiregistruoti")
            return None
############################################################################################################################################################################
def end_program():
    print("Viso gero!")
    exit()





# add_movie()
# show_movie_list()
# update_movie()
# remove_movie()
# add_movie_to_schedule()
# show_schedule()
# edit_schedule()
# guest_registration() 
