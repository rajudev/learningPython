#!/usr/bin/penv python3

s = input("Please input string:")

z = s[::-1]

if s == z:
    print("%s is palindrome" % s)
else:
    print("%s is not palindrome" % s)

