#!/usr/bin/env python3

import random

MAX_MATCHES = 5

def sfide(L, matches):								# calcolo del vincitore

	player1 = 0
	player2 = 0

	for i in range(matches):
		if L[i][2] == 't':						# se testa (t) vince il dado più alto
			if L[i][0] > L[i][1]: player1 += 1
			elif L[i][0] < L[i][1]: player2 += 1
		else:								# se croce (c) vince il dado più basso
			if L[i][0] > L[i][1]: player2 += 1
			elif L[i][0] < L[i][1]: player1 += 1

	if player1 > player2: return 1
	elif player1 < player2: return -1
	else: return 0

matches = random.randint(1, MAX_MATCHES)					# numero casuale di partite
L=[]

for i in range(matches):							# inizializzazione dell'array di partite con valori casuali
	if random.randint(0, 1) % 2 == 0: moneta = 't'
	else: moneta = 'c'

	L.append([random.randint(1, 6), random.randint(1, 6), moneta])
	print("Partita " + str(i+1) + ": " + str(L[i][0]) + "-" + str(L[i][1]) + "-" + str(L[i][2]))

winner = sfide(L, matches)							# calcolo del vincitore della partita tramite la funzione sfide()

if winner == 1: print("Ha vinto il Giocatore 1!")
elif winner == -1: print("Ha vinto il Giocatore 2!")
else: print("Parità!")
