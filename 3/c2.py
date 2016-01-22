from functools import reduce
from itertools import accumulate


with open("input.dat") as f:
    moves = f.read()
    
nSantas = 1
#print(len(reduce(set.union,(set(accumulate( {y:1j**x for x,y in enumerate('<^>v')}[p] for p in m)) for m in  (moves[i::nSantas] for i in range(nSantas))),{0})))
print(len(reduce(set.union,(set(accumulate( {symbol:1j**i for i,symbol in enumerate('<^>v')}[move] for move in move_set)) for move_set in  (moves[Sno::nSantas] for Sno in range(nSantas))),{0})))



