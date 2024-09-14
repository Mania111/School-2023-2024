# age pomiędzy 18 a 65
age = 22
if 18 <= age < 65:
  print("OK")
else:
  print("nie OK")

  
# sprawdzenie czy zmienna ma wartość
imie = "jan"

print(bool("")) # zwraca false - brak wartości
print(bool("tomek")) # zwraca true - wartość istnieje

if imie: # imie jest "Truthy"
  print("Tak")


succesful = True
for number in range(3): # loop
  print("Attempt")
  if succesful:
    print("Succesful")
    break
else:
  print("Attempted 3 times and failed") # gdy loop jest nieudany

for x in range(5):
  for y in range(3):
    print(f"({x},{y})")


# Iterable - czyli można po tym w pętli coś robić
for x in "Python":
  print(x)

parzyste = 0
for liczba in range(10):
  if liczba%2 == 0:
    print(liczba)
    parzyste = parzyste+1
print(f"parzyste = {parzyste}")

# def - tworzy funkcje
def dodawanie(x, y, z):
    print(x + y)

dodawanie(2, 3, 5) #uruchom def
