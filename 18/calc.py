# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:58:20 2015

@author: byo
"""
from __future__ import print_function

import numpy
import itertools

def ReadInitial(filename):
    parse = {'.':0, '#':1}
    with open(filename) as fd:
        data = fd.read().splitlines()
    grid = []
    for d in data:
        row = []
        for c in d:
            row.append(parse[c])
        grid.append(row)
    return numpy.lib.pad(grid,1,'constant',constant_values=(0))

def PrintGrid(grid,doparse=True):
    parse = {0:".",1:"#"}
    grid_size = len(grid) - 2
    for i in xrange(1,grid_size + 1):
        for j in xrange(1,grid_size + 1):
            p = parse[grid[i,j]] if doparse else grid[i,j]
            print(p,end="")
        print()
    print()

def NextStep(grid):
    grid_size = len(grid) - 2

    neighbours = numpy.zeros_like(grid)
    for x,y in itertools.product([-1,0,1],repeat=2):
        if (x,y) != (0,0):
            neighbours +=  numpy.roll(numpy.roll(grid,x,axis=0),y,axis=1)
    
    for i in xrange(1,grid_size + 1):
        for j in xrange(1,grid_size + 1):
            if grid[i,j]==1:
                grid[i,j] = 1 if neighbours[i,j] in [2,3] else 0
            else:
                grid[i,j] = 1 if neighbours[i,j] == 3 else 0
    return grid
    
def TurnCornersOn(grid):
    grid_max = len(grid) - 2
    for i,j in itertools.product([1,grid_max],repeat=2):
        grid[i,j] = 1
    return grid

grid = ReadInitial('input.dat')  
grid2 = TurnCornersOn(ReadInitial('input.dat'))  
nSteps = 100

for i in xrange(nSteps):   
    grid = NextStep(grid) 
    grid2 = TurnCornersOn(NextStep(grid2))
            
print(numpy.count_nonzero(grid))
print(numpy.count_nonzero(grid2))