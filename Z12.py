import csv

def find_any(**columnvalues):
	res=[]
	headers=[x for x in columnvalues]
	with open('H:\\Python\\Володя\\Финашка\\Зачёт по питону\\participants.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for line in csv_reader:
			for header in headers:
				if line[header] == columnvalues[header]:
					res.append(line)
					break
	return res

print(find_any(name='Nate'))