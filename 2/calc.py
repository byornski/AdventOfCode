from operator import mul
from itertools import combinations

def paper_needed(dim):
    sides = [reduce(mul,comb) for comb in combinations(dim,2)]
    return 2*sum(sides) + min(sides)
    
def ribbon_needed(dim):
    dim.sort()
    return 2 * sum(dim[:2]) + reduce(mul,dim)

with open("input.dat") as dat:
    data = dat.read().splitlines()

dims =  [map(int,s.split("x")) for s in data]
print sum(map(paper_needed,dims)), sum(map(ribbon_needed,dims))
