def cummulate(*args):
	answer=[]
	summa=0
	for x in args:
		summa += x
		answer.append(summa)
	return answer

print(cummulate(1,3,2,2))