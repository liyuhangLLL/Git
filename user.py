class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_uesr(self):
        long_name = f'{self.first_name} {self.last_name}'
        print(long_name.title())

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0