import random
class Animal:
    """A generic animal class"""

    def __init__(self,weight,food,water,Type,name):
        self._weight = weight
        self._days_growing = 0 
        self._growth_rate = 1
        self._food_need = food
        self._water_need = water
        self._status = "New Born"
        self._type = Type
        self._name = name
    def report(self):
        return {'type': self._type,'name': self._name,'status':self.status}
    def update_status(self):
        if self._days_growing > 600:
            self._days_growing = "Old"
        elif self._days_growing > 300:
            self._status = "Mid-life"
        elif self._days_growing > 100:
            self._status = "Mature"
        elif self._days_growing > 50:
            self._status = "Young"
        elif self._days_growing > 10:
            self._status = "Very Young"
    def grow(self,water,food):
        if food >= self._food_need and water >= self._water_need:
            self._days_growing += 1
        self.update_status()

def auto_grow(animal,days):
    for day in range(days):
        water = random.randint(1,20)
        food = random.randint(1,20)
        animal.grow(water,food)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow Autamatically over 30 days")
    print("3. Report status")
    print("0. Exit program")
    print()
    print("Select an option from the menu above")

def get_menu_choice():
    Invalid = True
    while Invalid:
        try:
            choice = int(input("Choose your option: "))
            if 0 <= choice <= 4:
                Invalid = False
            else:
                raise ValueError
        except ValueError:
            print("Enter a value between 0 and 3")
    return choice

def manage_animal(animal):
    print("[Animal management program]")
    print()
    Exit = False
    while not Exit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            Exit = True
            print()
    print(" Bye Bye")

def manual_grow(animal):
    NotValid = True
    while NotValid:
        try:
            food = int(input("Enter a food value: "))
            if 1 <= food <= 10:
                NotValid = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter a value between 1 and 10")
    NotValid = True
    while NotValid:
        try:
            water = int(input("Please enter a water value: "))
            if 1 <= water <= 10:
                NotValid = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter a value between 1 and 10")
    animal.grow(water,food)






    
