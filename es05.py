#!/usr/bin/env python

n = input("Enter a number and I will tell you if it is a prime number: ")

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
	
		div = 2							# set the first divisor
		flag = 0						# set the flag to zero
	
		while div <= n/2 and flag==0:				# as long as the divisor is smaller than half the number entered and flag = 0
			if n%div==0:					# if a divisor has been found that gives zero remainder
				flag+=1					# set the flag to one (the number entered is not a prime number)
			div+=1						# increase the divisor
	
		if flag==0:
			print("%d is a prime number! :D" % n)
		else:
			print("%d in not a prime number! :(" % n)
