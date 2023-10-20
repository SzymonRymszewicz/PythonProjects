import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
BLOCK_SIZE = 25

FPS = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

Tiles = []

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
