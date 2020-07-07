#!/usr/bin/env python

def add():
	a = int(input("Enter the first addend: "))
	b = int(input("Enter the second addend: "))
	print("Result:", a+b)

def sub():
	a = int(input("Enter the minuend: "))
	b = int(input("Enter the subtrahend: "))
	print("Result:", a-b)

def mul():
	a = int(input("Enter the first factor: "))
	b = int(input("Enter the second factor: "))
	print("Result:", a*b)

def div():
	a = int(input("Enter the dividend: "))
	b = int(input("Enter the divisor: "))
	if b != 0:
		print("Result:", a/b)
	else:
		print("Error: you can't divide by zero!")

## MAIN ##

print("Options:\n\
- a: addition\n\
- s: subtraction\n\
- m: multiplication\n\
- d: division")
op = input("Enter the letter corresponding to the operation you want to perform: ")

if op == "a": add()
elif op == "s":	sub()
elif op == "m":	mul()
elif op == "d":	div()
else: print("Error: operation not supported!")	
