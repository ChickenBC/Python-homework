class Restaurant():

	def __init__(self, retaurant_name, cuisine_type):
		self.retaurant_name = retaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.retaurant_name.title() + " " + self.cuisine_type.title())

	def open_restaurant(self):
		print(self.retaurant_name.title() + " is opening.")

	def number_serve(self):
		print("The number is " + str(self.number_served) + '.')

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, increment_number):
		self.number_served += increment_number

'''
class IceCreamStand():

	def __init__(self, retaurant_name, cuisine_type):
		super().__init__()
		self.flavors = ['strawberry', 'mango', 'orange', 'apple']

	def describe_icecream(self):
		for flavor in self.flavors:
			print("The flavor of the icecream is " + flavor + ".")
		
icecreamstand1 = IceCreamStand('lixiaohong', 'chinese')
icecreamstand1.describe_icecream()
'''
class IceCreamStand(Restaurant):
	#记得把父类写入括号里面
	def __init__(self, retaurant_name, cuisine_type):
		super().__init__(retaurant_name, cuisine_type)
		self.flavors = ['strawberry', 'mango', 'orange', 'apple']

	def describe_icecream(self):
		for flavor in self.flavors:
			print("The flavor of the icecream is " + flavor + ".")

icecreamstand1 = IceCreamStand('lixiaohong', 'chinese')
icecreamstand1.describe_icecream()
