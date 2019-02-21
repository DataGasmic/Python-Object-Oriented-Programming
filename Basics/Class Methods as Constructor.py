# Python OOP Static and Class Methods

class Friends:
	inc_percent = 1.25    
	total_friends = 0


	def __init__(self,first,last):
		self.first = first
		self.last = last
		#self.email = first+'_'+last+'@Friends.com'
		#self.pocket_money = pocket_money
		#Friends.total_friends += 1        

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def inc_pmoney(self):
		self.pocket_money = int(self.pocket_money*self.inc_percent)   

	@classmethod
	def raise_pmoney(cls,percent):
		cls.inc_percent = percent   # Using cls as class is a keyword in Python

	@classmethod   # Classmethod used a Constructor to create an instance of a class
	def data_from_string(cls,str_data):
		first,second_half = str_data.split('.',1)
		last,domain = second_half.split('@')
		return cls(first,last)  # Instance being created every time a string is passed from the data_from_string method


#fr1 = Friends('Pranjal','Biyani',1000000)
#fr2 = Friends('Karan','Vyas',1000000)
#fr3 = Friends('Indradeep','Dey',1000000)
#fr4 = Friends('Rohit','Shukla',1000000)
#fr5 = Friends('Karni','Singh',1000000)

fr1_email = 'Pranjal.Biyani@Friends.com'   # Wanting to extract first and last name from Email Address
fr2_email = 'Karan.Vyas@Friends.com'       # If input data is expected in the form of a string

fr1 = Friends.data_from_string(fr1_email)
fr2 = Friends.data_from_string(fr2_email)

print(fr1.fullname())
print(fr2.fullname())


