def licz_cyf_cenz(wejscie):
    litery = 0
    cyfry = 0
    ocenzurowane_znaki = 0
    for znak in wejscie:
        if znak.isalpha():
            litery += 1
        if znak.isdigit():
            cyfry += 1
        if znak == "*":
            ocenzurowane_znaki += 1

    return litery, cyfry, ocenzurowane_znaki

def cenzura(wejscie, lista_zakazow):
    slowa = wejscie.split()
    wynik = []

    for s in slowa:
        if s.lower() in [z.lower() for z in lista_zakazow]:
            print(f"Słowo {s} jest zakazane, zostanie ocenzurowane")
            wynik.append("*" * len(s))
        else:
            wynik.append(s)
    return " ".join(wynik) #sklejenie listy w jeden tekst


tekst = input("Podaj tekst ogłoszenia: ")
limit = int(input("Podaj limit: "))
zakaz = input("Podaj zakazane słowa oddzielone spacją: ").split()


cenz_tekst = cenzura(tekst, zakaz)
dlugosc_cenz = len(cenz_tekst)
litery, cyfry, ocenzurowane_znaki = licz_cyf_cenz(cenz_tekst)

print("-" * 30)

if dlugosc_cenz <= limit:
    print(f"Długość z cenzurą (jeżeli wystąpiła): {dlugosc_cenz}")
    print(f"Tekst mieści się w limicie znaków, do osiągnięcia limitu brakuje {limit - dlugosc_cenz} znaków ")
    print(f"Tekst: {cenz_tekst}")
else:
    skr_cenz = cenz_tekst[:limit]
    
    print(f"Długość z cenzurą (jeżeli wystąpiła): {dlugosc_cenz}")
    print(f"Tekst przekroczył ilośc znaków o {dlugosc_cenz - limit}, tekst zostanie skrócony.")
    print(f"Skrócony tekst: {skr_cenz}")


print(f"Liczba liter: {litery}, Liczba cyfr: {cyfry}, Ocenzurowane znaki: {ocenzurowane_znaki}")