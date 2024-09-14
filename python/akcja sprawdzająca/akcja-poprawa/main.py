open('wynik.txt', 'w').close()
open('dziesietne.txt', 'w').close()
open('liczby9.txt', 'w').close()

# 1.1

plik = open("przyklad.txt", "r")
#plik = open("anagram.txt", "r")
liczby_bin = plik.read()
liczby_bin = liczby_bin.split("\n")

plik.close()

g = open("wynik.txt","a")
h = open("dziesietne.txt","a")
f = open("liczby9.txt", "a")

counter1 = 0
counter0 = 0

zr = 0
prawie_zr = 0

for x in range(len(liczby_bin)):

  counter1 = 0
  counter0 = 0

  for y in range(len(liczby_bin[x])):
    if int(liczby_bin[x][y]) == 1:
      counter1 = counter1 + 1
    elif int(liczby_bin[x][y]) == 0:
      counter0 = counter0 + 1

  if counter0 == counter1:
    zr = zr + 1
  if abs(int(counter1) - int(counter0)) == 1:
    prawie_zr = prawie_zr + 1

print(zr, prawie_zr)
g.write(f"1.1) {zr}, {prawie_zr}")
g.write("\n")

# 1.2

anagramy = []

for x in range(len(liczby_bin)):

    counter1 = 0
    counter0 = 0

    for y in range(len(liczby_bin[x])):
        if int(liczby_bin[x][y]) == 1:
            counter1 = counter1 + 1
        elif int(liczby_bin[x][y]) == 0:
            counter0 = counter0 + 1
    if counter0 + counter1 == 8:
        if counter0 == 4 or counter1 == 5:
            anagramy.append(liczby_bin[x])

print(anagramy)
g.write(f"1.2) {anagramy}")
g.write("\n")

# 1.3

max = 0

# binarne - > dziesietne
for x in range(len(liczby_bin)):
    liczba = int(0)
    len_ciagu = int(len(liczby_bin[x]))
    for y in range(len_ciagu):
        liczba = liczba + (2**(len_ciagu-y-1))*(int(liczby_bin[x][y]))
        #print(y, liczby_bin[x][y], liczba, len_ciagu)
    h.write(str(liczba))
    h.write("\n")

h.close()

plik2 = open("dziesietne.txt", "r")
liczby_dzies = plik2.read()
liczby_dzies = liczby_dzies.split("\n")
liczby_dzies.pop()

for x in range(len(liczby_dzies)-1):
    delta = abs(int(liczby_dzies[x]) - int(liczby_dzies[x+1]))
    #print(delta, max)
    if (delta > max) == True:
        max = delta
    
print((bin(max))[2:])

g.write(f"1.3) {(bin(max))[2:]}")
g.write("\n")

plik2.close()

# 1.4

for x in range(len(liczby_dzies)):
    liczba2 = int(liczby_dzies[x])
    reszta = int(0)
    liczba_dziewiec = ""
    while (( int(liczba2) > 0 ) == True) :
        reszta = int(liczba2) % 9
        liczba2 = int(liczba2) // 9
        liczba_dziewiec = str(int(reszta)) + liczba_dziewiec
    f.write(str(liczba_dziewiec))
    f.write("\n")

f.close()

plik3 = open("liczby9.txt", "r")
liczby_dziewiec = plik3.read()
liczby_dziewiec = liczby_dziewiec.split("\n")
liczby_dziewiec.pop()

plik3.close()

#print(liczby_dziewiec)

#a)
bez_zera = 0

for x in range(len(liczby_dziewiec)):
    ilosc_0 = int(0)
    for y in range(len(liczby_dziewiec[x])):
        if int(liczby_dziewiec[x][y]) == 0:
            ilosc_0 = ilosc_0 + 1
    if ilosc_0 > 0:
        bez_zera = bez_zera + 1

print(bez_zera)

g.write(f"1.4) a) {bez_zera}")
g.write("\n")

#b)
najw_suma = 0
wartosc_o_najw_sumie = ""
ilosc_najw = 0

#print(liczby_dziewiec)

for x in range(len(liczby_dziewiec)):
    lista_cyfr = []
    suma_cyfr = 0
    for y in range(len(liczby_dziewiec[x])):
        current_value = liczby_dziewiec[x][y]
        if (str(liczby_dziewiec[x][y]) in lista_cyfr) == False:
            lista_cyfr.append(liczby_dziewiec[x][y])
            suma_cyfr = suma_cyfr + int(liczby_dziewiec[x][y])
            #print(liczby_dziewiec[x], suma_cyfr)
            #print(suma_cyfr, liczby_dziewiec[x][y] ,liczby_dziewiec[x])
            
    if suma_cyfr == najw_suma:
        ilosc_najw = ilosc_najw + 1
        najw_suma = suma_cyfr
        wartosc_o_najw_sumie = liczby_dziewiec[x]
        
    if suma_cyfr > najw_suma:
        najw_suma = suma_cyfr
        wartosc_o_najw_sumie = liczby_dziewiec[x]
        
print(wartosc_o_najw_sumie, ilosc_najw)
    
g.write(f"1.4) b) liczba: {wartosc_o_najw_sumie}, wystąpienia: {ilosc_najw}")
g.write("\n")

g.close()