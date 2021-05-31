filename = 'pi_digits.txt'

with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()
	#列表被存储到变量lines当中
for line in lines:
	print(line.rstrip())
