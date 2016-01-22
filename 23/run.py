from collections import defaultdict

class prog:
    def __init__(self,filename,start_values = {}):
        #Read instruction from a file
        with open(filename) as f:
            self.data = [l.split() for l in f.read().splitlines()]
        #Initialise line pointer and registers
        self.lineno = 0
        self.registers = defaultdict(int,start_values)

    #Define an iterator for instructions...
    def __iter__(self):
        return self
    
    def next(self):
        if self.lineno >= len(self.data) or self.lineno < 0:
            raise StopIteration
        else:
            ret_data = self.data[self.lineno]
            self.lineno += 1
            return ret_data

    #Define a jump to offset
    def rel_jmp(self,offset):
        self.lineno += offset - 1

    def run(self):
        #Iterate over instructions
        for instr in self:
            cmd = instr[0]
            target = instr[1].strip(",")
            
            if len(instr) > 2:
                offset = instr[2]
            else:
                offset = target
                
            jmp_predicate = False
            
            if cmd == "hlf":
                self.registers[target] /= 2
            elif cmd == "tpl":
                self.registers[target] *= 3
            elif cmd == "inc":
                self.registers[target] += 1
            elif cmd == "jmp":
                jmp_predicate = True
            elif cmd == "jie":
                jmp_predicate = self.registers[target] % 2 == 0
            elif cmd == "jio":
                jmp_predicate = self.registers[target] == 1
            else:
                print "iunnno", cmd

            if jmp_predicate:
                self.rel_jmp(int(offset))
        return self


print prog("p1.prog").run().registers["b"]
print prog("p1.prog",start_values={"a":1}).run().registers["b"]

