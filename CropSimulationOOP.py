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
        #returns a dicionary containing the type, status, growth and days growing of the plant
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
            if light >= 1 and light <= 10:
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

if __name__ == "__main__":
    main()