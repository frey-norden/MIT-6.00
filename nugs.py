# Name: Frey Norden
# Collaborators: -
# Time: 1:30
# returns solutions to number of 6,9,20 piece mcNuggets that equal totals in range 50 t0 100

def mcNuggets(a, b, c, total):
    solutions = list()
    solutionFound = False
    x = 6*a + 9*b + 20*c
    if x == total:
        #return [a, b, c]
        print('solution',[a, b, c], total)
        solutionFound = True
    #if solutionFound == True:
        #solutions.append([a, b, c, total])
    #else:
        #print('no solution',total)
    #if not solutionFound: print('no solution')
    #print(solutions)

def cashier():
    u = int(input('Enter upper limit of nuggets: '))
    l = int(input('Enter lower limit of nuggets: '))
    for x in range(0,int(u/6+1)):
        for y in range(0,int(u/9+1)):
            for z in range(0,int(u/20+1)):
                for total in range(l,u+1):
                    mcNuggets(x, y, z, total)

def main():
    cashier()

if __name__ == '__main__':
    main()
