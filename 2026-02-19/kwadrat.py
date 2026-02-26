# kwadrat liczby, który kończy się tak samo

# pętla for dla każdej liczby pomiędzy 1 a 1001:
    # zmienna kwadrat = i do potęgi drugiej (kwadratu)

    # s_i = zamiana i na string (ciąg znaków)
    #s_kwadrat = zamiana zmiennej kwadrat na string (ciąg znaków)

    # jeżeli s.kwadrat kończy się na jakąś liczbę z zakresu od 1 do 1001:
        # wyświetl jaka to liczba


for i in range(1, 1001):
    kwadrat = i ** 2

    s_i = str(i)
    s_kwadrat = str(kwadrat)

    if s_kwadrat.endswith(s_i):
        print(f"Liczba: {i}, bo {i}^2 = {kwadrat}")