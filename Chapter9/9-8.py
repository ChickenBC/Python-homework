class User():

	def __init__(self, first_name, last_name, username, email, location):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.location = location

	def describe_user(self):
		print("\n" + self.first_name + " " + self.last_name)
		print("Username: " + self.username)
		print("Email: " + self.email)
		print("Location: " + self.location)

	def greet_user(self):
		print("\nWelcome back, " + self.username + "!")


class Privileges():

	def __init__(self, privileges=[]):
		#注意列表的表示方法
		self.privileges = privileges

	def show_privileges(self):
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- This user has no privileges.")

class Admin(User):

	def __init__(self, first_name, last_name, username, email, location):
		super().__init__(first_name, last_name, username, email, location)
		self.privilege = Privileges()

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privilege.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privilege.privileges = eric_privileges
eric.privilege.show_privileges()
