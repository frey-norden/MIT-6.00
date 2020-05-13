#!/usr/bin/env python3
# File: ch3.py
# example looking at incrementing floats w/ a loop

x = 0.0
for i in range(10):
    x += 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')

# square root of 2 rounded to 3 digits
x1 = round(2**0.5, 3)
print(x1)

r = int(input('How many decimal places? '))
# now 5 decimal places
x2 = round(2**0.5, r)
print(x2)
