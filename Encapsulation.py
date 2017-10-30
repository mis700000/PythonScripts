class LoginClass():

	def __init__(self, x, y) :
		self.loginID =  x
		self.password = y
	
	__username = 'Irfan123'
	
	def getLoginID(self):
		return self.loginID
	
	def setLoginID(self) :				## Encapsulation , where __username can set by only this class .Other class dont have
		return __username 
		
	def checkUserStartswithS(self):
		print(1)
		print(str(self.loginID))

	def submit(self):
		print(self.password)
		
	
	def checkUserStartswithS(self,**Kwargs):
		print(names)
		print(str(self.loginID))
	
	def display(self):
		print("Displaying Class")
	


a = LoginClass('ravi', '12365')
a.checkUserStartswithS()
a.checkUserStartswithS(names = [namesFromDB] , id = [idsFromDB] , salaries = [salariesFromDB])

list ---  args 
dict ---- Kwargs

class MyChatloginClass(LoginClass , A , B) :
	
	def submit(self):
		getAlert()
	

b = MyChatloginClass()
b.submit()  # Method overriding of the submit method of Parent class
b.display()	# Multiple inheritance

MRO  - Method Resolution Order.


	
Encapsulation : It is process of Data hiding , where the variables of class will be hidden from other classes and have access only 
	to read/get value.
	* Declare variables as Private 
	* Setter and getters declare as Public 
