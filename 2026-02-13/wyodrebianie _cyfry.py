# wyodrębnianie cyfry z liczby

# program pyta używkownika o liczbę i zapisuje ją jako int, czyli liczbę całkowitą. 
# pętla while odbywa się dopóki liczba nie będzie równa 0
# zmienna czyfra to reszta z dzielenia liczby przez 10, czyli zostaje to co nie ma pełnej 10, np 1234 zostaje 4
# wypisuje tą cyfrę
# liczba zostaje podzielona całkowice przez 10, czyli ta ostatnia cyfra zostaje ucięta, np 1234 zostaje 123

# gdy liczba osiągnie zero wszystkie cyfry będą wypisane


liczba = int(input("Podaj liczbę: "))
while liczba > 0:
    cyfra = liczba % 10
    print (f"Pobrano cyfrę: {cyfra}")

    liczba = liczba // 10