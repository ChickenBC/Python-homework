administrators = ['lucy', 'sheldon', 'missy', 'admin', 'frank']

for administrator in administrators:
	if administrator == 'admin':
		print("Hello " + administrator + ", would you like to see status report?")
	else:
		print("Hello " + administrator + ", thank you for logging again.")

Eric = []
if Eric:
	print("Hola!")
else:
	print("We need to find some users!")

current_users = ['Lucy', 'sheldon', 'missy', 'admin', 'frank']
new_users = ['lucy', 'sheldon', 'missy', 'eric', 'billy']
current_user_lower = [user.lower() for user in current_users]
for current_user in current_users:
	if current_user.lower() in current_user_lower:
		print("Sorry, " + current_user + ", that name was taken.")
	else:
		print("Great, " + current_user + ", is stil available.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")