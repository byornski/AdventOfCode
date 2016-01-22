from hashlib import md5
from itertools import count    

key = "ckczppom"
num_zeros = 6

print (x for x in count(1) if str(md5(key+str(x)).hexdigest())[:num_zeros] == "0"*num_zeros).next()
