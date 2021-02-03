#!/usr/bin/env python3

import sys

##### FUNCTION STUDENTIFC #####

def studentifc(filename, year):

	try:									# apertura file in lettura
		f = open(filename, "r")						
	except:
		return -1
	
	if int(year) < 1 or int(year) > 5:					# controllo sul limite di anni
		return -1

	counter = 0								# inizializzazione numero studenti fuori corso

	for line in f:
		L1 = line.split(',')						# divisione della riga tramite virgola
		L2 = L1[2].split()						# divisione del terzo elemento della riga tramite spazio
		if L2[0] == year and L2[1] == "FC": counter += 1		# contollo sull'anno e sullo status dello studente

	return counter

##### MAIN #####

if len(sys.argv) != 3:								# controllo del numero di parametri passati alla funzione
	print("ERRORE: numero di parametri errato!")
	print("Esempio di utilizzo: ./ex03.py ./work/exambooking.txt 2")
	exit(-1)

n = studentifc(sys.argv[1], sys.argv[2])					# calcolo degli studenti fuori corso

if n == -1: print("Il nome del file inserito e/o il valore dell'anno di corso non è valido!")
else: print("Il numero di studenti fuori corso per l'anno " + sys.argv[2] + " è pari a " + str(n) + ".")
