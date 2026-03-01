# alan 

# zmienna tekst = pobiera tekst wpisany przez użytkownika
# zmienna slowo = przechowuje słowo Alan
# jeśli slowo znajduje się w zmiennej tekst
#     wyświetl znaleziono
# w przeciwnym wypadku
#     wyświetl że nie ma takiego słowa

tekst = input("Napisz dowolny tekst: ")
slowo = "Alan"

if slowo in tekst:
    print("Znaleziono!")
else:
    print("Nie ma takego słowa")