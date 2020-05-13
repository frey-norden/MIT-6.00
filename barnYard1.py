#!/usr/bin/env python3
# File: barnYard1.py

def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads -numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return [numPigs, numChicks, numSpiders]
    return [None, None, None]

def barnYard1():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs:', pigs)
        print('Number of chickens:', chickens)
        print('Number of spiders:', spiders)

def main():
    barnYard1()

if __name__ == '__main__':
    main()
