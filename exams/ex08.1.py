#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:							# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex08.1.py ./work/directions1.txt")
	exit(-1)

try:
	f = open(sys.argv[1], "r")					# apertura file in lettura
except:
	print("ERRORE: apertura del file di input non riuscita!")
	exit(-1)

vert = 0
oriz = 0

for line in f:								# riempimento matrice
	L = line.split()
	if L[0] == 'N': vert += int(L[1])				# incrementa asse verticale
	elif L[0] == 'S': vert -= int(L[1])				# decrementa asse verticale
	elif L[0] == 'E': oriz += int(L[1])				# incrementa asse orizzontale
	elif L[0] == 'O': oriz -= int(L[1])				# decrementa asse orizzontale

f.close()

if vert != 0:
	if vert > 0:
		coordinate = 'N'
	else:
		coordinate = 'S'
		vert = abs(vert)
	print(vert, "METRI VERSO", coordinate)

if oriz != 0:
	if oriz > 0:
		coordinate = 'E'
	else:
		coordinate = 'O'
		oriz = abs(oriz)
	print(oriz, "METRI VERSO", coordinate)
