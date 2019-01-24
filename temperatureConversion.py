#!/usr/bin/env python3

#program to print the Fahrenheit to Celcius conversion table upto 250

fahrenheit = 0.0
print ("Fahrenheit Celcius")
while fahrenheit <= 250:
    celcius = (fahrenheit - 32.0 ) / 1.8  #Here we calculate the celcius value
    print ("%5.1f %7.2f" % (fahrenheit , celcius))
    fahrenheit = fahrenheit + 25
