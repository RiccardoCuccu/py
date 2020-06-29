#!/usr/bin/env python

import os

files=os.listdir('./work')							# get the list of files in the "work" directory
files.sort()									# sort files alphabetically
new_files=[]
for i in files:									# search .c and .h files
	if ".c" in i:
		new_files.append(i)
	elif ".h" in i:
		new_files.append(i)

if not files:									# if files is empty
	print("There are no files in the 'work' directory")
else:
	print("Files in the 'work' directory:")
	for i in files:
		print("--", i)

if not new_files:								# if new_files is empty
	print("There are no .c or .h files in the 'work' directory")
else:	
	print("Files .c and .h in the 'work' directory:")
	for i in files:
		print("--", i)