def recursivecount(x,redflag):
    sum = 0

    if (type(x)==dict):
        x = [x[y] for y in x]
        if redflag and 'red' in x:
            return 0

    for i in x:
        if type(i) == dict or type(i) == list:
            sum += recursivecount(i,redflag)
        elif type(i)== int:
            sum += i
    return sum


import json

with open('input.dat') as filedata:
    data = json.load(filedata)
    
print recursivecount(data,redflag=False)
print recursivecount(data,redflag=True)
