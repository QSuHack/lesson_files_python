import math
def skrot(wiadomosc:str):
    start = "ALGORYTM"
    start = list(start)
    tab= []
    for i in range(0,math.ceil(len(wiadomosc)//8)+1):
        tab.append(wiadomosc[8*i:8*i+1])

    for s in range(0, len(start)):
        start[s] = ord(start[s])
    while len(wiadomosc) < 8:
        wiadomosc += "."

