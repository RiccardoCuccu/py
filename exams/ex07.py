#!/usr/bin/env python3

import sys

##### FUNCTION SAVECROSSWORD #####

def savecrossword(filename):
	try:
		f = open(filename, "r")					# apertura file in lettura
	except:
		print("ERRORE: apertura del file di input non riuscita!")
		exit(-1)

	N, M = f.readline().split()					# N righe e M colonne del file di input
	N = int(N)							# conversione da stringa ad intero (righe)
	M = int(M)							# conversione da stringa ad intero (colonne)
	Matrix = []							# inizializzazione matrice
	Row = []							# inizializzazione riga

	for line in f:							# riempimento matrice
		for char in line:
			if char == '\n': break
			Row.append(char)
		Matrix.append(Row)
		Row = []

	f.close()							# chiusura input file

	return Matrix, N, M

##### FUNCTION WRITEWORDS #####

def writewords(Matrix, N, M):
	try:
		f = open("./work/parole.txt", "w")			# apertura file in scrittura
	except:
		print("ERRORE: apertura del file di output non riuscita!")
		exit(-1)
	
	Word = []							# inizializzazione lista dei caratteri

	for n in range(N):						# ciclo esterno sulle righe
		for m in range(M):					# ciclo interno sulle colonne
			if Matrix[n][m] != ' ':				# se il carattere è diverso da uno spazio vuoto concatenalo alla lista Word
				Word.append(Matrix[n][m])
			elif len(Word) > 1:				# altrimenti se il numero di caratteri nella lista è superiore ad uno uniscili e stampali
				W = "".join(Word)
				f.write(W + '\n')
				Word = []
			else:						# se il numero di caratteri nella lista è inferiore a due scartali
				Word = []
		if len(Word) > 1:					# se alla fine della riga il numero di caratteri nella lista è superiore ad uno uniscili e stampali
			W = "".join(Word)
			f.write(W + '\n')
		Word = []						

	f.write('\n')							# riga vuota
	
	Word = []							# reset lista dei caratteri

	for m in range(M):						# ciclo esterno sulle colonne
		for n in range(N):					# ciclo interno sulle righe
			if Matrix[n][m] != ' ':				# se il carattere è diverso da uno spazio vuoto concatenalo alla lista Word
				Word.append(Matrix[n][m])
			elif len(Word) > 1:				# altrimenti se il numero di caratteri nella lista è superiore ad uno uniscili e stampali
				W = "".join(Word)
				f.write(W + '\n')
				Word = []
			else:						# se il numero di caratteri nella lista è inferiore a due scartali
				Word = []
		if len(Word) > 1:					# se alla fine della riga il numero di caratteri nella lista è superiore ad uno uniscili e stampali
			W = "".join(Word)
			f.write(W + '\n')
			Word = []

	f.close()							# chiusura output file

	return 0

##### MAIN #####

if len(sys.argv) != 2:							# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex07.py ./work/crossWord.txt")
	exit(-1)

Matrix, N, M = savecrossword(sys.argv[1])
writewords(Matrix, N, M)
