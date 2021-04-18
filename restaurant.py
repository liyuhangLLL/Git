class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cuisine_type}')

    def open_restaurant(self):
        print("restaurant is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f'number served {self.number_served}')

    def increment_number_served(self, increment):
        self.number_served = self.number_served + increment


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


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)





class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavor, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavor = flavor

    def show_taste(self):
        print(f'ice cream taste {self.flavor}')


r1 = Restaurant('luyi', 'chinese')
r2 = Restaurant('yuhang', 'fast food')
r3 = Restaurant('Dai', 'germany')
g1 = User('yuhang', 'li')
r4 = IceCreamStand('yuhang', 'chinese', ['chocolate', 'strawberry'])
g2 = Admin('xuangeng', 'dai', 'can delete post')

r1.describe_restaurant()
g1.greet_user()
g1.increment_login_attempts()
g1.increment_login_attempts()
print(g1.login_attempts)
g1.reset_login_attempts()
print(g1.login_attempts)
r4.show_taste()
g2.show_privileges()