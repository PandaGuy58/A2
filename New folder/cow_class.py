from animal_class import *

class Cow(Animal):
    def __init__(self):
        super().__init__(10,10,10,"Mammal","Cow")

    def grow(self,food,water):
        if food >= self._water_need and water >= water._water_need:
            self._weight += self._growth_rate * 2
        self._days_growing += 1
        self.update_status()
        
