import sys
import os

# Absoliutus pathas iki admin_menu failo (nuo pat disko) __file__ nurodo kelią iki failo ir nuiima paskutinį lygį. 
#be os.path.dirname pathas gaunasi c:\..\..\Desktop\CA_Filmu_festivalis\views\user_interface.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# pasiima vienu lygiu aukščiau esančią direktoriją (jau gaunasi root)
project_root = os.path.dirname(current_dir)
# print(project_root)

# prideda pathą iki root direktorijos, kad būtų galima paprasčiau importuoti kitus failus
sys.path.append(project_root)

from colorama import Fore,Back,Style
import services.schedule_handler as schedule
import services.movie_handler as mov
import models.Functions as fun


def client_menu(logged_in_guest):
    while True:
        print(Fore.MAGENTA + "Žiūrovo meniu:" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "[1] - Rodyti repertuarą\n[2] - Filmo paieška\n[3] - Bilietų rezervacija\n[4] - Rezervacijų peržiūra\n[5] - Rezervacijos atšaukimas\n[6] - Filmų reitingavimas\n[7] - Mano įverinimai\n[Q] - Uždaryti programą\n" + Style.RESET_ALL)
        if choice == "1":
            schedule.show_schedule()
        elif choice == "2":
            mov.search_movies()
        elif choice == "3":
            schedule.reserve_seats(logged_in_guest)
        elif choice == "4":
            schedule.show_reservations(logged_in_guest)
        elif choice == "5":
            schedule.cancel_reservation(logged_in_guest)
        elif choice == "6":
            mov.rate_movie(logged_in_guest)
        elif choice == "7":
            mov.show_guest_ratings(logged_in_guest)
        elif choice.lower() == "q":
            fun.end_program()
        else:
            print(Back.RED + "Neteisingas meniu pasirinkimas" + Style.RESET_ALL)
