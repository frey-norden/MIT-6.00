#!/usr/bin/env python3
# File: ps1a.py
# Problem Set 1
# Name: Frey Norden
# Collaborators: -
# Time:


def primeTest(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


n = input('Enter number for nth prime: ')
n = int(n)
#print(primeTest(n))
#n = 999
x = 10000
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

# print output
nth_prime = primeints[n-1]
#print(primeints)
print(nth_prime)
