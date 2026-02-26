# palindromy - wyrazy, zdania lub liczby, które czytane od lewej do prawej oraz od prawej do lewej brzmią tak samo (np. kajak, zakaz)

# program pyta użytkownika o liczbę do sprawdzenia i zapisuje ją w zmiennej liczba

# jeżeli zmnienna liczba będzie taka sama jak zmienna liczba od tyłu:
    # wyświetl że liczba jest palindromem
# w przeciwnym razie:
    # wyświetl że liczba nie jest palindromem

liczba = input("Podaj liczbę do sprawdzenia: ")

if liczba == liczba[::-1]:
    print(f"Tak, {liczba} jest palindromem.")
else:
    print(f"Nie, {liczba} nie jest paindromem.")