# nww i nwd

# program prosi użytkownika o 2 liczby i zapisuje je jako zmienne a i b (int)
# zmienne pierwsza i druga mają przypisaną wartość a i b

    # algorytm euklidesa
# pętla while jest wykonywana dopóki zmienna b jest różna od zera
    # zmienna a jest zamieniana na b 
    # zmienna b jest zamieniana na modulo (resztę z dzielenia) liczby a przed zamianą jej na b (dlatego w komentarzu utworzyłem zmienną temp)

# zmienna nwd = a

# zmienna nww = pierwsza * podzielona całkowicie przed zmienna nwd (wzór)

# wyświetla nwd i nww i liczby jakie były wykorzystane

def nwd():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    pierwsza = a
    druga = b

    while b != 0:
        a, b = b, a % b     #temp = a % b
                        #a = b            
                        #b = temp
    


    nwd = a

    nww = (pierwsza * druga) // nwd

    print(f"Liczby {pierwsza} i {druga}")
    print(f"NWD: {nwd}")
    print(f"NWW: {nww}")

nwd()


