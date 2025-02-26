#čia bus cli jei gerai seksis ir gui

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

import services.schedule_handler as schedule
import services.movie_handler as mov
import models.functions as fun
from colorama import Fore, Back, Style
def authentication():
    choice = input(Fore.GREEN + "[1] - Organizatoriaus prisijungimas\n[2] - Žiūrovo prisijungimas\n[3] - Žiūrovo registracija\n[Q] - Uždaryti programą\n" + Style.RESET_ALL)

    if choice == "1":
        while True:
            print(Fore.MAGENTA + "Įveskite prisijungimo duomenis: " + Style.RESET_ALL)
            user_name = input("Vartotojo vardas: ").strip()
            user_password = input("Slaptažodis: ").strip()
            if user_name.lower() == "admin" and user_password.lower() == "admin": 
                print(Fore.YELLOW + "Prisijungimas sėkmingas!" + Style.RESET_ALL)
                admin_menu()  
            else:
                print (Back.RED + "Neteisingas vartotojo vardas arba slaptažodis, bandykite dar kartą" + Style.RESET_ALL)
                   
    elif choice == "2":
        logged_in_guest = fun.guest_login()
        if logged_in_guest is not None:
           client_menu(logged_in_guest)
        else:
           authentication()
           
    elif choice == "3":
        fun.guest_registration()
        authentication()
    elif choice.lower() == "q":
        fun.end_program() 
    else:
        print(Back.RED + "Neteisinga įvestis, pasirinkite opciją iš meniu 1-3" + Style.RESET_ALL)                    

def main_menu():
    print(Fore.MAGENTA + "Sveiki atvykę į Code Academy 2025 Filmų festivalį!" + Style.RESET_ALL)
    authentication()

def admin_menu():
    while True:
        print(Fore.MAGENTA + "Organizatoriaus meniu" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "[1] - Rodyti filmų sąrašą\n[2] - Pridėti filmą\n[3] - Pašalinti filmą\n[4] - Atnaujinti filmo informaciją\n[5] - Pridėti filmą į repertuarą\n[6] - Rodyti repertuarą\n[7] - Ieškoti filmo\n[8] - Koreguoti repertuarą\n[Q] Uždaryti programą\n" + Style.RESET_ALL)
        if choice == "1":
            mov.show_movie_list()
            admin_menu()
        elif choice == "2":
            mov.add_movie()
            admin_menu() 
        elif choice == "3":
            mov.remove_movie()
            admin_menu()
        elif choice == "4":
            mov.update_movie()
            admin_menu()
        elif choice == "5":
            schedule.add_movie_to_schedule()
            admin_menu()
        elif choice == "6":
            schedule.show_schedule()
            admin_menu()
        elif choice == "7":
            mov.search_movies()
            admin_menu()
        elif choice == "8":
            schedule.edit_schedule()
            admin_menu()
        elif choice.lower() == "q":
            fun.end_program()
        else:
            print(Back.RED + "Neteisingas meniu pasirinkimas" + Style.RESET_ALL)    

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
