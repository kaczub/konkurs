# sprawdza czy liczba jest pierwsza 
# liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki naturalne: 1 oraz samą siebie

# program pyta użytkownika o liczbę do sprawdzenia i zapisuje ją jako int w zmiennej liczba
# jeżeli zmienna liczba jest mniejsza od 2:
    # zmienna wynik (bool) dostaje wartośc False
# w przeciwnym razie:
    # zmienna wynik (bool) dostaje wartośc True
    #pętla for dla każdej liczby w zakresie od 2 do wartości pierwiastka kwadratowego z zmiennej liczba za każdym razem dodane 1
        # jeżeli modulo (reszta z dzielenia) zmniennej liczba przez zmienna i będzie równa 0:
            # przypisz zmiennej wynik wartośc False
            # zakończ pętle
# jeżeli zmienna wynik (domyślnie true):
    # wyświetl że liczba jest pierwsza
# w przeciwnym razie:
    # wyświetl że liczba nie jest pierwsza



liczba = int(input("Podaj liczbę do sprawdzenia: "))
if liczba < 2:
    wynik = False
else:
    wynik = True
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            wynik = False
            break
if wynik: 
    print(f"Liczba {liczba} JEST pierwsza.")
else:
    print(f"Liczba {liczba} NIE JEST pierwsza.")