# przeliczanie z dec na bin

# program pyta użytkownika o wartośc dziesiętną i zapisuje ją jako string (ciąg znaków)
# zmienna wynik ma przypisaną wartość zmiennej dziesietna zamienionej na int (liczbę całkowitą) oraz bin (system dwójkowy)
# wyświetla wynik zamieniony na bin 

dziesietna = input("Podaj dziesiętną: ")
wynik = bin(int(dziesietna))
print(f"binarnie to: {wynik}")