# przesuwanie liter

# program pyta użytkownika o tekst i zapisuje go jako string (ciąg znaków) w zmiennej tekst
# program pyta użytkownika o liczbę i zapisuje ją jako int (liczba całkowita)
# wynik = ""

# pętla for dla każdej  litery w zmiennej tekst
    # jeżeli litera to spacja
        # wynik = wynik + " "

    # w przeciwnym razie:
        # program zamienia literę na numer w tabeli ASCII
        # program dodaje do numeru wartośc klucz i zapisuje to w zmiennej numer2
        # program przypisuje zmiennej wynik wartość wynik + zamienia wartośc numer2 znowu na litery

# wyświetl zaszyfrowaną informacje


tekst = input("Wpisz tekst:")
klucz = int(input("O ile miejsc przesunąć litery: "))
wynik = ""
for litera in tekst:
    if litera == " ":
        wynik = wynik + " "
    else:
        numer = ord(litera)
        numer2 = numer + klucz
        wynik = wynik + chr(numer2)

print("Zaszyfrowana informacja:", wynik)