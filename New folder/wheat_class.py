from crop_class import *

class Wheat(Crop):
    """ A Wheat Crop"""

    def __init__(self):
        super().__init__(2,3,4)
        self._type = "Wheat"
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seed":
                self._growth += self._growth_rate * 1.5
                
            elif self._status == "Young":
                self._growth += self._growth_rate * 1.25
                
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()
