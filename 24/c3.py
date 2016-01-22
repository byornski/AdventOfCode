
def QE(vals):
    import operator
    return reduce(operator.mul,vals)


def readSizes(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]


    
import itertools


def testMain(sizes,num):
    works = testSizes(sizes,sum(sizes)/num,num)

    return min((QE(w),w) for w in works)

    

def testSizes(sizes,goal,depth):
    works = []

    for min_size in xrange(len(sizes)):
        for bucket in itertools.combinations(sizes,min_size):
            if sum(bucket) == goal:
                #Test for subsets
                if depth > 2:
                    remain = [x for x in sizes if x not in bucket]
                    if testSizes(remain,goal,depth-1):
                        works.append(bucket)
                else:
                    works.append(bucket)
        if works: break
    return works



    
sizes = readSizes("Proper.dat")


print testMain(sizes,3)
print testMain(sizes,4)

