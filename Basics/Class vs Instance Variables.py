class Friends:
	inc_percent = 1.25


	def __init__(self,first,last,pocket_money):
		self.first = first
		self.last = last
		self.email = first+'_'+last+'@Friends.com'
		self.pocket_money = pocket_money
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def inc_pmoney(self):
		self.pocket_money = int(self.pocket_money*self.inc_percent)



fr1 = Friends('Pranjal','Biyani',1000000)
fr2 = Friends('Karan','Vyas',1000000)
fr3 = Friends('Indradeep','Dey',1000000)
fr4 = Friends('Rohit','Shukla',1000000)
fr5 = Friends('Karni','Singh',1000000)

#print(emp1.fullname())
#print(emp1.pocket_money)
#fr1.inc_pmoney()
#print(emp1.pocket_money)
print(fr1.pocket_money)
print(fr2.pocket_money)
fr1.inc_percent = 2
fr1.inc_pmoney()
fr2.inc_pmoney()
print(fr1.pocket_money)
print(fr2.pocket_money)
print('\n')
print(Friends.inc_percent)
print(fr1.inc_percent)
print(fr2.inc_percent)
print('\n')
print(Friends.__dict__)
print(fr1.__dict__)
print(fr2.__dict__)
