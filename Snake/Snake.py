from Variables import *


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
        pygame.draw.rect(WINDOW, GREEN_2, rect)

    class Tail:

        def __init__(self, parent):
            self.parent = parent
            self.pos_x = self.parent.pos_x
            self.pos_y = self.parent.pos_y
            self.delta = BLOCK
            self.clock = FPS
            self.direction = self.parent.direction

            self.offset()

        def move(self, direction):  # MOVEMENT
            self.direction = direction
            if self.direction == "LEFT":
                self.pos_x -= self.delta
            elif self.direction == "RIGHT":
                self.pos_x += self.delta
            elif self.direction == "DOWN":
                self.pos_y += self.delta
            elif self.direction == "UP":
                self.pos_y -= self.delta

        def offset(self):  # PLACES TAIL BEHIND THE 'PARENT PART'
            if self.direction == "LEFT":
                self.pos_x += self.delta
            elif self.direction == "RIGHT":
                self.pos_x -= self.delta
            elif self.direction == "DOWN":
                self.pos_y -= self.delta
            elif self.direction == "UP":
                self.pos_y += self.delta

        def draw(self):  # DRAWS TAIL
            rect = pygame.Rect(self.pos_x, self.pos_y, BLOCK, BLOCK)
            pygame.draw.rect(WINDOW, GREEN, rect)

        def logic(self, direction):  # ALL TAIL LOGIC
            if snake[0].clock >= FPS:
                self.move(direction)
                self.clock = 0
