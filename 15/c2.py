import numpy
def ParseValues(filename):
    from functools import partial
    with open(filename) as filedata:
        data = filedata.read().splitlines()
    m = []
    for d in data:
        s = d.split()
        item = s[0].strip(':')
        vals = s[2], s[4],s[6],s[8],s[10]
        v2 = map(int,(s.strip(',') for s in vals))
        m.append(v2)
    mat = numpy.matrix(m).transpose()
    return mat

def GetTotal(mat,r):
    from operator import mul
    if any(t < 0.0 for t in r):
        print r
        raise Exception('bbq')
    res = numpy.dot(mat,r).tolist()[0]
    if any(r < 0.0 for r in res[:4]): return 0
    return reduce(mul,res[:4])

def GetNewPos(mat,r):
    E_i = GetTotal(mat,r)
    d = GetDerivative(mat,r)
    pos = LineSearch(mat,r,d)
    return pos, GetTotal(mat,pos) - E_i

def LineSearch(mat,r,direction):
    from itertools import count
#    print direction, r
    while True:
        r2 = Normalise(Sanitise(r + direction),1000.0)
        if GetTotal(mat,Sanitise(r+direction)) < GetTotal(mat,r):
            break
        r = r2
    return r
    

def GetDerivative(mat,r):
    from operator import mul
    from itertools import combinations
    res = numpy.dot(mat,r).tolist()[0]
    testvals = res[:4]
    total = reduce(mul,testvals)
    if total==0:
        print '.........ZERO TOTAL..........'
        return
    dervs = numpy.add.reduce([numpy.multiply(total/v, m) for v,m in zip(testvals,mat)]).tolist()[0]
    return FixDerv(dervs,0.1,r)
    
    
#    return r,total
def FixDerv(r,target,post):
    target = float(target)
    n = Normalise(r,target) - target/len(post)
    return n

def Sanitise(r):
    return [max(0,a) for a in r]

def Normalise(r,total):
    s = sum(r)
    return numpy.multiply(total / s, r)


import random

def tryget(target,m):

    num_elem = m.shape[1]
    t = Normalise([1.0] * num_elem,target)

    #Init to random that doesnt have 0 value....

    random.seed()

    while GetTotal(m,t) == 0.0:
        t = Normalise([random.random() for i in xrange(num_elem)],target)




    delta_e = 100000

    while(delta_e > 1):
        t, delta_e =  GetNewPos(m,t)
        print delta_e, sum(t)


    print math.log10(GetTotal(m,t)), 't'
    from math import floor, ceil
    from itertools import product

    totals = []

    for f in product([floor,ceil],repeat=num_elem):
        nv = [y(x) for y,x in zip(f,t)]
        if sum(nv) == target:
            totals.append((GetTotal(m,nv), nv))

    return max(totals)

        
import math
m = ParseValues('input-super.dat')


mv = tryget(1000.0,m)
print mv
print math.log10(mv[0])
print math.log10(156310812000)
print math.log10(213827871528)
print math.log10(189819811440)

print math.log10(GetTotal(m,[298,440,175,0,87,0]))
