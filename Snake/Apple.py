from Variables import *
import random


class Apple:

    def __init__(self):
        self.pos_x = None
        self.pos_y = None

        self.change_position()

    def change_position(self):  # CHANGES THE POSITION OF THE APPLE
        self.pos_x = random.randrange(0, WINDOW_SIZE - BLOCK, BLOCK)
        self.pos_y = random.randrange(0, WINDOW_SIZE - BLOCK, BLOCK)

    def draw(self):  # DRAWS APPLE
        rect = pygame.Rect(self.pos_x, self.pos_y, BLOCK, BLOCK)
        pygame.draw.rect(WINDOW, RED, rect)
