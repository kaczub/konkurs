# przeliczanie z bin na dec

# program pyta użytkownika o wartośc binarną i zapisuje ją jako string 
# zmienna wynik ma przypisaną wartość zmiennej binarna, która jest zamieniona na int czyli liczbę całkowitą. 2 oznacza system dwójkowy (bin), np. gdyby napisać 8 to byłby ósemkowy (oct) itd. 
# program wyświetla wynik w systemie dwójkowym.

binarna = input("Podaj wartośc binarną: ")
wynik = int(binarna, 2)
print(f"dziesiętna: {wynik}")