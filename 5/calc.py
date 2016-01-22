



def enough_vowels(x):
    return len([t for t in x if t in ['a','e','i','o','u']]) >= 3


def repeated_letter(x):
    return len([a for a,b in zip(x,x[1:]) if a==b]) >= 1

def no_bad_strings(x):
    return all(t not in x for t in ['ab','cd','pq','xy'])

def is_good1(x):
    return enough_vowels(x) and repeated_letter(x) and no_bad_strings(x)

def repeated_with_gap(x):
    return len([a for a,b in zip(x,x[2:]) if a==b]) >= 1

def repeated_pair(x):
    return any(x[t:t+2] in x[t+2:] for t in xrange(len(x)))

def is_good2(x):
    return repeated_with_gap(x) and repeated_pair(x)



with open('input.dat') as filedata:
    data = filedata.read().splitlines()

print sum(is_good1(x) for x in data)
print sum(is_good2(x) for x in data)

