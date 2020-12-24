def repl(s,**kwargs):
	#print(kwargs)
	temp=s.split(' ')
	for i in range(len(temp)):
		for (k,v) in kwargs.items():
			if temp[i]==k:
				temp[i]=v
	#print(temp)
	result = ' '.join(temp)
	return result

print(repl('replace my val abc', my='s1', abc='fff'))