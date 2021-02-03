#!/usr/bin/env python3

filename = "./work/sums.txt"
eq = 0							# equal
ne = 0							# not equal

for line in open(filename, "r"):			# apertura file in lettura e suddivisione del file in righe
	elements = line.split(';')			# salvataggio degli elementi utili in elements[0]
	edges = elements[0].split('=')			# divisione dei due lati dell'uguaglianza
	e1 = edges[0].split('+')			# salvataggio in una lista dei numeri (sinistra)
	e2 = edges[1].split('+')			# salvataggio in una lista dei numeri (destra)
	e1 = sum(list(map(int, e1)))			# conversione dei numeri da stringhe ad interi, assegnazione del risultato ad una lista e somma dei suoi elementi (sinistra)
	e2 = sum(list(map(int, e2)))			# conversione dei numeri da stringhe ad interi, assegnazione del risultato ad una lista e somma dei suoi elementi (destra)
	if e1 == e2: eq += 1				# comparazione
	else: ne +=1

total = eq + ne						# numero totale di uguaglianze
perc = (eq / total) * 100				# percentuale di uguaglianze corrette

print("La percentuale di uguaglianze corrette è del {:.0f}%!".format(perc))
