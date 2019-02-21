class Friends:

	def __init__(self,first,last,pocket_money):
		self.first = first
		self.last = last
		self.pocket_money = pocket_money
		self.email = first+'_'+last+'@Friends.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)



fr1 = Friends('Pranjal','Biyani',1000000)
fr2 = Friends('Karan','Vyas',1000000)
fr3 = Friends('Indradeep','Dey',1000000)
fr4 = Friends('Rohit','Shukla',1000000)
fr5 = Friends('Karni','Singh',1000000)

print(fr1.fullname())
print(fr2.fullname())
print(fr3.fullname())
print(fr4.fullname())
print(fr5.fullname())

print(fr1.email)
print(fr2.email)
print(fr3.email)
print(fr4.email)
print(fr5.email)

