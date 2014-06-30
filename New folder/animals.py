from animal_class import *
from sheep_class import *

def display_menu():
    print()
    print("Which crop would you like to create? ")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("Please select an option")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_animal():
    display_menu()
    if choice == 1:
        new_crop = Cow()
    elif choice == 2:
        new_crop = Sheep()
    return new_crop

def main():
    new_animal = create_animal()
    manage_animal(animal)

if __name__ == "__main__":
    main()
    
