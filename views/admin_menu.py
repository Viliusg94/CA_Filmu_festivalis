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

from colorama import Fore, Back, Style
import services.movie_handler as mov
import services.schedule_handler as schedule
import models.Functions as fun 

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