filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
	name = input("\nEnter you name:")
	if name != 'quit':
		with open(filename, 'a') as f:
			f.write(name + "\n")
			print("Hi " + name + ", you've been added to the guest book.")
	else:
		break
