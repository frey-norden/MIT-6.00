#!/usr/bin/env python3
# File: solve2.py

def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totlegs = 4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return [numPigs, numChicks, numSpiders]
                solutionFound = True
    if not solutionFound: return [None, None, None]

def barnYard():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))

def main():
    solve2(numLegs, numHeads)

if __name__ == '__main__':
    main()
