#!/usr/bin/env python

s = input("Enter a string of characters: ")
#s = "abcdefgabc"
D = {}

#for char in s:
#	if char not in D.keys():
#		D[char] = 1
#	else:
#		D[char] += 1

for char in s:
	D[char] = D.get(char, 0)+1		# return 0+1 if the key is not found

for (key, value) in sorted(D.items()):		# print the list in alphabetical order
	print(key + ',' + str(value))
