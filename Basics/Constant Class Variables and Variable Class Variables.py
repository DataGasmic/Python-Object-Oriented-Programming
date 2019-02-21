class Friends:
	inc_percent = 1.25    
	total_friends = 0


	def __init__(self,first,last,pocket_money):
		self.first = first
		self.last = last
		self.email = first+'_'+last+'@Friends.com'
		self.pocket_money = pocket_money
		Friends.total_friends += 1        # Using Class name, so that this variable changes with class, not instances

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def inc_pmoney(self):
		self.pocket_money = int(self.pocket_money*self.inc_percent)   # Using self so that each instance can have it's own unique value


print(Friends.total_friends)

fr1 = Friends('Pranjal','Biyani',1000000)
fr2 = Friends('Karan','Vyas',1000000)
fr3 = Friends('Indradeep','Dey',1000000)
fr4 = Friends('Rohit','Shukla',1000000)
fr5 = Friends('Karni','Singh',1000000)

print(Friends.total_friends)
print(fr1.total_friends)
