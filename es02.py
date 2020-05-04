#!/usr/bin/env python

w = "spam"

for l in w:
	print(w, end=' ')
	w = w[1:] + w[0]
