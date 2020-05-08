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

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if op == "a":
	print("Result:", add(a, b))
elif op == "s":
	print("Result:", sub(a, b));
elif op == "m":
	print("Result:", mul(a, b));
elif op == "d":
	print("Result:", div(a, b));
else: print("Error: operation not supported!")	
