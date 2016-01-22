import cProfile

class operand:
    def __init__(self,val):
        #Try parsing as an int
        try:
            self.int_val = int(val)
            self.has_value = True
        except:
            self.string_val = val
            self.has_value = False

    def __str__(self):
        if (self.has_value):
            return str(self.int_val)
        else:
            return self.string_val

    def update_val(self,d):
        if not self.has_value:
            if (self.string_val in d):
                self.int_val = d[self.string_val]
                self.has_value = True

class op:
    def __init__(self,operation,operands,target):
        self.f = operation
        self.operands = operands
        self.name = operation.__name__.strip("_")
        self.target = target
        self.can_perform = all(o.has_value for o in self.operands)
        self.already_run = False
    
    def perform(self,d):
        if not self.can_perform:
            raise Exception('Dont have all required values')
        if self.target in d:
            pass #For part b
        else:
            vals = [o.int_val for o in self.operands]
            res = self.f(*vals)
            d[self.target] = res
        self.already_run = True

    def update(self,d):
        for o in self.operands:
            o.update_val(d)
        self.can_perform = all(o.has_value for o in self.operands)

    def update_and_perform(self,d):
        self.update(d)
        if self.can_perform:
            self.perform(d)
            
    def __str__(self):
        d = map(str,self.operands)
        if (len(self.operands)==2):
            return d[0] + " " + self.name + " " + d[1] + " => " + self.target
        else:
            return self.name + " " + d[0] + " => " + self.target
        return ""

def Let(a):
    return a
    
def ParseOp(string):
    import operator as op_list
    if string=="NOT":
        return op_list.inv
    elif string=="ADD":
        return op_list.add
    elif string=="AND":
        return op_list.__and__
    elif string=="OR":
        return op_list.__or__
    elif string=="LSHIFT":
        return op_list.lshift
    elif string=="RSHIFT":
        return op_list.rshift
    else:
        raise Exception('Bad operator',string)
   
def parse(cmd):
    s = cmd.split('->')
    target = s[1].strip()
    ops = s[0].split()
    if len(ops)==1:
        d = [ops[0]]
        o = Let
    elif len(ops)==2:
        d = [ ops[1] ]
        o = ParseOp(ops[0])
    else:
        d = [ops[0],ops[2]]
        o = ParseOp(ops[1])
    d = map(operand,d)
    o = op(o,d,target)  
    return o

def run_file(filename,values=None):
    with open(filename) as filedata:
        data = filedata.read().splitlines()

    if not values: values = {}
    todo = [parse(d) for d in data]

    while todo:
        for o in todo:
            o.update_and_perform(values)
        todo = [o for o in todo if not o.already_run]    
    return values

def perform():
    a = run_file("input2.dat")['a']
    print a
    print run_file("input3.dat",{'b':a})['a']


cProfile.run('perform()')
