
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

for x in range(0,10):
    for y in range(0,10):
        for z in range(0,6):
            for total in range(50,101):
                mcNuggets(x, y, z, total)
