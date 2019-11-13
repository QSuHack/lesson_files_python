def skrot(message):
    s = [ord(x) for x in "ALGORYTM"]
    message = message + ("." * (8 - len(message) % 8)) if len(message) % 8 != 0 else message
    for x in range(0, (len(message)), 8):
        for y in range(0, 8):
            s[y] = (s[y] + ord(message[x + y])) % 128

    wynik = ""
    print(len(message))
    print([x % 128 for x in s])
    for x in range(0, 8):
        wynik = wynik + chr(65 + (s[x] % 26))

    print(wynik)
    return wynik


def skrot_czysty(message):
    s = [ord(x) for x in "ALGORYTM"]
    message = message + ("." * (8 - len(message) % 8)) if len(message) % 8 != 0 else message
    for x in range(0, (len(message)), 8):
        for y in range(0, 8):
            s[y] = (s[y] + ord(message[x + y])) % 128
    wynik = ""
    for x in range(0, 8):
        wynik = wynik + chr(65 + (s[x] % 26))
    return wynik


def deszyfruj_podpis(podpis, d, n):
    wynik = ""
    for l in [int(x) for x in podpis.split()]:
        wynik += chr((l * d) % n)
    return wynik


podpisy, skroty = [], []
with open("podpisy.txt")as plik:
    for line in plik.readlines():
        podpisy.append( deszyfruj_podpis(line.replace("\n", ""), 3, 200))
with open("wiadomosci.txt") as plik2:
    for line in plik2.readlines():
        skroty.append(skrot_czysty(line.replace("\n", "")))


with open("epodpis_wynik.txt", mode="w+") as plik_wynikowy:
    plik_wynikowy.write("Wiarygodne wiadomości to: ")
    for x in range(1,12):
        if skroty[x-1] == podpisy[x-1]:
            plik_wynikowy.write(str(x)+" ")
print("Zadanie2\n" + "\n".join(podpisy))

print("Zadanie 1")
skrot(
    "W sieci mozna udawac wszystko z wyjatkiem tego co sie naprawde liczy. Nie mozesz udawac inteligencji, poczucia humoru ani blyskotliwosci, zlosliwosci, przewrotnosci, ani calej reszty twojej paskudnej, fascynujacej osobowosci.")
