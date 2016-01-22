import pstats

p = pstats.Stats('run.dat')


p.sort_stats('calls')
p.print_stats()


factor = 10**9

bn =  0.012 / 4215 
lp  =  0.041 / 2460
ic = 1.739 / 1324556

print bn * factor
print lp * factor
print ic * factor
#print p


#5.089
