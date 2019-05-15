import math


def odw(slowo):
    """
    Odwraca słowo.
    :param slowo:
    """
    return slowo[::-1]


def odw2(slowo):
    """
    odwraca słowo dłuższa wersja
    :param slowo:
    :return:
    """
    tmp = ""
    for x in slowo:
        tmp = x + tmp
    return tmp


def szukaj_dzielnikow(liczba):
    """
    Znajduje dzielniki liczby mniejsze < liczba
    :param liczba:
    :return: lista dzielników
    """
    n = math.floor(math.sqrt(liczba))
    lista_dzielnikow = [1]
    for x in range(2, n + 1):
        if liczba % x == 0:
            lista_dzielnikow.append(x)
            lista_dzielnikow.append(math.floor(liczba / x))
    return lista_dzielnikow


def czy_doskonala(liczba):
    """
    Sprawdza czy podana liczba jest doskonała.
    :param x:
    :return: true/false
    """
    return sum(szukaj_dzielnikow(liczba)) == liczba


def liczba_cyfr(liczba):
    """Zwraca liczbę cyfr"""
    licz_cyfry = 0
    while liczba != 0:
        liczba = liczba // 10
        licz_cyfry += 1
    return licz_cyfry


def czy_palindrom(slowo):
    """Sprawdza czy string jest palindromem"""
    return slowo == slowo[::-1]


def powielanie(wyraz, liczba):
    rezultat = ""
    for x in wyraz:
        rezultat = rezultat + (x * liczba)
    return rezultat


def nwd(a, b):
    """wylicza największy wspólny dzielnik"""
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def skracanie(licznik, mianownik):
    """skraca ułamek"""
    if math.isnan(licznik) or math.isnan(mianownik):
        licznik = int(licznik)
        mianownik = int(mianownik)
    nwd_ = nwd(licznik, mianownik)
# to zwraca tuple a na wyjściu oczekuemy dwóch wartości oddzielonych spacją
# return math.floor(licznik / nwd_), math.floor( mianownik / nwd_)
    return str(math.floor(licznik / nwd_))+ " " + str(math.floor( mianownik / nwd_))


if __name__ == "__main__":
    print(skracanie(2, 4))
    print(odw(input()))
    print(odw2(input()))
