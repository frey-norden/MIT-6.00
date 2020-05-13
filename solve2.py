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

def barnYard1():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens, spiders = solve2(legs, heads)
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
