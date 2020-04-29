#!/usr/bin/env python3
# File: runninpython.py

x = 15
y = 5
z = 11
print(x,y,z)
#Is this right?
if x < y:
    if x < z: print('x is least')
    else: print('z is least')
else: print('y is least')

print('now we illustrate the bug in the branching')

x = 15
y = 13
z = 11
print(x,y,z)
#Is this right? Ans- no, there is a bug.
if x < y: 
    if x < z: print('x is least')
    else: print('z is least')
else: print('y is least')

print('\n', "now we see a better branching structure")

if x < y and x < z: print('x is least')
elif y < z: print('y is least')
else: print('z is least')
