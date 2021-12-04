import csv
from os.path import exists
PATH = 'data/'
class Data():
	def __init__(self,file_name:str,headers:[str]):
		self.path = PATH+file_name
		self.headers = headers
		if exists(PATH):
			print("Creating file in "+self.path)
			self.__createCsv__()
		else:
			raise Exception("!Error in relaitve path")	
	def __createCsv__(self):
		try:
			with open(self.path,"w") as f:
				csv_handler = csv.DictWriter(f,self.headers)
				csv_handler.writeheader()
		finally:
			f.close()	

d1 = Data('usuarios.csv',['id','nombres','contraseñas','saldo'])