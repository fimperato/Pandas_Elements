# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 

@author: Francesco
"""

## per Counter section:
from collections import Counter

## Task 02 
print("\r\n## Task 2")
print("Hello world!")
STR_0 = "HeLLo world!"
print(STR_0.lower())
print(STR_0.upper())
print(STR_0.capitalize())
print(STR_0[0])

## b è la notazione per l'array binario
print("\r\n## b è la notazione per l'array binario")
BINARY_0 = b"Hello world!"
print(BINARY_0[0])

## encode e decode da/a bin a/da string
print("\r\n## encode e decode da/a bin a/da string")
BINDECODED_TO_STRING = BINARY_0.decode()
print(BINDECODED_TO_STRING[0])
STRING_ENCODED_TO_BIN = BINDECODED_TO_STRING.encode()
print(STRING_ENCODED_TO_BIN[0])

## split e join
print("\r\n## split e join")
STRING_SPLITTED = STR_0.split(" ")
print(STRING_SPLITTED)
COMMA_IN_JOIN = ", "
STR2 = "alpha"
STR3 = "beta"
STR4 = "gamma"
STR_JOINED = COMMA_IN_JOIN.join([STR2, STR3, STR4])
print(STR_JOINED)
#### secondo test
print("#### secondo test")
STR5 = "this string\r\n has many\t\tspace"
print(STR5)
print(STR5.split())
print(" ".join(STR5.split()))

## find e count
print("\r\n## find e count")
INDICE_MANY_IN_STR5 = STR5.find("many") ## -1 se non trovato
print(INDICE_MANY_IN_STR5)
COIUNT_A_IN_STR5 = STR5.count('a')
print(COIUNT_A_IN_STR5)

## liste e set
print("\r\n## liste e set")
MY_LIST_1 = [i for i in range(10)]
MY_LIST_2 = [i for i in range(5)]
MY_LIST_1 = MY_LIST_1.__add__(MY_LIST_2)
print(MY_LIST_1)
#### rimuovere i duplicati da una list
MY_LIST_1 = list(set((MY_LIST_1)))
print(MY_LIST_1)

## dizionari: chiave, valore;
print("\r\n## dizionari: chiave, valore; ")
#### costruttore enumerate(seq) per creare un dizionario la cui chiave è il numero sequenziale
#### del rispettivo elemento nella lista
print("#### dizionari con costruttori enumerate")
SEQ_VALORI_1 = ["alpha", "beta", "gamma"]
DICT1 = dict(enumerate(SEQ_VALORI_1))
print(DICT1)
#### usare il costruttore zip(kseq,vseq) per creare un dizionario da una sequenza di chiavi, kseq,
#### e una sequenza di valori, vseq
print("#### dizionari con costruttori zip")
SEQ_CHIAVI_2 = "zxy"
SEQ_VALORI_2 = ["alpha2", "beta2", "gamma2"]
DICT2 = dict(zip(SEQ_CHIAVI_2, SEQ_VALORI_2))
print(DICT2)

## generatori di liste python: enumerate, zip, range
print("\r\n## generatori di liste: enumerate, zip, range")
print(enumerate(SEQ_VALORI_1))
ZIP_CHIAVI2_VALORI2 = zip(SEQ_CHIAVI_2, SEQ_VALORI_2)
print(ZIP_CHIAVI2_VALORI2)
print(range(10))
#### trasformazione di un generatore di liste in list
#### (un generatore di liste, produce l'elemento successivo solo su richiesta):
print("#### trasformazione di un generatore di liste in list")
print(list(enumerate(SEQ_VALORI_1)))
print(list(ZIP_CHIAVI2_VALORI2))
print(list(range(10)))

## manipolazione di liste
print("\r\n## manipolazione di liste")
LIST_INITIAL_1 = list(range(12))
LIST_ELABORATED_1 = [i for i in LIST_INITIAL_1] ## copia
print(LIST_ELABORATED_1)
LIST_ELABORATED_1 = LIST_INITIAL_1[:] ## copia più efficiente
LIST_ELABORATED_1 = LIST_INITIAL_1.copy() ## copia più efficiente
print(LIST_ELABORATED_1)
LIST_ELABORATED_2 = [i for i in LIST_INITIAL_1 if i >= 3] ## con condizione
print(LIST_ELABORATED_2)
LIST_ELABORATED_3 = [1/i for i in LIST_INITIAL_1 if i != 0] ## lista di reciproci
print(LIST_ELABORATED_3)
INFILE = open("02_file_to_read.txt", "r")
## prende tutte le righe non vuote dal file: INFILE:
LIST_ELABORATED_4 = [line for line in [line0.strip() for line0 in INFILE] if line]
print(LIST_ELABORATED_4)
INFILE.close()

## COUNTER
print("\r\n## COUNTER")
STR_TO_CNT = "my word1 my word2 and my word3"
ARRAY_TO_CNT = STR_TO_CNT.split()
COUNTER = Counter(ARRAY_TO_CNT)
ITEM_WITH_COUNT_VALUE_ARRAY = COUNTER.most_common()
#### restituisce una lista degli n elementi, o tutti se n non è specificata,
#### con le maggiori occorrenze (count)
print(ITEM_WITH_COUNT_VALUE_ARRAY)
#### conversione in dizionario (facilita le ricerche)
ITEM_WITH_COUNT_VALUE_DICT = dict(ITEM_WITH_COUNT_VALUE_ARRAY)
print(ITEM_WITH_COUNT_VALUE_DICT)
print("find value for item 'my': " + str(ITEM_WITH_COUNT_VALUE_DICT['my']))
print("find value for item 'my': {} ".format(ITEM_WITH_COUNT_VALUE_DICT['my']))

## gestione dei files
print("\r\n## gestione dei files")
with open("02_file_to_read.txt", mode="r") as FILE_1:
    DATI_1 = FILE_1.read() # legge tutti i dati come una stringa o dati binari
    print("FILE_1.read(): "+DATI_1)
N_BYTE = 10
with open("02_file_to_read.txt", mode="r") as FILE_1:
    DATI_1 = FILE_1.read(N_BYTE) # legge i primi n byte come una stringa o dati binari
    print("FILE_1.read(N_BYTE): "+DATI_1)
with open("02_file_to_read.txt", "r") as FILE_1:
    DATI_1 = FILE_1.readline() # legge la prossima riga come una stringa
    print("FILE_1.readline(): "+DATI_1)
with open("02_file_to_read.txt", "r") as FILE_1:
    DATI_1 = FILE_1.readlines() # legge tutte le righe come un array di stringhe
    print("FILE_1.readlines(): "+"-".join(DATI_1))
with open("02_file_to_write.txt", "w") as FILE_2:
    FILE_2.write("Prova scrittura .. "+DATI_1[2]) # scrive una stringa o dati binari
    FILE_2.writelines(DATI_1) # scrive una lista di stringhe
#### check
with open("02_file_to_write.txt", "r") as FILE_2:
    DATI_2 = FILE_2.read()
    print("FILE_2.read() after write operation: "+DATI_2)
