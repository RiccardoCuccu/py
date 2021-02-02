#!/usr/bin/env python3

import sys

def converter(n):
	if n == "zero": ret = 0
	elif n == "uno": ret = 1
	elif n == "due": ret = 2
	elif n == "tre": ret = 3
	elif n == "quattro": ret = 4
	elif n == "cinque": ret = 5
	elif n == "sei": ret = 6
	elif n == "sette": ret = 7
	elif n == "otto": ret = 8
	elif n == "nove": ret = 9
	else: 
		print("ERRORE: non è possibile decodificare il valore " + n)
		sys.exit(1)
	return ret

filename = input("Inserire il nome del file da analizzare: ")
#filename = "./work/stringnum.txt"

result=0
S=""

for line in open(filename, "r"):
	numbers = line.split()
	for n in numbers:
		if n == "stop":
			result = result + int(S)
			S=""
			break
		else:
			S = S + str(converter(n))

print("Somma = " + str(result))
