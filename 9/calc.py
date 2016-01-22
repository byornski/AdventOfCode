from collections import defaultdict
import itertools
import operator

def printval(x):
    print " => ".join(x[0]), " = ", x[1]

def calculate_length(towndata,order):
    return sum(towndata[a][b] for a,b in zip(order, order[1:]))
    
def findminmax(filename):

    with open(filename) as filedata:
        data = filedata.read().splitlines()

    towns = defaultdict(dict)

    for d in data:
        tstr,dist = d.split(" = ")
        t1,t2 = tstr.split(" to ")   
        towns[t1][t2] = towns[t2][t1] = int(dist)

    # avoid counting 1,2,3 and 3,2,1
    l = [(i,calculate_length(towns,i)) for i in itertools.permutations(towns) if i[0] < i[-1]]

    #Faster to do this than a python loop...
    printval(min(l,key=operator.itemgetter(1)))
    printval(max(l,key=operator.itemgetter(1)))

    

findminmax("input.dat")
#cProfile.run('''findminmax("input.dat")''')
    

    
