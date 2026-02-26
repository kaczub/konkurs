# sortowanie kolorów wg słownika

# program prosi użytkownika o 2 kolory, dodałem .lower(), ponieważ gdy python porównuje string duża litera i mała litera mają inną wartość. 
# potem porównuje obie zmienne, a że każda litera w typie danych string ma przypisaną liczbę to porównuje liczbę przypisaną literze. 
# f to f-string, pozwala on na wstawienie zmiennej do tekstu
# dodałem wykrywanie dwóch identycznych słów.


kolo1 = str(input("Podaj nazwę pierwszego koloru: ")).lower()
kolo2 = str(input("Podaj nazwe drugiego koloru: ")).lower()
if kolo1 < kolo2:
    print(f"Słowo '{kolo1}' jest wcześniej w słowniku niż '{kolo2}'")
elif kolo1 > kolo2:
    print(f"Słowo '{kolo2}' jest wcześniej w słowniku niż '{kolo1}'")
else:
    print(f"Oba słowa są identyczne")


