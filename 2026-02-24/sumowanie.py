# sumowanie

# funkcja sumowanie z parametrem n:
    # suma = 0
    # pętla for dla każdej liczby w zakresie od 1 do n +1:
        # suma = suma + 1 
    # zakończenie funkcji i zwrócenie wyniku suma 
# użytkownik jest proszony o podanie liczby, która jest zapisywana w zmiennej liczba jako int (liczba całkowita)
# funkcja sumowanie(liczba) zostaje przypisanana do zmiennej wynik
# program wyświetla ile wynosi suma liczb od 1 do {liczba}

# np jeżeli liczba = 3 to:
# for i in range (1, 3 + 1), czyli pętla powtórzy się 3 razy 
    # za każdym razem do zmiennej suma jest dodawana liczba która jest w zmiennej i: 
# 1 raz:
    # 0 + 1
# 2 raz:
    # 1 + 2
# 3 raz:
    # 3 + 3
# czyli suma będzie wynosić 6

def sumowanie(n):
    suma = 0 
    for i in range (1, n + 1):
        suma += i # suma = suma + i
    return suma
liczba = int(input("Podaj liczbę: "))
wynik = sumowanie(liczba)
print(f"Suma liczb od 1 do {liczba} wynosi: {wynik}")