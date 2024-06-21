class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}, {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, people):
        self.number_served = people

    def increment_number_served(self, increment):
        self.number_served += increment

# making different instance and describe them
restaurant_orange = Restaurant("Tutti", "Italian")
restaurant_tustin = Restaurant("Honda", "Izakaya")
restaurant_cerritos = Restaurant("Ipoh", "Malaysian")

restaurant_orange.describe_restaurant()
restaurant_tustin.describe_restaurant()
restaurant_cerritos.describe_restaurant()


restaurant = Restaurant("Solo", "Italian")

# modify the attribute's value directly
restaurant.number_served = 23
restaurant.describe_restaurant()

# modify the attribute's value through method
restaurant.set_number_served(15)
restaurant.increment_number_served(200)
restaurant.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "chocolate", "rum", "earl gray"]

    def display_flavors(self):
        print(f"{self.flavors}")

ice1 = IceCreamStand("Coldstone", "Icecream")
ice1.display_flavors()


class User:
    def __init__(self, appellation, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.appellation = appellation
        self.login_attempts = 0

    def describe_user(self):
        print(self.appellation, self.first_name, self.last_name, self.login_attempts)

    def greet_user(self):
        print(f"Hello {self.appellation} {self.first_name} {self.last_name}, how can I help you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        # reset login to zero
        self.login_attempts = 0

p1 = User("Mr.", "Jensen", "Huang")

# increment login attempts by 1 and give back the value to self(p1)
p1.increment_login_attempts()
p1.describe_user()

p1.increment_login_attempts()
p1.describe_user()

p1.increment_login_attempts()
p1.describe_user()

p1.reset_login_attempts()
p1.describe_user()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"{self.privileges}")

class Admin(User):
    def __init__(self, appellation, first_name, last_name):
        super().__init__(appellation, first_name, last_name)
        self.privileges = Privileges()



a1 = Admin("Ms.", "Anna", "Parker")
a1.describe_user()
a1.privileges.show_privileges()
