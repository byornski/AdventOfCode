import numpy as np
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
    mat = np.matrix(m).transpose()
    return mat

def ZeroMin(x):
    return max(0,x)

zm = np.vectorize(ZeroMin)

def GetValue(x,mat):
    from operator import mul
    res =  np.array(zm(mat.dot(x))).reshape(-1)
    if not res[-1]==500: return 0
    return reduce(mul,res[:4])



def ToTrial(comb):
    sumv = 0
    Trial = []
    for v in comb[:]:
        Trial.append(v - sumv)
        sumv = v
    Trial.append(totalvalue - v)
    return Trial

totalvalue = 100
d = ParseValues('input.dat')
num_vars = d.shape[1] - 1

#from itertools import combinations_with_replacement as cwr
from itertools import combinations as cwr
combs = cwr(xrange(totalvalue),num_vars)

Trials = (ToTrial(c) for c in combs)

res = ((GetValue(t,d),t) for t in Trials)

print max(res)



#GetValue(trial,d)
