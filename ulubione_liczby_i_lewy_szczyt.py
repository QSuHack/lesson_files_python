x = [5, 2, 3, 4, 5, 1]
y = [4, 5, 2, 4, 3, 5]


def lewy_szczyt(x, y):
    i = 1
    mx = x[0]
    my = y[0]
    n = len(x)
    while i <= (n - 1):
        if x[i] / y[i] < mx / my:
            mx = x[i]
            my = y[i]
        i += 1
    return mx, my


# print(lewy_szczyt(x,y))


def szukaj_parzystej(stos_liczb):
    """
    Ulubione liczby
    Jaś i Małgosia.
    Liczby najpierw nieparzyste, potem parzyste, nieznana ilość poszczególnych
    szukamy pierwszej parzystej w złożoności lepszej niż liniowa (log n)
    """
    n = len(stos_liczb)
    a, b = 1, n - 1

    while b - a > 1:
        s = (a + b) // 2
        if stos_liczb[s] % 2 == 0:
            b = s
        else:
            a = s
    return stos_liczb[b]


print(szukaj_parzystej([int(x) for x in input().split()]))  # wejście w postaci "1 5 7 11 4 12 6 8"
