#!/usr/bin/env python3

class Square:

	def __init__(self, n):
		self.side = n

	def calculate_area(self):
		self.area = self.side * self.side

Q = Square(6)
Q.calculate_area()
print("Area:", Q.area)
