# ile nominałow trzeba wydać

# zmienna nominały to lista zawierająca nominały
# zmienna reszta pyta użytkownika o kwotę i zapisują ją jako liczba całkowita (int)
# wyświetla jakie nominały wydaje, f-string pozwala na dodanie w środku tekstu zmiennej

# pętla for bierze każdy nominał z listy i wykonuje dla niego pętle, gdy nominały się skończą pętla się zakończy
    # jeżeli zmienna reszta jest większa lub równa nominałowy dla którego jest wykonywana teraz pętla:
        # zmienna ile razy jest równa reszcie podzielonej bez reszty przez n (nominał z listy)
        # zmienna reszta zostaję zastępiona resztą z dzielenia (modulo) z zmiennej reszta

        # program wyświetla w nowej linijce ile szt nominału {n} musimy użyć 

nominały = [200, 100, 20, 10, 5, 2, 1]
reszta = int(input("Podaj kwotę reszty do wydania: "))
print(f"Dla kwoty {reszta} wydaję: ")

for n in nominały:
    if reszta >= n:
        ile_razy = reszta // n
        reszta = reszta % n
        
        print (f"Nominał {n} zł: {ile_razy} szt.")
