# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    VISION = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        self.wall_bounce()
        Pulsator.update(self, model)
        within_range = [i for i in model.find(lambda x: isinstance(x, Prey) and x.distance(self.get_location()) <= Hunter.VISION)]
        within_range.sort(key=lambda x: x.distance(self.get_location()))
        if within_range != []:
            closest_prey = within_range[0]
            self.set_angle(atan2(closest_prey.get_location()[0]-self._y, closest_prey.get_location()[1]-self._x))
            
                    
                
