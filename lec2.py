#!/usr/bin/env python3
# File: lec2.py //MIT 6.00 Fall 2008

x = 15
if (x/2)*2 == x:
  print('Even')
else: print('Odd')

y = 0
x = 3
itersLeft = x
while(itersLeft>0):
    y = y + x
    itersLeft -= 1
    #print('y =',y,',itersLeft=',itersLeft)
print(y)

print('\n')

# find the square root of a perfect square
x = 16
ans = 0
while ans*ans <= x:
    ans += 1
print(ans)
