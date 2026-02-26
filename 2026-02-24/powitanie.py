# powitanie

# funkcja powitanie z parametrami imie i wiek:
    # zmienna wynik wita użytkownika używając zmiennych imie i wiek
    # zakańcza funkcje
# program prosi użytkownika o wprowadzenie imienia i zapisuje je w zmiennej imie + zmienia 1 litere na dużą
# program prosi użytkownika o wprowadzenie wieku i zapisuje go w zmiennej wiek
# funkcja powitanie(imie, wiek) zostaje przypisana zmiennej wiadomosc
# program wyswietla funkcje powitanie

def powitanie(imie, wiek):
    wynik = (f"Cześć {imie}! Masz {wiek} lat.")
    return wynik
imie = input("Jak masz na imie? ").capitalize()
wiek = int(input("Ile masz lat? "))
wiadomosc = powitanie(imie, wiek)
print(wiadomosc)