#čia bus cli jei gerai seksis ir gui
import pickle
import services.data_handler as files

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
                break
            else:
                print ("Neteisingas vartotojo vardas arba slaptažodis, bandykite dar kartą")
            admin_menu()
            files.load_movies()          
    elif choice == "2":
        guests = files.load_guests()
        while True:
            print("Įveskite prisijungimo duomenis: ")
            guest_user = input("Įveskite vartotojo vardą: ")
            if guest_user in guests:
                break
            else:
                print("Toks vartotojas neegzistuoja")
        client_menu()
    elif choice.upper() == "Q":
        print("Viso gero!")
        exit()    
    else:
        print("Neteisinga įvestis, pasirinkite savo rolę: Organizatorius - 1 arba Svečias - 2")                    

def main_menu():
    print("Sveiki atvykę į Code Academy 2025 Filmų festivalį!")
    authentication()

def admin_menu():
    choice = input("Pridėti filmą - [1]\n Pašalinti filmą - [2]\n Atnaujinti filmo informaciją - [3]\nRodyti repertuarą - [4]\nIeškoti filmo - [5]\nSeansai - [6]\nUždaryti programą - [Q]:")
    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    if choice == "6":
        pass
    if choice.upper() == "Q":
        print("Viso gero!")
        exit()

def client_menu():
    choice = input("Rodyti repertuarą - [1]\nFilmo paieška - [2]\nBilietų rezervacija - [3]\nFilmų reitingavimas - [4]")
    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice.upper() == "Q":
        print("Viso gero!")
        exit()





        