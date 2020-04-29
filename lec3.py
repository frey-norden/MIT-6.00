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
        print(ans)
        break
