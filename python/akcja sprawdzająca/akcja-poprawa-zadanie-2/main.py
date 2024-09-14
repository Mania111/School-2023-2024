open('odpowiedzi.txt', 'w').close()
g = open("odpowiedzi.txt","a")

def wczytaj_tablice(nazwa_pliku):
    array_3d = []
    with open(nazwa_pliku, 'r') as file:
        array_2d = []
        for line in file:
            line = line.strip()
            if line == "":
                
                if array_2d:  
                    array_3d.append(array_2d)
                    array_2d = []
            else:
                
                row = list(line)
                array_2d.append(row)
        
        if array_2d:
            array_3d.append(array_2d)
    return array_3d

nazwa_pliku = 'szachy_przyklad.txt'
array_3d = wczytaj_tablice(nazwa_pliku)

print(array_3d[0][1][5])

#2.1

ilosc_kropek = 0
pusta_kolumna = 0
max_pustych_kolumn = 0
plansze_z_pustymi_kolumnami = 0

for x in range(len(array_3d)):
    print("------Tablica: ", x, " -------")
    pusta_kolumna = 0
    for kolumna in range(8):
        ilosc_kropek = 0
        for wiersz in range(8):
            if (array_3d[x][wiersz][kolumna] == "."):
                ilosc_kropek = ilosc_kropek + 1
        if ilosc_kropek == 8:
            pusta_kolumna = pusta_kolumna + 1
            print("Kolumna ", kolumna, " jest pusta" )

    if pusta_kolumna >= 1:
        plansze_z_pustymi_kolumnami = plansze_z_pustymi_kolumnami + 1
    
    if pusta_kolumna > max_pustych_kolumn:
        max_pustych_kolumn = pusta_kolumna
        
    print("-----Liczba pustych kolumn: ", pusta_kolumna)

print(plansze_z_pustymi_kolumnami, max_pustych_kolumn)
g.write(f"2.1) {plansze_z_pustymi_kolumnami} plansz z pustymi kolumnami, największa liczba pustych kolumn na planszy - {max_pustych_kolumn}")
g.write("\n")

#2.2

ilosc_zr_plansz = 0
najm_liczba_bierek = 64

for x in range(len(array_3d)):
    print("Tablica: ", x, "-----")
    krol_d = 0
    krol_m = 0
    wieza_d = 0
    wieza_m = 0
    skoczek_d = 0
    skoczek_m = 0
    hetman_d = 0
    hetman_m = 0
    goniec_d = 0
    goniec_m = 0
    pionek_d = 0
    pionek_m = 0
    for y in range(len(array_3d[x])):
        for z in range(len(array_3d[x][y])):
            if array_3d[x][y][z] == "K":
                krol_d = krol_d + 1
            if array_3d[x][y][z] == "k":
                krol_m = krol_m + 1
            if array_3d[x][y][z] == "W":
                wieza_d = wieza_d + 1
            if array_3d[x][y][z] == "w":
                wieza_m = wieza_m + 1
            if array_3d[x][y][z] == "S":
                skoczek_d = skoczek_d + 1
            if array_3d[x][y][z] == "s":
                skoczek_m = skoczek_m + 1
            if array_3d[x][y][z] == "H":
                hetman_d = hetman_d + 1
            if array_3d[x][y][z] == "h":
                hetman_m = hetman_m + 1
            if array_3d[x][y][z] == "G":
                goniec_d = goniec_d + 1
            if array_3d[x][y][z] == "g":
                goniec_m = goniec_m + 1
            if array_3d[x][y][z] == "D":
                pionek_d = pionek_d + 1
            if array_3d[x][y][z] == "d":
                pionek_m = pionek_m + 1
    if (krol_d == krol_m) and (wieza_d == wieza_m) and (skoczek_d == skoczek_m) and (hetman_d == hetman_m) and (goniec_d == goniec_m) and (pionek_d == pionek_m) and ((krol_d + wieza_d + skoczek_d + hetman_d + goniec_d +  pionek_d) == (krol_m + wieza_m + skoczek_m + hetman_m + goniec_m + pionek_m)):
        print("tablica zrównoważona")
        ilosc_zr_plansz = ilosc_zr_plansz + 1
        if ((krol_d + krol_m + wieza_d + wieza_m + skoczek_d + skoczek_m + hetman_d + hetman_m + goniec_d + goniec_m + pionek_d + pionek_m) < najm_liczba_bierek):
            najm_liczba_bierek = (krol_d + krol_m + wieza_d + wieza_m + skoczek_d + skoczek_m + hetman_d + hetman_m + goniec_d + goniec_m + pionek_d + pionek_m)
    else:
        print("tablica nie zrównoważona")

print("ilość zrównoważonych plansz : ", ilosc_zr_plansz, ", najmniejsza suma bierek : ", najm_liczba_bierek)
g.write(f"2.2) ilość zrównoważonych plansz : {ilosc_zr_plansz}, najmniejsza suma bierek : {najm_liczba_bierek}")
g.write("\n")

#2.3
szachD = 0
szachm = 0
zle = 0

for x in range(len(array_3d)):
    kolumna_wiezaW = []
    kolumna_wiezaw = []
    wiersz_wiezaW = []
    wiersz_wiezaw = []
    for y in range(len(array_3d[x])):
        for z in range(len(array_3d[x][y])):
            if array_3d[x][y][z] == 'W':
                for a in range(8):
                    kolumna_wiezaW.append(array_3d[x][a][z])
                for b in range(8):
                    wiersz_wiezaW.append(array_3d[x][y][b])
                    
            if array_3d[x][y][z] == 'w':
                for a in range(8):
                    kolumna_wiezaw.append(array_3d[x][a][z])
                for b in range(8):
                    wiersz_wiezaw.append(array_3d[x][y][b])
                    
    if ('k' in kolumna_wiezaW):
        zle = 0
        kolumna_wiezaW.remove('k')
        kolumna_wiezaW.remove('W')
        for i in range(len(kolumna_wiezaW)):
            if kolumna_wiezaW[i] != '.':
                zle = zle + 1
        if zle == 0:
            szachD = szachD + 1
    if ('k' in wiersz_wiezaW):
        zle = 0
        wiersz_wiezaW.remove('k')
        wiersz_wiezaW.remove('W')
        for i in range(len(wiersz_wiezaW)):
            if wiersz_wiezaW[i] != '.':
                zle = zle + 1
        if zle == 0:
            szachD = szachD + 1

    if ('K' in kolumna_wiezaw):
        zle = 0
        kolumna_wiezaw.remove('K')
        kolumna_wiezaw.remove('w')
        for i in range(len(kolumna_wiezaw)):
            if kolumna_wiezaw[i] != '.':
                zle = zle + 1
        if zle == 0:
            szachm = szachm + 1
    if ('K' in wiersz_wiezaw):
        zle = 0
        wiersz_wiezaw.remove('K')
        wiersz_wiezaw.remove('w')
        for i in range(len(wiersz_wiezaw)):
            if wiersz_wiezaw[i] != '.':
                zle = zle + 1
        if zle == 0:
            szachm = szachm + 1

print(szachD, szachm)
g.write(f"2.3) Wygrana białych : {szachD}, czarnych : {szachm}")

