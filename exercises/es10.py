#!/usr/bin/env python

from datetime import datetime

old_date='2018-05-12'
y=datetime.strptime(old_date, '%Y-%m-%d')
z=datetime.now()
difference=z-y
print(difference, end='\n')