primes = {r for r in xrange(2,100) if not any(r%x==0 for x in xrange(2,r))}
print {(x,x+2) for x in primes if x+2 in primes}
