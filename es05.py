#!/usr/bin/env python

n = input("Enter a number and i will tell you if it is a prime number: ")

try:
	n = int(n)
except:
	print("This is not a number!")
else:

	if n < 0:
		print("Number entered less than zero.")
	elif n == 0:
		print("Number entered equal to zero.")
	else:
	
		div = 2
		count = 0
	
		while div <= n/2 and count==0:
			if n%div==0:
				count+=1
			div+=1
	
		if count==0:
			print("%d is a prime number! :D" % n)
		else:
			print("%d in not a prime number! :(" % n)
