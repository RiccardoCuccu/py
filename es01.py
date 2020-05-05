#!/usr/bin/env python

D = {'a': 1, 'c': 3, 'b': 2}

#for i in list(range(4)):
#	for j in ['a', 'b', 'c']:
#		if D[j] == i:
#			print(j + " => " + str(D[j]))

for (key, value) in (sorted(D.items())):
	print(key, ' => ', value)
