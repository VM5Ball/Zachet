def cummulate(*args, mul=True):
	if mul==False:
		answer=[]
		summa=0
		for x in args:
			summa += x
			answer.append(summa)
	else:
		answer=[]
		multi=1
		for x in args:
			multi *= x
			answer.append(multi)
	return answer

print(cummulate(1,3,2,2))
print(cummulate(1,3,2,2, mul=False))