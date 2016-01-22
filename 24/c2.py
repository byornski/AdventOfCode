
def QE(vals):
    import operator
    return reduce(operator.mul,vals)


def readSizes(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]


def testWorks(sizes,goal):
    return len(testSizes(sizes,goal)) > 0
    

def test2(sizes,goal):
    


def testSizes(sizes,goal):
    import itertools
    done = False
    works = []

    for min_size in xrange(len(sizes)):
        for bucket in itertools.combinations(sizes,min_size):
            if sum(bucket) == avg_weight:
                done = True
                works.append(bucket)
        if done: break
    return works
    

    
sizes = readSizes("Proper.dat")

avg_weight = sum(sizes) /  3

works = testSizes(sizes,avg_weight)

best_boxes = []

for w in works:
    remain = [x for x in sizes if x not in w]
    if testWorks(remain,avg_weight):
        best_boxes.append(w)


        
bb = min(best_boxes,key=QE)

print bb, QE(bb)





