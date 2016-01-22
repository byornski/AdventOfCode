# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:32:38 2015

@author: byo
"""



def ReadJugs(filename):
    with open(filename) as fd:
        data = fd.read().splitlines()
    jugs = [int(j) for j in data]
    return jugs
    
jugs = ReadJugs("input.dat")

target = 150

from itertools import product
import numpy

jugsets = []

for p in product([0,1],repeat=len(jugs)):
    used = numpy.multiply(p,jugs)
    if numpy.add.reduce(used)==target:
        jugsets.append(p)
        

print len(jugsets)
jugsums = [sum(p) for p in jugsets]

minsum = min(jugsums)

print sum(1 for p in jugsums if p==minsum)


