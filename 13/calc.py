from collections import defaultdict
from itertools import permutations
from operator import itemgetter


def total_value(permut,pot):
    sum = 0
    for i,j in zip(permut,permut[1:]+(permut[0],)):
        if i in pot and j in pot:
            sum += pot[i][j] + pot [j][i]
    return sum

def perform(p1 = None):

    with open('input.dat') as filedata:
        data = filedata.read().splitlines()

        pot = defaultdict(dict)
    
    
        for d in data:
            d = d.split()
            person,gain,value,target =  d[0], 'gain' in d[2],int(d[3]), d[-1].strip('.')
            if not gain:
                value = -value
            pot[person][target] = value
                
        if p1 is None:
            p1 = min(pot)
        reduced_people = [p for p in pot if p is not p1]

        valuepairs = []

        for permut in permutations(reduced_people):
            permut = (p1,) + permut
            #    x = (permut, total_value(permut,pot))
            valuepairs.append(total_value(permut,pot))

        print max(valuepairs)


perform()
perform('byo')

