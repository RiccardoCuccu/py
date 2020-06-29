#!/usr/bin/env python

import random

def symbolDefInit():
	global val
	global syb

	val = [						# table of values
		1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1
		]

	syb = [						# table of symbols
		"M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
		]

def generateRandomInteger():				# random integer generator
	n = random.randint(0, 2000)
	return n

def conversionToRoman(intNum):				# converter to roman numerals
	roman_numeral = ''
	for i in range(0, len(val)):			# cycle through the whole table of values
		value = int(intNum / val[i])		# calculates how many times val[i] can fit inside the number considered
		intNum = intNum % val[i]		# calculate the reminder
		roman_numeral += value*syb[i]		# append the corresponding symbol for the calculated number of occurrences
	return roman_numeral

### MAIN ###

symbolDefInit()

for i in range(0,20):
    x = generateRandomInteger()
    y = conversionToRoman(x)
    print('%d is %s' % (x, y))

