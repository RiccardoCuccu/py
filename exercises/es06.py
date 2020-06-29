#!/usr/bin/env python

import os

for file in os.listdir():
	if file.endswith(".c") or file.endswith(".h"):
		print(file)