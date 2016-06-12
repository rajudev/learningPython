#!/usr/bin/env python3

N = 10  # Total numbers of whom the average is to be calculated
sum = 0 #sum of all the entered numbers
count = 0
print ("Enter Numbers:")
while count < N:
    number = float(input (""))
    sum = sum + number
    count = count + 1
average = float(sum)/N
print("N = %d , sum = %f" % (N, sum))
print("average = %f") % average
