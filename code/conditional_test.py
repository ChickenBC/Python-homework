#conditional_test.py
a = 'sheep'
b = 'lamp'
if a == b:
	print('True')
else:
	print('False')

c = 'sheep'
d = 'Sheep'
if d.lower() == c:
	print('True')
else:
	print('False')

fruits = ['apple', 'pear', 'peach']
fruit_a = 'apple'
if fruit_a in fruits:
	print("Congratulation!")
fruits_b = 'mango'
if fruits_b not in fruits:
	print('try again!')