tekst = input("Wpisz tekst:")
klucz = int(input("O ile miejsc przesunąć znaki: "))
wynik = ""
for znak in tekst:
    if znak.islower(): #jeżeli znak jest małą literą
        numer = ord(znak) - ord("a") # numer = znak jest zamieniana na ascii, np a zamienione na 97, po czym odejmuje wartość a, czyli 97 dla wygody, czyli (a=0, b=1 itd)
        numer2 = numer + klucz # do numer2 dodaje numer i klucz, czyli np klucz to 3, np. skoro a to 0, to po dodaniu 3 wyjdzie d
        numer3 = numer2 % 26 # reszta z dzielenia przez 26, ponieważ podstaowy alfabet ma 26 znaków. Jeżeli klucz to 3, a znak to będzie z to 25, to po dodaniu wyjdzie 28, co wychodzi po za alfabet. Dlatego 28 % 26 daje nam 2, czyli c, zrobi się jakby pętla.
        wynik = wynik + chr(numer3 + ord("a")) # wynik = do wyniku program dodaje zamienioną już na zwykłe litery wartośc zmiennej numer3 dodając do tego wartość a w ascii, żeby można było to zamienić znowu na właśnie ascii
    elif znak.isupper(): #jeżeli znak jest dużą literą
        numer = ord(znak) - ord("A") # ta sama sytuacja jak powyżej, tylko odejmując i dodając potem wartośc dużego A, czyli 65
        numer2 = numer + klucz 
        numer3 = numer2 % 26
        wynik = wynik + chr(numer3 + ord("A"))
    else:
         wynik = wynik + znak # w szyfrze cezara zazwyczaj nie przesuwa się cyfr, ani znaków. Działa to tez na spacje, czyli nie przesuwa spacji.

            # w przeciwnym razie (cyfra lub znak) tez przesuwa ją o klucz
            #numer = ord(znak)
            #numer2 = numer + klucz
            #wynik = wynik + chr(numer2)
        

print("Zaszyfrowana informacja:", wynik)