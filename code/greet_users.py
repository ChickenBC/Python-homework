def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['chen', 'yang', 'huang']
greet_users(usernames)