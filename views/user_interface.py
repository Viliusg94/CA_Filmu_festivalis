#čia bus cli jei gerai seksis ir gui

def authentication():
    print("Organizatoriaus prisijungimas - [1] | Svečio prisijungimas - [2]:")
    choice = input("")
    if choice == "1":
        while True:
            print("Įveskite prisijungimo duomenis: ")
            user_name = input("Vartotojo vardas: ")
            user_password = input("Slaptažodis: ")
            if user_name.lower() == "admin" and user_password.lower() == "admin": 
                break
            else:
                print ("Neteisingas vartotojo vardas arba slaptažodis, bandykite dar kartą")
        admin_menu()                
    elif choice == "2":
        client_menu()
    else:
        print("Neteisinga įvestis, pasirinkite savo rolę: Organizatorius - 1 arba Svečias - 2")                    

def main_menu():
    print("Sveiki atvykę į Code Academy 2025 Filmų festivalį!")
    authentication()

def admin_menu():
    choice = input("Pridėti filmą - [1]\n Pašalinti filmą - [2]\n Atnaujinti filmo informaciją - [3]\nRodyti repertuarą - [4]\nIeškoti filmo - [5]\nSeansai - [6]:")
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
    pass

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