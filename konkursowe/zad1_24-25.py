tekst = input("Wprowadź tekst do gazetki: ")

ilosc_znakow = len(tekst)
limit = 50

litery = 0
cyfry = 0

if ilosc_znakow <= limit:
    print(f"DŁUGOŚĆ: {ilosc_znakow}")
    print("MIEŚCI SIĘ W LIMICIE")
else:
    nadm_znaki = ilosc_znakow - limit
    skrocony = tekst[:limit]
    print(f"DŁUGOŚĆ: {ilosc_znakow}")
    print(f"PRZEKROCZONO LIMIT O: {nadm_znaki}")
    print(f"SKRÓCONY TEKST: {skrocony}")

for znak in tekst:
    if znak.isalpha():
        litery += 1
    if znak.isdigit():
        cyfry += 1

print(f"Liczba liter: {litery}, Liczba cyfr: {cyfry}")        
    