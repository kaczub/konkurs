# sprawdza czy numer jest z Polski

# program pyta uzytkownika o ciąg znaków (str) i przypisuje go zmiennej numer
# jeżeli zmienna numer zaczyna się ciągiem znaków 48 (startswith)
    # wyświetla "Numer z kierunkowym PL!")
# w przeciwnym razie
    # wyświetla inny kraj


numer = str(input("Podaj numer telefonu zaczynając od kierunkowego: "))
if numer.startswith("48"):
    print("Numer z kierunkowym PL!")
else:
    print("Inny kraj")