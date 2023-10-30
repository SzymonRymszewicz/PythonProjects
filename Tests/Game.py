import pygame

from Variables import *
from Player import Player
from Bullet import Bullet


class Game:

    def __init__(self):

        self.run = True
        self.player = Player()
        self.bullets_on_window = []

        pygame.display.set_caption("Window")
        pygame.mouse.set_visible(False)

        while self.run:  # MAIN GAME LOOP
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.bullets_on_window.append(Bullet(self.player.pos))
                        print("shoot")

            self.logic()
            self.draw()
            GAME_CLOCK.tick(FPS)

        pygame.quit()

    def logic(self):
        self.player.logic()

    def draw(self):
        WINDOW.fill(BLACK)

        for bullet in self.bullets_on_window:
            bullet.draw()
        self.player.draw()
        pygame.draw.circle(WINDOW, GREEN, pygame.mouse.get_pos(), 5, 1)

        pygame.display.flip()
        pygame.display.update()
