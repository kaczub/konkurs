print("Jeżeli naciśniej enter program zakończy działanie")

while True:
    komunikat = input("Wprowadź dowolny komunikat: ")
    if komunikat == "":
        print("Dziękuje za miło spędzony czas")
        while input() != "":
            pass
        break
    else:
        komunikat = komunikat[::-1].capitalize()
        print(f"komunikat odwórcony: {komunikat}")

