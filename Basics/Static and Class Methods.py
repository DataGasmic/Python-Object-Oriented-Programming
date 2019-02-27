# Regular Methods - Pass Instance
# Class Methods - Pass Class
# Static Methods - Passing Nothing


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

	@classmethod
	def data_from_string(cls,str_data):
		first,second_half = str_data.split('.',1)
		last,domain = second_half.split('@')
		return cls(first,last)

	@staticmethod
	def name_count(name):
		return len(name)


fr1 = Friends('Pranjal','Biyani')
fr2 = Friends('Karan','Vyas')

print(Friends.name_count('Rohit'))   # No relation with any instance simply a function, can be used internally as well




