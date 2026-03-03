orginal = input("Podaj tekst do sprawdzenia: ")
tekst = orginal.lower().replace(" ", "")
if tekst == tekst[::-1]:
    print(f"Tak, {orginal} jest palindromem.")
else:
    print(f"Nie, {orginal} nie jest paindromem.")

    # teraz program wykrywa że Kobyła ma mały bok jest palindromem 
    # bez względu na wielkośc i spacji.