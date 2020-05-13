#!/usr/bin/env python3
# File: solve2.py

def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totlegs = 4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                print('Number of pigs:' + str(numPigs) + ',',)
                print('Number of chickens:' + str(numChicks) + ',',)
                print('Number of spiders:', numSpiders)
                solutionFound = True
    if not solutionFound: print('There is no solution.')

def barnYard():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    return [legs, heads]

def main():
    barnYard()

if __name__ == '__main__':
    main()
