my_fruits = ['apple', 'banana', 'pear', 'cherry', 'watermelon']

print("The first three items in the list are:")
print(my_fruits[:3])

print("The items from the middle of the list are:")
print(my_fruits[1:4])

print("The last three items in the list are:")
print(my_fruits[-3:])

friend_fruits = my_fruits[:]
my_fruits.append('mango')
friend_fruits.append('peach')

print("my favorite fruits are:")
for fruit in my_fruits:
	print(fruit)
print("my friend favorites fruits are:")
for fruit in friend_fruits:
	print(fruit)
