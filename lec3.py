#!/usr/bin/python3
# File: lec3.py

x = 25
ans = 0
if x >= 0:
    while ans * ans < x:
        ans += 1
        #print('ans =', ans)
    if ans * ans != x:
        print(x, 'is not a perfect square.')
    else: print(ans)
else: print(x,'is a negative number.')

print('\n')
# find the divisors of given number, x
x = 10
i = 1
while i<x:
    if x%i == 0:
        print('divisor ',i)
    i += 1
print('\n')
# find divisors with for loop
x = 10
for i in range(1,x):
    if x%i == 0:
        print('divisor ',i)

print('\n')
x = 1515361
if x>=0:
    for ans in range(1,x):
        if ans*ans == x:
            print(ans)
            break

print('\n')
x = 100
divisors = ()
for i in range(1, x):
    if x%i == 0:
        divisors = divisors + (i,)
print(divisors)

print('\n')
# strings as ordered sequence of characters
s1 = 'abcdefg'
s2 = 'hijklmn'

print(s1 + s2)

print(s1)
print(s1[0])
print(s1[3])
print(s1[-1])
print(s1[2:4])
# up to but not including 5 for example
print(s1[:5])
print(s1[3:])

# searching chars w find() func
print(s1.find('cde'))
print('\n')
print('now string comparisons')
print(s1 == s1)
print(s1 == s2)
print(s1 < s2)
print(s1 > s2)

print('\n')
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print(sumDigits)
