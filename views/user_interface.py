#čia bus cli jei gerai seksis ir gui
import pickle


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

import services.data_handler as files
import models.Functions as fun
def authentication():
    print("Organizatoriaus prisijungimas - [1] | Svečio prisijungimas - [2] | Uždaryti programą - [Q]:")
    choice = input("")

    if choice == "1":
        while True:
            print("Įveskite prisijungimo duomenis: ")
            user_name = input("Vartotojo vardas: ")
            user_password = input("Slaptažodis: ")
            if user_name.lower() == "admin" and user_password.lower() == "admin": 
                print("Prisijungimas sėkmingas!")
                admin_menu()  
                try:
                    files.load_movies()
                except FileNotFoundError:
                    print("Error: Movie data file not found.")
                break
            else:
                print ("Neteisingas vartotojo vardas arba slaptažodis, bandykite dar kartą")
                   
    elif choice == "2":
        try:
            guests = files.load_guests()
        except FileNotFoundError:
            print("Klaida: Failas nerastas.")
            return #išeina iš autentikacijos
        while True:
            print("Įveskite prisijungimo duomenis: ")
            guest_user = input("Įveskite vartotojo vardą: ")
            if guest_user in guests:
                break
            else:
                print("Toks vartotojas neegzistuoja")
        client_menu()
    elif choice.lower() == "q":
        print("Viso gero!")
        exit()    
    else:
        print("Neteisinga įvestis, pasirinkite savo rolę: Organizatorius - 1 arba Svečias - 2")                    

def main_menu():
    print("Sveiki atvykę į Code Academy 2025 Filmų festivalį!")
    authentication()

def admin_menu():
    choice = input("Rodyti filmų sąrašą - [1]\nPridėti filmą - [2]\n Pašalinti filmą - [3]\n Atnaujinti filmo informaciją - [4]\nPridėti filmą į repertuarą - [5]\nRodyti repertuarą - [6]\nIeškoti filmo - [7]\n Koreguoti repertuarą - [8]\nUždaryti programą - [Q]:")
    if choice == "1":
        fun.show_movie_list()
    elif choice == "2":
        fun.add_movie() 
    elif choice == "3":
        fun.remove_movie()
    elif choice == "4":
        fun.update_movie()
    elif choice == "5":
        fun.add_movie_to_schedule
    elif choice == "6":
        fun.show_schedule()
    elif choice == "7":
        fun.search_movies()
    elif choice == "8":
        fun.edit_schedule()
    elif choice.lower() == "q":
        fun.end_program()
    else:
        print("Neteisingas meniu pasirinkimas")    

def client_menu():
    choice = input("Rodyti repertuarą - [1]\nFilmo paieška - [2]\nBilietų rezervacija - [3]\nFilmų reitingavimas - [4]")
    if choice == "1":
        fun.show_schedule()
    elif choice == "2":
        fun.search_movies()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice.lower() == "q":
        fun.end_program()
    else:
        print("Neteisingas meniu pasirinkimas")




        