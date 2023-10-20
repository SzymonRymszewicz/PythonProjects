from Variables import *
from random import *
from Cell import Cell
from Tile import Tile


def innit():
    pygame.display.set_caption("War Cells!")
    for y in range(0, HEIGHT, BLOCK_SIZE):
        for x in range(0, WIDTH, BLOCK_SIZE):
            Tile(x, y)
    starting_tile = randint(0, len(Tiles) - 3)
    Tiles[starting_tile].objects_on_tile.append(Cell(BLOCK_SIZE + 1, RED, starting_tile))
    starting_tile = randint(0, len(Tiles) - 3)
    Tiles[starting_tile].objects_on_tile.append(Cell(BLOCK_SIZE + 1, GREEN, starting_tile))
    starting_tile = randint(0, len(Tiles) - 3)
    Tiles[starting_tile].objects_on_tile.append(Cell(BLOCK_SIZE + 1, BLUE, starting_tile))


def logic():
    for tile in Tiles:
        for element in tile.objects_on_tile:
            element.logic()


def draw_grid():
    for i in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(WINDOW, WHITE, (0, i), (WIDTH, i))
        pygame.draw.line(WINDOW, WHITE, (i, 0), (i, HEIGHT))


def draw():
    WINDOW.fill(BLACK)
    # draw_grid()

    for tile in Tiles:
        tile.draw()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    innit()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        logic()
        draw()
        print("Red: ", Cell.Red_Count, " Green: ", Cell.Green_Count, " Blue: ", Cell.Blue_Count)
    pygame.quit()


if __name__ == "__main__":
    main()
