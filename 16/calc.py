lookstr = '''children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1'''

def GetData(s):
    if "Sue" in s:
        s = s[s.find(":")+2:]
    data = s.split(',')
    d_sue = {}
    for d in data:
        key,value = d.split(": ")
        d_sue[key.strip()] = int(value)
    return d_sue
    
def Readfile(filename):
    with open(filename) as fd:
        data = fd.read().splitlines()
    sues = []
    for d in data:
        sues.append(GetData(d))
    return sues

looksue = GetData(lookstr)
sues = Readfile("input.dat")


for i,s in enumerate(sues,1):
    Found = True
    for key in s:
        if (s[key] != looksue[key]):
            Found = False
            exit
    if Found:
        print i
        break


for i,s in enumerate(sues,1):
    Found = True
    for key in s:
        if key in ['cats','trees']:
            test = s[key] < looksue[key]
        elif key in ['pomeranians','goldfish']:
            test = s[key] > looksue[key]
        else:
            test = s[key] != looksue[key]

        if (test):
            Found = False
            exit
    if Found:
        print i
        break
        