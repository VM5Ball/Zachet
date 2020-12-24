from random import *

s='ten,one,five,two,three,four'
print(s)
sp=s.split(',')
sp1=sp.copy()

shuffle(sp1) 

d={k: f'number {sp.index(k)+1} in a string' for k in sp1}

for (k,v) in d.items():
	print(k, ':',v)