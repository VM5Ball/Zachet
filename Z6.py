from fractions import Fraction

first_number=input('Enter first num: ').split(' ')
if len(first_number)>1:
	celaya_chast=int(first_number[0])
	drob=Fraction(first_number[1])
	number1=celaya_chast+drob
else:
	number1=Fraction(first_number[0])

second_number=input('Enter second num: ').split(' ')
if len(second_number)>1:
	celaya_chast=int(second_number[0])
	drob=Fraction(second_number[1])
	number2=celaya_chast+drob
else:
	number2=Fraction(second_number[0])

resultat = number1*number2

if resultat>1:
	resultat=str(resultat).split('/')
	chislitel=int(resultat[0])
	znamenatel=int(resultat[1])
	cel=chislitel//znamenatel
	ost=chislitel-(cel*znamenatel)
	print(cel, ' ', ost,'/', znamenatel, sep='')
else:
	print(resultat)
