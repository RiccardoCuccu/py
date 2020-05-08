#!/usr/bin/env python

import random

def symbolDefInit():
	global val
	global syb

	val = [
		1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1
		]

	syb = [
		"M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
		]

def generateRandomInteger():
	n = random.randint(0, 2000)
	return n

def conversionToRoman(intNum):
	roman_numeral = ''
	for i in range(0, len(val)):
		value = int(intNum / val[i])
		intNum = intNum % val[i]
		roman_numeral += value*syb[i]
	return roman_numeral

### MAIN ###

symbolDefInit()

for i in range(0,20):
    x = generateRandomInteger()
    y = conversionToRoman(x)
    print('%d is %s' % (x, y))

