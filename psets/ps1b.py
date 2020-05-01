#!/usr/bin/env python3
# File: ps1b.py
# Problem Set 1 problem 2
# Name: Frey Norden
# Collaborators: -
# Time: 0:30
#computes the sum of log(prime) in range(2,n-1) - Enjoy!
"""
There is a cute result from number theory that states that for sufficiently
large n the product of the primes less than n is less than or equal to e**n
and that as n grows, this becomes a tight bound (that is, the ratio of the
product of the primes to e**n gets close to 1 as n grows).
"""

import math

def primeTest(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

n = input('Enter number for nth prime: ')
n = int(n)

x = (n * 10)
oddints = []
primeints = []

# generate list of candidate ints
for num in range(1,x):
    if num%2 != 0:
        oddints.append(num)
        #print(num)

# test candidate if prime
for i in oddints:
    if primeTest(i) == True:
        primeints.append(i)

sum = 0

for j in primeints[:n-1]:
    sum += math.log(j)
    ratio = sum/j
    print(sum,j,ratio)
