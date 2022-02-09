'''
class car:
	def __init__(self):
		self.x=10
		print("car object")
class bmw(car):
	def __init__(self):
		self.x=20
		print("bmw object")
class bmw_3_series(bmw):
	pass
class bmw_7_series(bmw):
	def __init__(self):
		self.x=30
		super().__init__();
		print("bmw_7_series object")
class benz(bmw_7_series):
	def __init__(self):
		print("benz object")
		self.x=40
		super().__init__();
class test(benz,bmw_7_series,bmw_3_series):
	def __init__(self):
		super().__init__();
		print("test object")
t=test()
print(t.x)

'''


'''my_list=(1,2,3,)
if type(my_list)is list:
	print(1==1)

class car:
	def b__init__(self):
		self.x=10
		print("car object")
class bmw(car):
	def __init__(self):
		self.x_=20
		self._y=5
		print("bmw object")
		super().__init__();
t=bmw()
print(t.x_)
print(t.x)
print(t._y)

