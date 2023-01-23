# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    RADIUS = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 0, 5)
        self.randomize_angle()
        
        
    def update(self, model):
        if random()*100 < 30:
            self._speed += random()-.5
            while 7 > self._speed > 3:
                self._speed += random()-.5
            self._angle += random()-.5
        self.move()
        self.wall_bounce()
        
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.RADIUS, self._y-Floater.RADIUS,
                        self._x+Floater.RADIUS, self._y+Floater.RADIUS,
                        fill='Red')
        
