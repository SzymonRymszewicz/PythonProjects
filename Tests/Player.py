import pygame.draw

from Variables import *


class Player:

    def __init__(self):
        self.pos = [int(WINDOW_SIZE / 2), int(WINDOW_SIZE / 2)]
        self.size = 30
        self.delta = 10

    def draw(self):
        pygame.draw.circle(WINDOW, RED, self.pos, self.size)

    def move(self):  # MOVEMENT
        if pygame.key.get_pressed():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.pos[0] -= self.delta
            elif keys[pygame.K_d]:
                self.pos[0] += self.delta
            elif keys[pygame.K_w]:
                self.pos[1] -= self.delta
            elif keys[pygame.K_s]:
                self.pos[1] += self.delta

    def logic(self):
        self.move()
