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
    if any(t < 0.0 for t in r): raise Exception('bbq')
    res = numpy.dot(mat,r).tolist()[0]
    if any(r < 0.0 for r in res[:4]): return 0
    return reduce(mul,res[:4])


def Normalise(r,total):
    s = sum(r)
    return numpy.multiply(total / s, r)


import random

def tryget(target,m,start=None):
    from itertools import combinations, permutations
    
    num_elem = m.shape[1]
    if (start is None):
        t = Normalise([1] * num_elem,target)
        t[2] += target - sum(t)
        print t, GetTotal(m,t)
    else:
        t = start


    de = 100
    while (de > 0):
        old_e = GetTotal(m,t)
        de = 0
        for x,y in permutations(xrange(num_elem),2):
            #Try this combination
            if (t[y] == 0):
                continue
            new_t = t.copy()
            new_t[x] += 1
            new_t[y] -= 1
            new_e = GetTotal(m,new_t)
            if (new_e > old_e):
                de = new_e - old_e
                t = new_t
                break

    print t, old_e
    return t
    
import math
m = ParseValues('input-super.dat')
t = tryget(100,m)
print sum(t)
t = tryget(1000,m,t*10)
print t, math.log10(GetTotal(m,t)), sum(t)
#print math.log10(mv[0])
print math.log10(156310812000)
print math.log10(213827871528)
print math.log10(189819811440)


