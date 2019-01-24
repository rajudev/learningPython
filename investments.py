#!/usr/bin/env python3
amount = float(input("Enter amount: "))
interestRate = float(input("Enter Interest rate"))
period = int(input("Enter duration"))

value = 0
year = 1

while year <= period:
    value = amount + (interestRate * amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1
