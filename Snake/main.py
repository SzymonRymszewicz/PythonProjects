from Variables import *
from Snake import Snake
from Apple import Apple


class Game:

    def __init__(self):

        self.RUN = True
        self.clock = FPS
        self.apples_eaten = 0

        snake.append(Snake())  # CREATES SNAKE
        snake.append(Snake.Tail(snake[0]))
        snake.append(Snake.Tail(snake[1]))
        snake.append(Snake.Tail(snake[2]))

        self.Apples = []
        for x in range(0, NUMBER_OF_APPLES, 1):  # CREATES APPLES
            self.Apples.append(Apple())

        while self.RUN:  # MAIN GAME LOOP
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

            if self.clock >= FPS:
                self.logic()
                self.draw()
                self.clock = 0
            else:
                self.clock += int(FPS / 10)

            GAME_CLOCK.tick(FPS)

        pygame.quit()

    def logic(self):  # ALL GAME LOGIC

        snake[0].logic()

        for parts in snake[1:]:
            parts.logic(snake[snake.index(parts) - 1])
            if snake[0].pos_x == parts.pos_x and snake[0].pos_y == parts.pos_y:
                self.RUN = False
                print("GAME OVER WITH SCORE:", self.apples_eaten)

        for apple in self.Apples:
            if snake[0].pos_x == apple.pos_x and snake[0].pos_y == apple.pos_y:
                snake.append(Snake.Tail(snake[len(snake) - 1]))
                apple.change_position()
                self.apples_eaten += 1

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
