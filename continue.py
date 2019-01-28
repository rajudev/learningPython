#!/usr/bin/env python3

while True:
    n = int(input("Enter the number"))
    if n < 0:
        print("number is negative")
        continue
    elif n == 0:
        print("number is equal to 0")
        break
    print("square is ", n ** 2)
