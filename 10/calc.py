import cProfile
import itertools

def look_and_say(x):
    res = ""
    curval = x[0]
    number = 1
    for i in x[1:]:
        if (i==curval):
            number += 1
        else:
            res += str(number) + curval
            curval = i
            number = 1
    res += str(number) + curval
    return res

def start(x):
    return x[:20]

def noop(x):
    return x

def lsrange(data,n,operation):
    for i in xrange(1,max(n)+1):
        data = look_and_say(data)
        if i in n:
            print i,operation(data)






data = "1113222113"
targets = [40,50]
op = len

cProfile.run('lsrange(data,targets,op)')
