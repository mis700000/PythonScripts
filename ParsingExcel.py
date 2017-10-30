'''
parsing excel 

'''
## Using openpyxl , parsed the excel data and stored into datastructure ( dict/table)
## once retrieve the excel data , will pass it to UI code and 
# store the values into database .

import openpyxl
wb = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\ravi_bckup\\C_Drive\\RaviTeja Mandiga\\Python\\Automation.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Login')

d = {}
for rowIndex in range(2,6) :
    l= []
    for col in range(1,7) :
        l.append(sheet.cell(row=rowIndex, column=col).value)
    d[rowIndex] = l

print(d)		


import login		## UI code ( defined below )	

for key,value in d.items() :  #{2 : ['mrt446' , 'dosko'...............] }
	login.setLoginID(value[0])
	login.setPassword(value[1])
	login.Submit()











login.py
	
	def SetLoginID(self , loginID) :
		self.loginID = loginID
	
	def SetPassword(self , password) :
		self.password = password
		
	def setName(self,name):
		self.name = name
	
	def insertIntoDB(self, dbConnection):
		##Connection to DB
		## SQL , insert into <DB table name > set loginID = self.LoginID and password = self.Password and name = self.Name

	def submit(self):		## Submits the details into DB
		self.insertIntoDB()





## Using openpyxl , parsed the excel data and stored into datastructure ( dict/table)
## once retrieve the excel data , will pass it to UI code and 
# store the values into database .