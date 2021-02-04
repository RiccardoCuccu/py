#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:							# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex08.2.py ./work/directions1.txt ./work/revdirections1.txt")
	exit(-1)

try:
	f = open(sys.argv[1], "r")					# apertura file in lettura
except:
	print("ERRORE: apertura del file di input non riuscita!")
	exit(-1)

C = []									# coordinate
M = []									# metri

for line in f:								# inversione delle coordinate
	L = line.split()
	if L[0] == 'N': C.append('S')
	elif L[0] == 'S': C.append('N')
	elif L[0] == 'E': C.append('O')
	elif L[0] == 'O': C.append('E')
	M.append(L[1])

f.close()

try:
	f = open(sys.argv[2], "w")					# apertura file in scrittura
except:
	print("ERRORE: apertura del file di output non riuscita!")
	exit(-1)

for x, y in zip(reversed(C), reversed(M)):				# scrittura in ordine inverso
	f.write("%s %s\n" % (x, y))

f.close()
