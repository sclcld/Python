# """ 
#     Esercizio 
#     Abbiamo la stringa: nome_scuola = "Epicode" 
#     Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.
# """

# nome_scuola = "Epicode"
# index = 0



# """ 
#     Esercizio 
#     Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while. Utilizzeremo:     
#     • un ciclo while 
#     • la funzione print() 
#     • una variabile, che dovrà essere inizializzata 
#     • una procedura di incremento
# """ 

# num = 0

# while num < 21:

#     print(num)

#     num += 1

# """
#     Esercizio 
#     Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.
# """    
# power = 0
# while power <= 10:

#     print(2 ** power)
#     power += 1

# """
#     Esercizio 
#     Calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while, domandando all'utente 
#     di inserire N
# """    
# power_inp = int(input("insert power:"))
# temp = 0
# while temp <= power_inp:
#     print(2 ** temp)
#     temp += 1
# """"Esercizio Calcolare e stampare tutte le potenze di 2 minori di 25000."""
# powers = 0
# pw = 0
# while powers < 25000:
  
#    powers= 2 ** pw
#    print(powers)
#    pw += 1

# """Esercizio (1/2) Abbiamo due liste, una di studenti e una di corsi:"""

# studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
# corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

# """ Esercizio (2/2) Aggiungere i dati mancanti alla lista corsi, sapendo che Emma segue Data Analyst 
#     Faith segue Backend Grace segue Frontend Henry segue Cybersecurity Aggiungeremo i dati mancanti uno 
#     alla volta con il metodo per appendere in coda alle liste, poi verificheremo che sono della stessa 
#     lunghezza e se lo sono stamperemo la lista corsi. Se alcuni dati sono già presenti non vanno aggiunti 
#     di nuovo.
# """

# for spec in ["Data Analyst", "Backend", "Frontend", "Cybersecurity"]:
#     corsi.append(spec)
# if len(studenti) == len(corsi):
#     print(corsi)    
# """"Esercizio 
#     Scriviamo un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, 
#     seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri, similmente all'esercizio della 
#     lezione scorsa. Stavolta facciamo attenzione a tutti i casi particolari, ovvero implementare 
#     soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri."""
# string = input("insert a word: ")
# half = len(string)//2
# print(f"{string[:half]}:{string[half:]}")
# """
#     Esercizio 
#     Memorizza e stampa tutti i fattori di un numero dato in input. 
#     Esempio: • input: 150 • output: [2, 3, 5, 5]
# """
# num = int(input("insert a number: "))
# divisor = 2
# factors = []
# while num > 1:
#     if num % divisor == 0:
#         factors.append(divisor)
#         num //= divisor
 
#     else:
#         divisor += 1
# """
#     Esercizio 
#     Abbiamo la stringa: nome_scuola = "Epicode" Stampare ogni carattere della stringa, uno su ogni riga, 
#     utilizzando un costrutto for.
# """
# nome_scuola = "Epicode"
# for lettera in nome_scuola:
#      print(lettera)

# """
#     Esercizio 
#     Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo.
# """
# for x in range(1, 11):
#     print(2 ** x)

# """
#     Esercizio 
#     Calcolare (ma non stampare) le prime N potenze di K;
#       ognuna di esse andrà memorizzata in coda a una lista. 
#       Alla fine, stampare la lista risultante. 
#       Proviamo con diversi valori di K, oppure facciamola inserire all'utente. 
#       Realizzare due versioni: • con un ciclo while, • con un ciclo for.
# """
# #inputs

# powers = []
# num = int(input("insert a number: "))
# pow = int(input("insert its power: "))

# #v1 while
# index = 0

# while index <= pow:
#     powers.append(num**index)
#     index += 1

# print(powers)    

# powers = []

# #v2 for
# for x in range(pow):
#     powers.append(num**x)

# print(powers)

# #v3 list comprehension
# powers = [num**x for x in range(pow)]

# """"Esercizio 
#     usando un costrutto for, calcolare la media dei guadagni e stamparla a video.
#     abbiamo una lista con i guadagni degli ultimi 12 mesi: 
# """


guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
sum = 1
mean = 0

for x in guadagni:

    sum += x

print(sum//12)

""""
    Esercizio 
    Abbiamo una lista di parole: 
    parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", 
    "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"] stampiamo, per ogni parola,
    quante volte appare la lettera "e"; facciamo attenzione al fatto che appare sia maiuscola che 
    minuscola.
"""
parole = [
            "Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", 
            "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"
        ]

for parola in parole:

    print(parola.lower().count("e"))

""" 
    Esercizio 
    Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo che: 
    • Ada guida una Punto 
    • Ben guida una Multipla 
    • Charlie guida una Golf 
    • Debbie guida una 107 
    Stampiamo il dizionario per intero, e poi l'auto associata a Debbie.
"""

owners = ["Ada", "Ben", "Charlie", "Debbie"]
cars = ["Punto", "Multipla", "Golf", "107"]
dizionario_auto = {}

if len(owners) == len(cars):

    for index in range(len(owners)):

        dizionario_auto[owners[index]] = cars[index]
        print(owners[index], dizionario_auto[owners[index]])

"""Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto che non sono una Multipla.""" 

for val in dizionario_auto.values():

    if val != "Multipla":

        print(val)

"""
    Esercizio
    Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto: 
    dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", 
    "Emily": "A1"} nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", 
    "Hugh": "Clio"} 
    Aggiornare il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari e stamparlo.
    Cosa è successo a Ben?
"""        
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}
dizionario_auto.update(nuovi_proprietari)

print(dizionario_auto)


"""
    Esercizio 
    Scrivere un programma che, data una lista di numeri, fornisca in output il minimo e il massimo 
    (possiamo usare o meno le funzioni built-in min() e max()).
"""

from random import randint

lista_numeri = [randint(1,1100) for x in range(randint(6,12))]
print(lista_numeri)


max = 0

for num in lista_numeri:

    if num > max:

        max = num

min = max

for n in lista_numeri:

    if n < min:

        min = n
    
    

print(max, min)        

"""
    Esercizio 
    Scrivere un programma che 
    • in input acquisisce una lista di numeri e un numero K 
    • in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K 
    • se non ce ne dovesse essere nessuno, dovrà stampare a schermo un messaggio adeguato.
"""

# lista_nums = input("Type in a list of numbers, separated by commas: ").split(",")
# k = int(input("Type in a number: "))
# lista_nums = [int(num) for num in lista_nums]

# sum = 0
# count = 0

# for n in lista_nums:

#     if n >= k:
        
#         sum += n
#         count += 1

# if not count:
#     print("There is no number greater than or equal to the one selected.")
# else:
#     avg = sum / count
#     print(avg)

"""
    Esercizio 
    Scrivere un programma che, data una lista di numeri, come output stamperà lo stesso numero di 
    asterischi su righe diverse, ottenendo una semplice visualizzazione grafica 
    Esempio, supponendo di avere il seguente input: numeri = [5, 2, 3, 4] 
    L'output sarà: ***** ** *** ****
"""

#v1 dynamic
for x in range(randint(7,10)):

    print(randint(1,10) * "*")

#v2
lista_nums = [randint(1,10) for x in range(10)]

for y in lista_nums:

    print("*" * y)    

"""
    Esercizio 
    Abbiamo una lista di codici fiscali
    • trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla; 
    • inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi 
      al cognome.
"""

lista_cf = [
            "ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", 
            "XYZABC01D05A789F", "DEFGHI95J06A987G"
            ]

to_print = [cod for cod in lista_cf if "95" in cod]

for cf in to_print:

    print(cf)
    print(f"Name {cf[:3]}")
    print(f"Surname {cf[3:6]}")

"""
    Esercizio 
    Abbiamo tre liste della stessa lunghezza, dove ogni elemento nella medesima posizione si riferisce ai 
    dati dello stesso studente: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", 
    "Henry"] corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", 
    "Frontend", "Cybersecurity"] edizioni = [1, 2, 3, 2, 2, 1, 3, 3] 
    • Stampare a video tutti e soli gli studenti che frequentano una prima edizione; 
    non tutti i dati potrebbero essere necessari.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = [
        "Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", 
        "Cybersecurity"] 
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for student in zip(studenti, corsi, edizioni):

    ed = student[-1]
    
    if ed == 1:

        print(student)

"""
    Esercizio 
    Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati scritti con il 
    simbolo dell'euro: prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] cambiare il simbolo 
    dell'euro (€) in quello del dollaro ($) per ogni stringa nella lista; il risultato sarà memorizzato 
    in un'altra lista.
"""

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]
prezzi_updated = [price.replace("€", "$") for price in prezzi]

"""
    Esercizio 
    Abbiamo una lista di studenti 
    vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: 
    selezioneremo i nomi in posizione pari per un squadra, e i nomi in posizione dispari per l'altra. 
    Creiamo due liste per ogni squadra, e alla fine visualizziamole.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"] 
teamA = []
teamB = []

for index,student in enumerate(studenti):

    if index % 2 == 0:

        teamA.append(student)
        
    else:
        
        teamB.append(student)

"""
    Esercizio 
    Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a Dicembre): 
    dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media dei 
    guadagni precedenti, e specificare nell'output 
    se il guadagno attuale è maggiore o minore della media dei precedenti. 
    Esempio di un possibile output: 
    Mese 1: 100 € 
    Mese 2: 90 € (media prec: 100 € - il guadagno attuale è minore) 
    Mese 3: 70 € (media prec: 95 € - il guadagno attuale è minore)
"""  
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
total = 0
count = 1
current = 0

for rev in guadagni:

    total += rev
    avg = total // count
    if count > 0:
        print(f"media prec: {current} € - il guadagno è {'maggiore' if avg > current else 'minore'}")
    current = avg
    count += 1