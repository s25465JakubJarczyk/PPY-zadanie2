pierwszy = "Python 2023"
drugi = "Python 2023"
trzeci = "Python 2023"

if pierwszy == drugi and drugi == trzeci:
    czyPrawda = bool(1)
    print(czyPrawda)
else:
    czyPrawda = bool(0)
    print(czyPrawda)

print(type(pierwszy), hex(id(pierwszy)))
print(type(drugi), hex(id(drugi)))
print(type(trzeci), hex(id(trzeci)))
print("Java 11")

if pierwszy == drugi and drugi == trzeci:
    czyPrawda = bool(1)
    print(czyPrawda)
else:
    czyPrawda = bool(0)
    print(czyPrawda)

print(type(pierwszy), hex(id(pierwszy)))
print(type(drugi), hex(id(drugi)))
print(type(trzeci), hex(id(trzeci)))
print("Java 11")


#==================================================


print("Prosty kalkulator")
liczba1 = float(input("Podaj piwerwsza liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))

print("Wybierz operacje matematyczna: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
wybor = input("Twój wybór (1/2/3/4): ")

if wybor == '1':
    wynik = liczba1 + liczba2
    print(liczba1, "+", liczba2, "=", wynik)
elif wybor == '2':
    wynik = liczba1 - liczba2
    print(liczba1, "-", liczba2, "=", wynik)
elif wybor == '3':
    wynik = liczba1 * liczba2
    print(liczba1, "*", liczba2, "=", wynik)
elif wybor == '4':
    wynik = liczba1 / liczba2
    print(liczba1, "/", liczba2, "=", wynik)
else:
    print("Nieprawidłowy wybór")



#=====================================================

print("Witaj w ankiecie!")

# utwórz słownik z pytaniami ankiety i możliwymi odpowiedziami
ankieta = {
    "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie": ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki", "spotkania z rodziną/przyjaciółmi"],
    "W jakich okolicznościach czytasz książki najczęściej?": ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)", "w ogóle nie czytam"],
    "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?": ["chęć poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "fakt, że czytanie jest modne", "czytanie to moje hobby"]
}
odpowiedzi = {}

for pytanie, odpowiedzi_mozliwe in ankieta.items():
    print(pytanie)

    for i, odpowiedz in enumerate(odpowiedzi_mozliwe):
        print(str(i + 1) + ".", odpowiedz)

    odpowiedz = input("Odpowiedź: ")
    odpowiedzi[pytanie] = odpowiedzi_mozliwe[int(odpowiedz) - 1]

print("Twoje odpowiedzi:")
for pytanie, odpowiedz in odpowiedzi.items():
    print(pytanie + ":", odpowiedz)
