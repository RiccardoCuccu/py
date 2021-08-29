#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:							# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex09.py ./work/assembly.tic")
	exit(-1)

try:
	fin = open(sys.argv[1], "r")					# apertura file in lettura
except:
	print("ERRORE: apertura del file di input non riuscita!")
	exit(-1)

output_file=sys.argv[1]
output_file=output_file[:-3]+"toc"					# generazione del nome del file di output

try:
	fout = open(output_file, "w")					# apertura file in scrittura
except:
	print("ERRORE: apertura del file di output non riuscita!")
	exit(-1)

while(1):
	line = fin.readline()						# legge una riga alla volta
	if line == '': break						# se 'line' è vuota il file è terminato
	for ch in line:
		if ch == '#':
			if line[0] != '#': fout.write('\n')		# se il primo carattere di 'line' è diverso da '#' tornare a capo
			break
		else:
			fout.write(ch)					# copia il carattere sul file di output

fin.close()
fout.close()
