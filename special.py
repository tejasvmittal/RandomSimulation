# A special is prey but unlike ball and floater it tries to
#    move away from blackhole, pulsator and hunter
#    They are green in color and are smaller and more agile than the balls

from prey import Prey 
from blackhole import Black_Hole
from math import pi, atan2

class Special(Prey):
    RADIUS = 3
    APPROACH = 50
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 6, 6, 0, 8)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        self.wall_bounce()
        within_range = [i for i in model.find(lambda x: isinstance(x, Black_Hole) and x.distance(self.get_location()) <= Special.APPROACH)]
        within_range.sort(key=lambda x: x.distance(self.get_location()))
        if within_range != []:
            run_from = within_range[0]
            self.set_angle(atan2(run_from.get_location()[0]-self._y, run_from.get_location()[1]-self._x)-pi)
            
    def display(self, canvas):
        canvas.create_oval(self._x-Special.RADIUS, self._y-Special.RADIUS,
                                self._x+Special.RADIUS, self._y+Special.RADIUS,
                                fill='Green')