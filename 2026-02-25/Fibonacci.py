# Ciąg Fibonacciego - pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich

# funkcja fibonacci z parametrem limit:
    # a = 0
    # b = 1
    # dopóki a będzie mniejsze lub równe parametrowi limit:
        # wyświetl zmienna a
        # a = b
        # b = a + stare b
# użytkownik jest pytany do ilu sprawdzać (limit), odpowiedz jest zapisywana jako int (l. całkowita) w zmiennej wybor
# program wyświetla Ciąg Fibonacciego do zmiennej wybor
# zostaje wywołana funkcja fibonacci z limitem równym zmiennej wybór

# domyślnie python po każdym print przenosi do nowej linijki, gdy doda się end="" po tym co chcemy wypisać zamiast przejść do nowej linijki wsztstko zostanie wypisane w jednej
# dlatego postawiłem end="" w print(a), aby ciąg fibonacciego został wyświetlony w jednej linijce, jeżeli chcemy aby liczby były oddzielone spacją to można użyć end=" "

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end="")
        a, b = b, a + b     #tuple unpacking    # a = b
                                                # b = a + stare b
wybor = int(input("do ilu sprawdzać: "))
print(f"Ciąg Fibonacciego do {wybor}:")
fibonacci(wybor)