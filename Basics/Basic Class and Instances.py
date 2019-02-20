class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'_'+last+'@companyname.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)



emp1 = Employee('Pranjal','Biyani',1000000)
emp2 = Employee('Single','Vyas',1000000)
emp3 = Employee('Lodu','Dey',1000000)
emp4 = Employee('Notanki','Shukla',1000000)
emp5 = Employee('Party_Kab_Dega','Singh',1000000)

for x in range(5):
	print(Employee.fullname('emp'+'x'))