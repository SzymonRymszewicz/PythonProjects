from Variables import *
from Snake import Snake
from Apple import Apple


class Game:

    def __init__(self):

        self.RUN = True
        snake.append(Snake())  # CREATES SNAKE
        self.Apples = []

        for x in range(0, NUMBER_OF_APPLES, 1):
            self.Apples.append(Apple())

        while self.RUN:  # MAIN GAME LOOP
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

            self.logic()
            self.draw()

            GAME_CLOCK.tick(FPS)

        pygame.quit()

    def logic(self):  # ALL GAME LOGIC

        snake[0].logic()

        for parts in snake[1:]:
            parts.logic(snake[snake.index(parts) - 1].direction)

        for apple in self.Apples:
            if snake[0].pos_x == apple.pos_x and snake[0].pos_y == apple.pos_y:
                snake.append(Snake.Tail(snake[len(snake) - 1]))
                apple.change_position()

    def draw(self):  # DRAWS EVERYTHING THAT HAPPENS ONTO THE GAME WINDOW

        WINDOW.fill(BLACK)

        for x in range(0, WINDOW_SIZE, BLOCK):  # DRAWS GRID ON THE SCREEN
            for y in range(0, WINDOW_SIZE, BLOCK):
                rect = pygame.Rect(x, y, BLOCK, BLOCK)
                pygame.draw.rect(WINDOW, WHITE, rect, 1)

        for apple in self.Apples:
            apple.draw()
        for parts in snake:  # DRAWS SNAKE
            parts.draw()

        pygame.display.flip()
        pygame.display.update()


Game()
