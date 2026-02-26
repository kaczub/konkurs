# przeliczanie dec na bin, oct, hex

# program pyta użytkownika o wartośc int (liczbę całkowitą) i zapisuje ją w zmiennej n
# wyświetla wartość w systemie binarnym dla wartości n
# wyświetla wartość w systemie ósemkowym dla wartości n
# wyświetla wartość w systemie szestnastkowym dla wartości n

n = int(input("Podaj wartość: "))
print("bin: ", bin(n))
print("oct: ", oct(n))
print("hex: ", hex(n))

