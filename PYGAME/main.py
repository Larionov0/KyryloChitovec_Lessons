import random
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1000
HEIGHT = 600


class Hero:
    def __init__(self, x, y, radius, color, speed, points):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.points = points

    def update(self, data):
        if data['vert'] == 1:
            if self.y < HEIGHT:
                self.y += self.speed
        elif data['vert'] == -1:
            self.y -= self.speed
        if data['hor'] == 1:
            self.x += self.speed
        elif data['hor'] == -1:
            self.x -= self.speed

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Enemy:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def update(self, data):
        dir = random.choice(['w', 'a', 's', 'd'])
        if dir == 'w':
            self.y -= 1
        elif dir == 's':
            self.y += 1
        elif dir == 'a':
            self.x -= 1
        elif dir == 'd':
            self.x += 1

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(WHITE)

clock = pygame.time.Clock()

data = {
    'hor': 0,
    'vert': 0
}

hero = Hero(100, 100, 20, BLUE, 3, 0)
enemies = [
    Enemy(45, 45, 40, RED, 2),
    Enemy(145, 45, 40, RED, 2),
    Enemy(45, 145, 40, RED, 2)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                data['vert'] = -1
            elif event.key == pygame.K_DOWN:
                data['vert'] = 1
            elif event.key == pygame.K_LEFT:
                data['hor'] = -1
            elif event.key == pygame.K_RIGHT:
                data['hor'] = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                data['vert'] = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                data['hor'] = 0

    # update
    hero.update(data)
    for enemy in enemies:
        enemy.update(data)

    # draw
    window.fill(WHITE)

    hero.draw(window)
    for enemy in enemies:
        enemy.draw(window)

    pygame.display.update()
    clock.tick(60)
