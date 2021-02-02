#!/usr/bin/env python3

import sys

def converter(n):									# conversione in numero

	if n == "zero": ret = '0'
	elif n == "uno": ret = '1'
	elif n == "due": ret = '2'
	elif n == "tre": ret = '3'
	elif n == "quattro": ret = '4'
	elif n == "cinque": ret = '5'
	elif n == "sei": ret = '6'
	elif n == "sette": ret = '7'
	elif n == "otto": ret = '8'
	elif n == "nove": ret = '9'
	else: 
		print("ERRORE: non è possibile decodificare il valore " + n)
		sys.exit(1)

	return ret

filename = input("Inserire il nome del file da analizzare: ")
#filename = "./work/stringnum.txt"

sum=0
S=""

for line in open(filename, "r"):							# apertura file in lettura e suddivisione del file in righe
	numbers = line.split()								# suddivisione della riga in parole
	for n in numbers:
		if n == "stop":								# se n contiene "stop"
			sum = sum + int(S)						# conversione in intero e somma con i valori precedenti
			S=""								# reset della variabil S
			break
		else:
			S = S + converter(n)						# decodifica e concatena il nuovo numero

print("Somma = " + str(sum))								# stampa della somma
