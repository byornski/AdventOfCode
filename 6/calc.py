def mov(pos,d):
    return [x+y for x,y in zip(pos,d)]


def getset(s,e):
    return ((x,y) for x in xrange(s[0],e[0]+1) for y in xrange(s[1],e[1]+1))


def toggle(grid,pos):
    d =  {"x":"o","o":"x"}
    grid[pos[0]][pos[1]] = d[grid[pos[0]][pos[1]]]

def change_brightness(grid,pos,setting):
    grid[pos[0]][pos[1]] = max(grid[pos[0]][pos[1]] + setting,0)
    

    
    
def turn(grid,pos,setting):
    grid[pos[0]][pos[1]] = setting


def grepcommand(grid,cmd):
    s = cmd.split()
    if "turn on" in cmd:
        p1 = map(int,s[2].split(","))
        p2 = map(int,s[4].split(","))
        for p in getset(p1,p2):
#            turn(grid,p,"x")
            change_brightness(grid,p,1)
    elif "toggle" in cmd:
        p1 = map(int,s[1].split(","))
        p2 = map(int,s[3].split(","))
        for p in getset(p1,p2):
            change_brightness(grid,p,+2)
            #            toggle(grid,p)        
    elif "turn off" in cmd:
        p1 = map(int,s[2].split(","))
        p2 = map(int,s[4].split(","))
        for p in getset(p1,p2):
            change_brightness(grid,p,-1)
#            turn(grid,p,"o")        
    else:
        print "fail", s


def printgrid(grid):
    for i in grid:
        print " ".join(i)
    print '\n'
        

size = 1000
        
with open("input.dat") as filedata:
    data = filedata.readlines()

grid = [[0]*size for x in xrange(size)]

for d in data:
    grepcommand(grid,d)

print len([t for l in grid for t in l if t=="1"])
print sum(sum(l) for l in grid)
