#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:							# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex06.py ./work/bitmapin.txt ./work/bitmapout.txt")
	exit(-1)

try:
	fin = open(sys.argv[1], "r")					# apertura file in lettura
except:
	print("ERRORE: apertura del file di input non riuscita!")
	exit(-1)

try:
	fout = open(sys.argv[2], "w")					# apertura file in scrittura
except:
	print("ERRORE: apertura del file di output non riuscita!")
	exit(-1)

N, M = fin.readline().split()						# N righe e M colonne del file di input
N = int(N)								# conversione da stringa ad intero (righe)
M = int(M)								# conversione da stringa ad intero (colonne)
fout.write("%d %d\n" % (N+2, M+2))					# scrittura della prima riga del file di output

for m in range(M+2):
	fout.write("255 255 255\n")					# scrittura prima riga matrice (pixel neri)

for n in range(N):
	fout.write("255 255 255\n")					# scrittura prima colonna matrice (pixel neri)
	for m in range(M):
		R, G, B = fin.readline().split()			# estrazione del valore dei pixel
		BN = (int(R) + int(G) + int(B)) / 3			# conversione in b/n
		fout.write("%d %d %d\n" % (BN, BN, BN))			# scrittura pixel intermedi
	fout.write("255 255 255\n")					# scrittura ultima colonna matrice (pixel neri)

for m in range(M+2):
	fout.write("255 255 255\n")					# scrittura ultima riga matrice (pixel neri)

fin.close()
fout.close()
