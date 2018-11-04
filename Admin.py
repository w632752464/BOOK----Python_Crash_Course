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

class Admin(User):

    def __init__(self, first_name, last_name):
        super.__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The admin " + self.privileges)

admin = Admin('asd', 'wu')
admin.show_privileges()