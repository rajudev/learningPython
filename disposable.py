#!/usr/bin/env python3
# Program to calculate days into months and days

try:
    days = 0
    days = int(input("Enter Days"))
    # months = days / 30
    # days = days % 30
    # print(f"Months = {months} and Days = {days}")

    # trying the divmod approach
    print("Months = %d Days = %d" % (divmod(days, 30)))

except:
    print("Please enter only integers, no alphabets or symbols")

