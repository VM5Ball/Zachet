phones_list = [{'name':'Ivan', 'city':'Moscow', 'phones':['232-19-55', '+7 (916) 230-00-75']},

{'name':'Anna', 'city':'Samara', 'phones':['200-11-15']},

{'name':'Anna', 'city':'Vologda', 'phones':['+7 (931) 711-00-75']},

{'name':'Nikolay', 'city':'Moscow', 'phones':['+7 (916) 778-71-05', '331-66-11', '783-33-85']},

{'name':'Ivan', 'city':'Moscow', 'phones':['+7 (916) 205-41-05', '232-19-55']},

{'name':'Anna', 'city':'Samara', 'phones':['+7 (916) 105-13-56']}

]

cities=[]
for x in phones_list:
	cities.append(x['city'])
cities=list(set(cities))
#print(cities)

phones=[[] for i in range(len(cities))]

for i in range(len(cities)):
	for x in phones_list:
		if x['city']==cities[i]:
			for y in x['phones']:
				phones[i].append((y, x['name']))
#print(phones)
t=[[]for i in range(len(cities))]
for i in range(len(t)):
	t[i]={k: v for k, v in phones[i]}

res=dict(zip(cities, t))

for (k,v) in res.items():
	print(k, ':', v)
