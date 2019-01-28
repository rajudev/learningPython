#!/usr/bin/env python3

j,k = 0,1

while k < 100000000000000000000:
    print(k, end=' | ')
    j,k = k, j + k
