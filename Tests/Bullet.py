from Variables import *


class Bullet:

    def __init__(self, pos):
        self.pos = pos
        self.size = 20

    def draw(self):
        pygame.draw.circle(WINDOW, RED, self.pos, self.size)
