#!/usr/bin/env python

s = "abcdefghijk"

for i in range(0, len(s), 2):		# odd elements
	print(s[i], end=' ')		# print using the index
print(end='\n')

for n in s[1::2]:			# even elements
	print(n, end=' ')		# print using the character
print(end='\n')