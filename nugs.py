# Name: Frey Norden
# Collaborators: -
# Time: 1:30
# returns solutions to number of 6,9,20 piece mcNuggets that equal totals in range 50 t0 100

def mcNuggets(a, b, c, total):
    solutionFound = False
    x = 6*a + 9*b + 20*c
    if x == total:
        #print(total, [a, b, c], 'solution')
        solutionFound = True
    if solutionFound == True:
        print(total, [a, b, c], 'solution')


def order():
    u = int(input('Enter upper limit of nuggets: '))
    l = int(input('Enter lower limit of nuggets: '))
    for x in range(0,int(u/6+1)):
        for y in range(0,int(u/9+1)):
            for z in range(0,int(u/20+1)):
                for total in range(l,u+1):
                    mcNuggets(x, y, z, total)

def main():
    order()

if __name__ == '__main__':
    main()
