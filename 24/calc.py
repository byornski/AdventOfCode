
def QE(vals):
    return numpy.prod(vals)


def readSizes(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]

sizes = readSizes("Simple.dat")

avg_weight = sum(sizes) /  3



weight_seeks = [avg_weight,avg_weight*2]

import numpy
from numpy import cumsum
from itertools import permutations


#items = [x for x in permutations(sizes) if avg_weight in cumsum(x) and avg_weight*2 in cumsum(x)]


items = numpy.asarray(list(permutations(sizes)))


cs = numpy.cumsum(items,axis=1)

b =   numpy.any(cs == avg_weight,axis=1) & numpy.any(cs==avg_weight*2,axis=1)

indexes = numpy.where(b)


works = [items[i] for i in indexes[0]]


global_min_boxes = 100
global_best_boxes = []


for item in works:
    tots = numpy.cumsum(item)
    lgap, ugap =  numpy.where(tots == avg_weight)[0]+1, numpy.where(tots == avg_weight*2)[0] + 1
    boxes = [ item[:lgap] , item[lgap:ugap], item[ugap:] ]

    local_min_boxes,mindex =  min((len(x),list(x)) for x in boxes)
    
    if local_min_boxes < global_min_boxes:
        global_best_boxes = [ mindex ]
    elif local_min_boxes == global_min_boxes:
        global_best_boxes.append(mindex)
#    if local_min_boxes == 2:
#        print item
        
    
print global_best_boxes, QE(global_best_boxes)


    

        
#print avg_weight

#for i in works:
#    print i


#print len(i[0])




