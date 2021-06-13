def make_car(manufacturer, type_car, **other_parm):
	car = {}
	car['manufacturer'] = manufacturer
	car['type'] = type_car
	for key, value in other_parm.items():
		car[key] = value
	return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
