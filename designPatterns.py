#!/usr/bin/env python3



rows = int(input("Enter the number of rows you want in the patterns: "))


# Design 1

x = rows
while x >= 0:
    print(x * "*")
    x -= 1


print("-------------------------")
# Design 2

m = rows
i = 1
while i <= m:
    print(i * "*")
    i += 1

print("-------------------------")


# Design 3

#import ipdb
#ipdb.set_trace()

y = rows
while y >= 0:
    a = y * "*"
    b = " " * (rows - y)
    print(b + a)
    y -= 1

print("-------------------------")
