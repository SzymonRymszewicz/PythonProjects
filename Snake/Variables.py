import pygame

pygame.init()

# CONSTANT GAME VARIABLES

WINDOW_SIZE = 800
NUMBER_OF_APPLES = 3  # NUMBER OF APPLES IN THE GAME
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
BLOCK = int(WINDOW_SIZE / 16)  # SINGULAR 'BLOCK' SIZE
GAME_CLOCK = pygame.time.Clock()
FPS = 60  # MAX FPS

# COLORS (R, G, B)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 150, 0)
GREEN_2 = (0, 255, 0)

# Snake

snake = []
