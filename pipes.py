import pygame

class Pipe:
    def __init__(self, pos, img, speed):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
    def update(self):
        self.pos[0] += self.speed

    def render(self):
        # render a pipe twice with different orientations
        pass
        
class Pipes:
    def __init__(self, speed):
        pass
    def render(self):
        pipe.render() 

    
