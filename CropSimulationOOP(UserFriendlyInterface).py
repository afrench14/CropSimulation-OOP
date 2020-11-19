import random


class Crop:
    '''a generic crop'''
    
    #constructor
    def __init__(self, growth_rate, light_needed, water_needed):
        #setting attributes with an initial value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_needed = light_needed
        self._water_needed = water_needed
        self._status = "Seed"
        self._type = "Generic"
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class

    def needs(self):
        #returns light and water needs in a dictionary
        return {"light need " : self._light_needed, "water need " : self._water_needed }

    def report(self):
        #returns a dicionary containing the type, status, growth and days growing of the plant in a dictionary
        return {"type " : self._type, "status " : self._status, "growth " : self._growth, "days growing" : self._days_growing}

    def _update_status(self):
        if self._growth > 20:
            self._status = "Dead"
        elif self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self, light, water):
        if light >= self._light_needed and water >= self._water_needed:
            self._growth = self._growth + self._growth_rate
        #increments number of days growing
        self._days_growing = self._days_growing + 1
        #updating status of crop
        self._update_status()

def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light, water)

def manual_grow(crop):
    #get light and water values from the user
    valid = False
    while not valid:
        try:
            light = int(input("please enter a light value (1-10): ")
            if 1 <= light <= 10:
                valid = True
            else:
                print("value entered not valid, enter a value (1-10): ")
        except ValueError:
            print("value entered not valid, enter a value (1-10): ")
    valid = False
    while not valid:
        try:
            water = int(input("please enter a water value (1-10): ")
            if water >= 1 and water <= 10:
                valid = True
            else:
                print("value entered not valid, enter a value (1-10): ")
        except ValueError:
            print("value entered not valid, enter a value (1-10): ")
    #growing the crop
    crop.grow(light, water)


def main():
    #instanciate the crop class
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    manual_grow(new_crop,30)
    print(new_crop.report())
    
def display_menu():
    print("1. grow manually over one day. ")
    print("2. Grow automatically over 30 days. ")
    print("3. Status report. ")
    print("0. Exit crop simulation. ")
    print()
    print("Please select an option form the above menu. ")
    
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid input. ")
        except ValueError:
            print("Please eter a valid option. ")
    return choice

def manage_crop(crop):
    print("This is the crop management program. ")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        elif option == 2:
            auto_grow(crop, 30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
    print("thank you for using the crop management program. ")

def main():
    new_crop = crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()



"""http://pythonschool.net/oop/inheritance-and-polymorphism/"""
#further methods video
