import pygame

class Pipe:
    def __init__(self, pos, img):
        self.pos = list(pos)
        self.img = img

class Pipes:
    def __init__(self, speed):
        self.pipes = []
        self.speed = speed
