#!/usr/bin/env python3
#calculate investments.

amount = float(input("Enter amount:"))
inrate = float(input("Enter rate of Interest:"))
period = int(input("Enter Period"))
value = 0
year = 1

while year <= period:
    value = amount + ( inrate * amount)
    print("Year %d Rs. %.2f" % (year,value))
    amount = value
    year = year + 1
