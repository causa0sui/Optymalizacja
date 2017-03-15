#!/usr/bin/python
import random
def czybije(Macierz, n): # plansza - lista
    hetmani = []
    for i in range(n):
        for j in range(n):
            if Macierz[i][j] == "H":
                hetmani.append((i,j))

    for hetm1 in hetmani:
        for hetm2 in hetmani:
            if hetm1 != hetm2:
                if hetm1[0] == hetm2[0]:
                    return False
                if hetm1[1] == hetm2[1]:
                    return False
                if abs(hetm1[0] - hetm2[0]) == abs(hetm1[1] - hetm2[1]):
                    return False
    return True

def generuj(n): # napis.lower() ~~~~~~~ lower(napis)
    macierz = []

    for i in range(n):
        macierz.append([])
    # [[],[],[],[],[],[],[],[], []]

    for i in range(n):
        for j in range(n):
            macierz[i].append(".")

    for i in range(n):
        j = random.randint(0, n - 1)
        macierz[i][j] = "H"
    return macierz

n = int(input())
macierz = generuj(n)

while not czybije(macierz, n):
    macierz = generuj(n)

for i in range(n):
    xd = ""
    for j in range(n):
        xd = xd + macierz[i][j]
        xd += " "
    print(xd)
    for i==1 and i==2 and i==3:
        print("ERROR")
