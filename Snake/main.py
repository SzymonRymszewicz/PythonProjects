from Variables import *
import random


class Game:

    def __init__(self):

        self.RUN = True
        self.Snake = self.Snake()  # CREATES SNAKE
        self.Apples = []

        for x in range(0, NUMBER_OF_APPLES, 1):
            self.Apples.append(self.Apple())

        while self.RUN:  # MAIN GAME LOOP
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

            self.logic()
            self.draw()

            GAME_CLOCK.tick(FPS)

        pygame.quit()

    def logic(self):  # ALL GAME LOGIC
        self.Snake.logic()
        for apple in self.Apples:
            if self.Snake.pos_x == apple.pos_x and self.Snake.pos_y == apple.pos_y:
                print("Apple eaten!")
                self.Snake.tail_length += 1
                apple.change_position()

    def draw(self):  # DRAWS EVERYTHING THAT HAPPENS ONTO THE GAME WINDOW

        WINDOW.fill(BLACK)

        for x in range(0, WINDOW_SIZE, BLOCK):  # DRAWS GRID ON THE SCREEN
            for y in range(0, WINDOW_SIZE, BLOCK):
                rect = pygame.Rect(x, y, BLOCK, BLOCK)
                pygame.draw.rect(WINDOW, WHITE, rect, 1)

        for apple in self.Apples:
            apple.draw()
        self.Snake.draw()  # DRAWS SNAKE

        pygame.display.flip()
        pygame.display.update()

    class Snake:

        def __init__(self):
            self.pos_x = int(WINDOW_SIZE / 2)
            self.pos_y = int(WINDOW_SIZE / 2)
            self.direction = "UP"
            self.delta = BLOCK
            self.clock = FPS
            self.tail_length = 0

        def check_border(self):  # CHECKS IF SNAKE 'HITS' THE BORDER AND TELEPORTS IT TO THE OPPOSITE SIDE IF TRUE
            if self.pos_x < 0:
                self.pos_x = WINDOW_SIZE - BLOCK
            elif self.pos_x >= WINDOW_SIZE:
                self.pos_x = 0
            elif self.pos_y < 0:
                self.pos_y = WINDOW_SIZE - BLOCK
            elif self.pos_y >= WINDOW_SIZE:
                self.pos_y = 0

        def move(self):  # MOVEMENT
            if self.direction == "LEFT":
                self.pos_x -= self.delta
            elif self.direction == "RIGHT":
                self.pos_x += self.delta
            elif self.direction == "DOWN":
                self.pos_y += self.delta
            elif self.direction == "UP":
                self.pos_y -= self.delta

            self.check_border()

        def determine_direction(self):  # CHECKS PLAYER INPUT AND DETERMINES IF IT IS VALID
            if pygame.key.get_pressed():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif keys[pygame.K_d] and self.direction != "LEFT":
                    self.direction = "RIGHT"
                elif keys[pygame.K_w] and self.direction != "DOWN":
                    self.direction = "UP"
                elif keys[pygame.K_s] and self.direction != "UP":
                    self.direction = "DOWN"

        def logic(self):  # ALL SNAKE LOGIC
            self.determine_direction()
            if self.clock >= FPS:
                self.move()
                self.clock = 0
            else:
                self.clock += int(FPS / 10)

        def draw(self):  # DRAWS SNAKE
            rect = pygame.Rect(self.pos_x, self.pos_y, BLOCK, BLOCK)
            pygame.draw.rect(WINDOW, GREEN, rect)

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


Game()
