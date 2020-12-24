from random import *

a=[[randint(1, 9) for i in range(randint(1, 10))] for m in range(randint(3, 8))]
for x in a:
	print(x)
print('-----------------------')
b=[]
for x in a:
	if len(x)<=3:
		b.append(x)
	if len(x)>3:
		t=[x[0],x[1]]
		t.append(sum(x[2:]))
		b.append(t)
for x in b:
	print(x)