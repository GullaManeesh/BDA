#mapper 
#!usr/bin/env python3

import sys

for line in sys.stdin:
        year,temp = line.strip().split()
        print(f"{year}\t{temp}")



#-----------------------------
#reducer
#!usr/bin/env python3

import sys

current_year = None
max_temp = float('-inf')
for line in sys.stdin:
        year,temp = line.strip().split("\t")
        temp = int(temp)

        if current_year == year:

                max_temp =  max(temp,max_temp)
        else:
                if current_year:
                        print(f"{current_year},{max_temp}")

                current_year=year
                max_temp=temp

if current_year:
        print(f"{year},{max_temp}")



#---------
2010 32
2010 35
2011 30
2011 40
2012 28
2012 33
