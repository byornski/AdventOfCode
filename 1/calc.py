import itertools


def cumsum(data):
    sum = 0
    for i in data:
        sum += i
        yield sum
        
with open("input.dat") as filedata:
    data = ( {"(":1,")":-1}[c] for c in list(filedata.read()) )

partial_sum = cumsum(data)   
first_basement = next(i for i,x in enumerate(partial_sum,1) if x<0)

print list(partial_sum)[-1], first_basement

