#!/usr/bin/env python

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

### MAIN ###

print("Options:\n\
- a: addition\n\
- s: subtraction\n\
- m: multiplication\n\
- d: division")
op = input("Enter the letter corresponding to the operation you want to perform: ")

if op == "a":
	a = int(input("Enter the first addend: "))
	b = int(input("Enter the second addend: "))
	print("Result:", add(a, b))
elif op == "s":
	a = int(input("Enter the minuend: "))
	b = int(input("Enter the subtrahend: "))
	print("Result:", sub(a, b));
elif op == "m":
	a = int(input("Enter the first factor: "))
	b = int(input("Enter the second factor: "))
	print("Result:", mul(a, b));
elif op == "d":
	a = int(input("Enter the dividend: "))
	b = int(input("Enter the divisor: "))
	if b == 0:
		print("Error: you can't divide by zero!")
	else:
		print("Result:", div(a, b));
else: print("Error: operation not supported!")	
