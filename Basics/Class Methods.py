# Python OOP Static and Class Methods

class Friends:
	inc_percent = 1.25    
	total_friends = 0


	def __init__(self,first,last,pocket_money):
		self.first = first
		self.last = last
		self.email = first+'_'+last+'@Friends.com'
		self.pocket_money = pocket_money
		Friends.total_friends += 1        

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def inc_pmoney(self):
		self.pocket_money = int(self.pocket_money*self.inc_percent)   

	@classmethod
	def raise_pmoney(cls,percent):
		cls.inc_percent = percent   # Using cls as class is a keyword in Python




fr1 = Friends('Pranjal','Biyani',1000000)
fr2 = Friends('Karan','Vyas',1000000)
fr3 = Friends('Indradeep','Dey',1000000)
fr4 = Friends('Rohit','Shukla',1000000)
fr5 = Friends('Karni','Singh',1000000)

print(Friends.inc_percent)
print(fr1.inc_percent)

Friends.raise_pmoney(2.5)   #Changing the inc_percent of the class, automatically becomes for instances

print('\n')
print(Friends.inc_percent)
print(fr1.inc_percent)

print('\n')

fr1.raise_pmoney(3.0)   # As raise_pmoney() is a class method, any call can change the class variable and also the instance variables together
print(Friends.inc_percent)
print(fr1.inc_percent)
print(fr2.inc_percent)
