#!/usr/bin/env python

print("1) read()")					# reads the whole file and converts it to a string
f=open("./work/main.c")					# default mode, it opens file for reading
print(f.read(), end='\n\n')
f.close()

print("2) readline()")					# reads one line at a time and returns it as a string
f=open("./work/main.c")					# default mode, it opens file for reading
n_lines = len(open("./work/main.c").readlines())
for line in range(0,n_lines):
	print(f.readline(), end='')
print(end='\n\n')
f.close()

print("3) readlines()")					# reads the whole file and returns the lines as a list of strings
f=open("./work/main.c")					# default mode, it opens file for reading
for line in f.readlines():
	print(line, end='')
print(end='\n')
f.close()
