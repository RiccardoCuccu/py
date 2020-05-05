#!/usr/bin/env python

s = "abcdefgabc"
D = {}

for char in s:
	if char not in D.keys():
		D[char] = 1
	else:
		D[char] += 1

for (key, value) in D.items():
	print(key + ',' + str(value))
