def dodawanie(ilość):
    wynik = 0
    for i in range (ilość):
        z = float(input("Podaj składnik: "))
        wynik = wynik + z
    print("Wynik to ", wynik)
    wybieranie_operacji()

def mnożenie(ilość):
    wynik = 1
    for i in range (ilość):
        z = float(input("Podaj czynnik: "))
        wynik = wynik * z
    print("Wynik to ", wynik)
    wybieranie_operacji()

def odejmowanie(ilość):
    wynik = float(input("Podaj odjemną: "))
    for i in range (ilość - 1):
        z = float(input("Podaj odjemnik: "))
        wynik = wynik - z
    print("Wynik to ", wynik)
    wybieranie_operacji()

def dzielenie(ilość):
    wynik = float(input("Podaj dzielną: "))
    for i in range (ilość - 1):
        z = float(input("Podaj dzielnik: "))
        wynik = wynik / z
    print("Wynik to ", wynik)
    wybieranie_operacji()

def wybieranie_operacji():
    operacja = input("Wybierz operację(dodawanie, odejmowanie, mnożenie lub dzielenie): ")
    if operacja == "dodawanie":
        dodawanie(int(input("Podaj ilość składników: ")))
    elif operacja == "mnożenie":
        mnożenie(int(input("Podaj ilość czynników: ")))
    elif operacja == "dzielenie":
        dzielenie(int(input("Podaj ilość dzielników: ")))
    elif operacja == "odejmowanie":
        odejmowanie(int(input("Podaj ilość odjemników: ")))
    else:
        print("Źle wpisano nazwę operacji lub taka operacja nie istnieje!\nSpróbuj jeszcze raz")
        wybieranie_operacji()


print("""                 ========================
                 ||Witaj w Kalkulatorze||
                 ========================\n""")
wybieranie_operacji()

input("Chcesz wyjść?")