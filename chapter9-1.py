class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("The user name is " + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def login_number(self):
        print(self.first_name.title() + " login number is " + str(self.login_attempts) + ".")

    def reset_login_attempts(self):
        self.login_attempts = 0

my_user = User('Octor', 'Only')
my_user.describe_user()
my_user.increment_login_attempts()
my_user.login_number()
my_user.increment_login_attempts()
my_user.login_number()
my_user.increment_login_attempts()
my_user.login_number()
my_user.reset_login_attempts()
my_user.login_number()

