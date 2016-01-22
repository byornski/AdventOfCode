startval = 20151125

mul_factor = 252533
mod_factor = 33554393

required_code = (2947,3029)
#required_code = (4,4)

def t_sum(n):
    return (n * (n + 1))/2

#Turn required code location into a number
power = t_sum(sum(required_code) - 2) + required_code[1]


#val = startval
#for i in range(power-1):
#    val = (val * mul_factor) % mod_factor
#print required_code, val


val = (pow(mul_factor,power-1,mod_factor) * startval) % mod_factor

print required_code,val

