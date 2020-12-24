phones_list = [{'name':'Ivan', 'city':'Moscow', 'phones':['232-19-55', '+7 (916) 230-00-75']},

{'name':'Anna', 'city':'Samara', 'phones':['200-11-15']},

{'name':'Anna', 'city':'Vologda', 'phones':['+7 (931) 711-00-75']},

{'name':'Nikolay', 'city':'Moscow', 'phones':['+7 (916) 778-71-05', '331-66-11', '783-33-85']},

{'name':'Ivan', 'city':'Moscow', 'phones':['+7 (916) 205-41-05', '232-19-55']},

{'name':'Anna', 'city':'Samara', 'phones':['+7 (916) 105-13-56']}

]

id_to_del=[]
for i in range(len(phones_list)):
	ntmp=phones_list[i]['name']
	ctmp=phones_list[i]['city']
	for j in range(i):
		if phones_list[j]['name']==ntmp and phones_list[j]['city']==ctmp:
			id_to_del.append(i)
			phones_list[j]['phones']+=phones_list[i]['phones']
			phones_list[j]['phones']=list(set(phones_list[j]['phones']))

id_to_del=id_to_del[::-1]
for x in id_to_del:
	phones_list.pop(x)

#for x in phones_list:
#	x['phones']=list(set(x['phones']))

for x in phones_list:
	print(x)
