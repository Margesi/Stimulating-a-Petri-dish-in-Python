import sys
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import random

## Do not forget to check for when both i and j are 0


random.seed(13)

n = int(input("Angabe der Größe der Petrischale: "))
bac = int(round(n * n * 0.8))

species = np.array(['A', 'B', 'C'])

developingsps = pd.DataFrame(columns=['Day', 'A', 'B', 'C', 'leer'])


def bewegung(orig, target):  # target neigbour
    target = orig
    orig = 'leer'
    return orig, target


def reproduktion(orig, target):
    target = orig
    return orig, target


def zerstorung(orig, target):
    target = 'leer'
    orig = orig
    return orig, target


bactpart = np.random.choice(species, bac)
petrisch = np.append(bactpart, np.repeat("leer", n * n - bac))
np.random.shuffle(petrisch)
petrisch = petrisch.reshape(n, n)
print(petrisch)

# add random probabilities

# Kondition probability r,b,z
ssp=input("Welche Stein-Schere-Papier von den Bakterien willst du haben? a) Bakterie A kann Bakterien B Zerstoren, B kann bakterien C Zerstoren und C kann A zerstoren, b)bakterie A kann Bakterien C zerstoren, C kann B zerstoren und B kann A zerstoren: ")

ta_key = True
pb = random.random()

while ta_key == True:
    if ssp=='a':
        pzab=random.random()
        pzac=0
        pzba=0
        pzbc=random.random()
        pzca=random.random()
        pzcb=0
        ta_key=False
    elif ssp =='b':
        pzab = 0
        pzac = random.random()
        pzba = random.random()
        pzbc = 0
        pzca = 0
        pzcb = random.random()
        ta_key=False
    else:
        ssp = input(
            "Welche Stein-Schere-Papier von den Bakterien willst du haben? a) Bakterie A kann Bakterien B Zerstoren, B kann bakterien C Zerstoren und C kann A zerstoren, b)bakterie A kann Bakterien C zerstoren, C kann B zerstoren und B kann A zerstoren: ")




print(petrisch)

for d in range(1, 300): #100 Jahre Iteration
    for i in range(1, n - 2):  # ursprungzelle iteration
        for j in range(1, n - 2):  #
            tb_key = True

            tries=0
            while tb_key == True:
                firstindice = np.random.choice(['m', 'l'])
                if firstindice == "m":               #nachbarzelle finden

                    m = j - np.random.choice([1, 0, -1])
                    if m == j:
                        l = i - np.random.choice([1, -1])
                    else:
                        l = i - np.random.choice([1, 0, -1])
                    t = [m, l]

                    if petrisch[j, i] != petrisch[t[0], t[1]]:
                        tb_key = False
                else:
                    l = i - np.random.choice([1, 0, -1])
                    if l == i:
                        m = j - np.random.choice([1, -1])
                    else:
                        m = j - np.random.choice([1, 0, -1])
                    t = [m, l]
                    if petrisch[j, i] != petrisch[t[0], t[1]]:
                        tb_key = False
                tries+=1
                if tries>=7:
                    tb_key = False
                continue




            # if t == [j,i]:
            #     print("equal")
            # else:
            #  print("not equal")
            print(t)
            print(j,i)
            print(petrisch[j,i])
            print(petrisch[m, l])

            if petrisch[j, i] == 'A':
                if petrisch[t[0], t[1]] == 'leer':
                    # fallunterscheidung bakterien
                    a = bewegung(petrisch[j, i], petrisch[t[0], t[1]])
                    b = reproduktion(petrisch[j, i], petrisch[t[0], t[1]])
                    if random.random() < pb:
                        c = a
                    else:
                        c = b
                    petrisch[j, i] = c[0]
                    petrisch[t[0], t[1]] = c[1]

                elif petrisch[t[0], t[1]] == 'B':
                    if random.random() < pzab:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]


                elif petrisch[t[0], t[1]] == 'C':

                    if random.random() < pzac:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]
                else:
                    print("same bacteria as original")
            elif petrisch[j, i] == 'B':
                if petrisch[t[0], t[1]] == 'leer':
                    # fallunterscheidung bakterien
                    a = bewegung(petrisch[j, i], petrisch[t[0], t[1]])
                    b = reproduktion(petrisch[j, i], petrisch[t[0], t[1]])
                    if random.random() < pb:
                        c = a
                    else:
                        c = b
                    petrisch[j, i] = c[0]
                    petrisch[t[0], t[1]] = c[1]

                elif petrisch[t[0], t[1]] == 'A':
                    if random.random() < pzba:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]


                elif petrisch[t[0], t[1]] == 'C':

                    if random.random() < pzbc:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]
                else:
                    print("same bacteria as original")
            elif petrisch[j, i] == 'C':
                if petrisch[t[0], t[1]] == 'leer':
                    # fallunterscheidung bakterien
                    a = bewegung(petrisch[j, i], petrisch[t[0], t[1]])
                    b = reproduktion(petrisch[j, i], petrisch[t[0], t[1]])
                    if random.random() < pb:
                        c = a
                    else:
                        c = b
                    petrisch[j, i] = c[0]
                    petrisch[t[0], t[1]] = c[1]

                elif petrisch[t[0], t[1]] == 'B':
                    if random.random() < pzcb:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]


                elif petrisch[t[0], t[1]] == 'A':

                    if random.random() < pzca:
                        c = zerstorung(petrisch[j, i], petrisch[t[0], t[1]])
                        petrisch[j, i] = c[0]
                        petrisch[t[0], t[1]] = c[1]

                else:
                    print("same bacteria as original")
            else:
                print("kein bakterien in ursprungzelle")

            print("\n")
            print("\n")
            print([j,i],[m,l])
            print(petrisch[j, i])
            print(petrisch[t[0], t[1]])
            print("\n")
            # print(petrisch)


    developingsps = developingsps.append({'A': np.count_nonzero(petrisch == 'A'), 'B': np.count_nonzero(petrisch == 'B'),
                                    'C': np.count_nonzero(petrisch == 'C'),
                                    'leer': np.count_nonzero(petrisch == 'leer'),
                                    'Day': d}, ignore_index=True)
    print(d)


# print(developingsps.head())


print("Die Bakterien die Uberlerbt haben sind: ")

if np.count_nonzero(petrisch[1:-2,1:-2]=='A')>=1:
    print("A")

if np.count_nonzero(petrisch[1:-2,1:-2]=='B')>=1:
    print("B")

if np.count_nonzero(petrisch[1:-2,1:-2]=='C')>=1:
    print("C")

vizdev=developingsps.iloc[::5, :]
vizdev.plot(x='Day',y=['A','B','C','leer'])

plt.show()


print(petrisch)


