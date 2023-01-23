# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    RADIUS = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def contains(self, xy):
        return self.distance(xy) < Black_Hole.RADIUS
    
    def update(self, model):
        eaten_simultons = set([i for i in model.find(lambda x: isinstance(x, Prey)) if self.contains(i.get_location())])
        for i in set(eaten_simultons):
            model.remove(i)
        return eaten_simultons 
    
    def display(self, canvas):
        canvas.create_oval(self._x-(self._width/2), self._y-(self._height/2),
                                self._x+(self._width/2), self._y+(self._height)/2,
                                fill='Black')       
        
