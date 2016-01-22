def decode(string):
    p = iter(string)
    ret = ""
    for i in p:
        if i == "\\":
            i = p.next()
            if (i == "x"):
                i = chr(int(p.next() + p.next(),16))
        ret += i
    return ret[1:-1]

def encode(string):
    ret = "\""
    for i in string:
        if i=="\\" or i=="\"":
            ret += "\\"
        ret += i
    ret += "\""
    return ret

filename = "input.dat"

with open(filename) as filedata:
    data = filedata.read().splitlines()

  
print sum(len(d) - len(decode(d)) for d in data)
print sum(len(encode(d)) - len(d) for d in data)

