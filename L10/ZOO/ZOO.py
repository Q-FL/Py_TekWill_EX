import cBirds
from datetime import datetime,timedelta

class zoO:
	def __init__(self,classZoo,name,age):
		self.classZoo = classZoo
		self.name = name
		self.age = age

	@staticmethod
	def getAgeInfo(name,age):
		return f'Type: {name} | Lifespan: {age} | Birthday: {datetime.today() - timedelta(weeks=48*int(age))}'

	def __str__(self):
		return f'Animal class: {self.classZoo} | Type: {self.name} | Lifespan: {self.age}'