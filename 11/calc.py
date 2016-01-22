def nextletter(c):
    return chr(ord(c) + 1)

def incletters_num(x):
    for i in range(len(x)-2):
        if x[i] + 1 == x[i+1] and x[i+1] + 1 == x[i+2]:
            return True
    return False

def letterpairs(x):
    import itertools
    return len([x for x,y in itertools.groupby(x) if len(list(y)) >= 2]) >= 2

def toChars(vals):
    return "".join(chr(x + ord('a')) for x in vals)

def toNums(vals):
    return [ord(x) - ord('a') for x in vals]

def not_badnum(nums):
    return not any(b in nums for b in toNums(['i','o','l']))


def passwordgenerator(start_pass):
    values = toNums(start_pass)
    while True:
        carry = 1
        for i in reversed(xrange(len(values))):
            values[i] += carry
            if (values[i] < 26):
                break
            values[i] -= 26
            carry = 1
        if incletters_num(values) and not_badnum(values) and letterpairs(values):
            yield toChars(values)

startpass = "hepxcrrq"
p = passwordgenerator(startpass)
print p.next(), p.next()


        
