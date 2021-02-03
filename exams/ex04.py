#!/usr/bin/env python3

import random

MAX_VECTORS = 5

def segmenti(L, vectors):

	D = {'1': 0, '2': 0, '3': 0, '4': 0}

	for i in range(vectors):
		if (L[i][0][0] > 0) and (L[i][1][0] > 0) and (L[i][0][1] > 0) and (L[i][1][1] > 0): D['1'] += 1			# x positivi e y positivi (I quadrante)
		elif (L[i][0][0] < 0) and (L[i][1][0] < 0) and (L[i][0][1] > 0) and (L[i][1][1] > 0): D['2'] += 1		# x negativi e y positivi (II quadrante)
		elif (L[i][0][0] < 0) and (L[i][1][0] < 0) and (L[i][0][1] < 0) and (L[i][1][1] < 0): D['3'] += 1		# x negativi e y negativi (III quadrante)
		elif (L[i][0][0] > 0) and (L[i][1][0] > 0) and (L[i][0][1] < 0) and (L[i][1][1] < 0): D['4'] += 1		# x negativi e y negativi (IV quadrante)

	return max(D, key=D.get)									# in caso di pareggio viene considerato il quadrante con l'indice minore


vectors = random.randint(1, MAX_VECTORS)								# numero casuale di vettori
N = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]									# valori di x e y ammessi
L = []

for i in range(vectors):										# inizializzazione dell'array di coordinate
	L.append([[random.choice(N), random.choice(N)], [random.choice(N), random.choice(N)]])
	print("Segmento " + str(i+1)) 
	print("- Coordinate primo punto\t Re: " + str(L[i][0][0]) + "\t Im: " + str(L[i][0][1]))	# z = x + iy
	print("- Coordinate secondo punto\t Re: " + str(L[i][1][0]) + "\t Im: " + str(L[i][1][1]))	# z = x + iy
	print(''.rjust(80,'-'))										# graphic divider

q = segmenti(L, vectors)										# calcolo del quadrante più popolato

print("Il quadrante che include il più alto numero di segmenti interi è il numero " + q + "!")
