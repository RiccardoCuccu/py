#!/usr/bin/env python

x=99					# global variable

def f1():
	x = 88				# local variable
	def f2():
		print("f2:", x)		# 88
	f2()
	print("f1:", x)			# 88

f1()
print("f0:", x)				# 99