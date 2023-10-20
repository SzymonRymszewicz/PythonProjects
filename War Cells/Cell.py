from Variables import *
from random import *


class Cell:
    Red_Count = 0
    Green_Count = 0
    Blue_Count = 0

    def __init__(self, size, color, position):
        self.replication_chance = 20
        self.size = size
        self.color = color
        self.position = position
        self.previous_position = self.position
        Tiles[self.position].is_empty = False
        self.max_pop = WIDTH / 5

        self.possible_directions = []

        if Cell.Red_Count < self.max_pop and self.color == RED:
            Cell.Red_Count += 1
        if Cell.Green_Count < self.max_pop and self.color == GREEN:
            Cell.Green_Count += 1
        if Cell.Blue_Count < self.max_pop and self.color == BLUE:
            Cell.Blue_Count += 1

    def logic(self):
        self.nearby_tiles()

        if len(self.possible_directions) > 0:
            self.movement()

        if Cell.Red_Count < self.max_pop and self.color == RED:
            self.replicate()
        if Cell.Green_Count < self.max_pop and self.color == GREEN:
            self.replicate()
        if Cell.Blue_Count < self.max_pop and self.color == BLUE:
            self.replicate()

    def movement(self):
        chosen_tile = randint(0, len(self.possible_directions) - 1)
        for i in range(0, len(Tiles), 1):
            if i == chosen_tile and self.possible_directions[i].is_empty:
                self.move_to(self.possible_directions[i])
            elif i == chosen_tile and not self.possible_directions[i].is_empty:
                self.kill_enemy(self.possible_directions[i])
                self.move_to(self.possible_directions[i])

    def move_to(self, tile):
        tile.is_empty = False
        Tiles[self.position].is_empty = True
        Tiles[self.position].objects_on_tile.pop(Tiles[self.position].objects_on_tile.index(self))
        tile.objects_on_tile.append(self)
        self.previous_position = self.position
        self.position = Tiles.index(tile)

    def kill_enemy(self, tile):
        for element in tile.objects_on_tile:
            if element.color != self.color:
                if element.color == RED:
                    Cell.Red_Count -= 1
                if element.color == GREEN:
                    Cell.Green_Count -= 1
                if element.color == BLUE:
                    Cell.Blue_Count -= 1
                tile.objects_on_tile.pop(tile.objects_on_tile.index(element))

    def replicate(self):
        replication_chance = randint(0, self.replication_chance)

        if replication_chance == 0 and Tiles[self.previous_position].is_empty:
            Tiles[self.previous_position].objects_on_tile.append(
                Cell(BLOCK_SIZE + 1, self.color, self.previous_position))

    def nearby_tiles(self):
        self.possible_directions.clear()
        for tile in Tiles:
            if tile.x == Tiles[self.position].x + BLOCK_SIZE and tile.y == Tiles[self.position].y:
                self.possible_directions.append(tile)
            if tile.x == Tiles[self.position].x - BLOCK_SIZE and tile.y == Tiles[self.position].y:
                self.possible_directions.append(tile)
            if tile.y == Tiles[self.position].y + BLOCK_SIZE and tile.x == Tiles[self.position].x:
                self.possible_directions.append(tile)
            if tile.y == Tiles[self.position].y - BLOCK_SIZE and tile.x == Tiles[self.position].x:
                self.possible_directions.append(tile)
