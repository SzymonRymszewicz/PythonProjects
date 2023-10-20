from Variables import *


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.objects_on_tile = []
        self.is_empty = True

        Tiles.append(self)

    def draw(self):
        for element in self.objects_on_tile:
            pygame.draw.rect(WINDOW, element.color, pygame.Rect(self.x, self.y, element.size, element.size))
