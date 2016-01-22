from operator import add

direction = { 'v':(0,1),
              "^":(0,-1),
              "<":(-1,0),
              ">":(1,0)
}

def visited(movs):
    pos = [0,0]
    for mov in movs:
        pos = map(add,pos,direction[mov])
        yield tuple(pos)

with open("input.dat") as f:
    moves = f.read()
    
nSantas = 2
move_sets = (moves[i::nSantas] for i in range(nSantas))
all_visited = reduce(set.union,(set(visited(m)) for m in  move_sets),{(0,0)})
print len(all_visited)


