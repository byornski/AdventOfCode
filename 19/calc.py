# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:04:36 2015

@author: byo
"""
from collections import defaultdict

def GetMatches(v,string):
    import re
    return [m.start() for m in re.finditer(v,string)]
    
def ReplaceAt(pos,i,f,string):
    ilen = len(i)
    return string[:pos] + f + string[pos+ilen:]


ReplaceAt(2,"x","hello","thxs is a long string")

deadends = set()

def DepthSearch(string,repls,depth=1):
    for k in sorted(repls,key=len,reverse=True):
        matches = GetMatches(k,string)
        for m in matches:
            newstring = ReplaceAt(m,k,repls[k],string)
            if newstring not in deadends:
                i = DepthSearch(newstring,repls,depth+1)
                if (i > 0):
                    return i
            if newstring == "e":
                return depth
    #Didnt work... add to deadends:
    #print string
    deadends.add(string)
    return 0
        
    


def Readfile(filename):
    with open(filename) as fd:
        data = fd.read().splitlines()

    replacements = defaultdict(list)
    for line in data:
        if line:    
            if "=>" in line:
                #is a replacement
                i,f =  line.split()[::2]
                replacements[i].append(f)
            else:
                initial = line.strip()
    return initial, replacements
        
string, repls = Readfile("input.dat")

finals = set()
#print string
for i in repls:
    #print i, repls[i]
    matches =  GetMatches(i,string)
    for f in repls[i]:
        for m in matches:
            finals.add(ReplaceAt(m,i,f,string))
            
print 'Calibration ', len(finals)


#Try reversing process


reverseReplacement = defaultdict(str)
#First invert dict
for i in repls:
    for f in repls[i]:
        reverseReplacement[f] = i

target = string
newvals = {target}
print "start:", target

DepthSearch(target,reverseReplacement)




