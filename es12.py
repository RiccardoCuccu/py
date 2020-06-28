#!/usr/bin/env python

def outer():
	x = "local"
	def inner():
		nonlocal x
		x = "nonlocal"
		print("Inner:", x)	# Inner: nonlocal
	inner()
	print("Outer:", x)		# Outer: nonlocal

outer()