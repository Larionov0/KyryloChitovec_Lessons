import random
import pygame
import time
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1000
HEIGHT = 600


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, data):
        pass

    def draw(self, window):
        pass

    def move(self, dir, speed):
        if dir == 'w':
            self.y -= speed
        elif dir == 's':
            self.y += speed
        elif dir == 'a':
            self.x -= speed
        elif dir == 'd':
            self.x += speed


class CircleGameObject(GameObject):
    def check_collision(self, other):
        if distance((self.x, self.y), (other.x, other.y)) <= self.radius + other.radius:
            return True
        else:
            return False


class Bullet(CircleGameObject):
    def __init__(self, x, y, damage, speed, r, dir):
        super().__init__(x, y)
        self.damage = damage
        self.speed = speed
        self.radius = r
        self.dir = dir

    def update(self, data):
        self.move(self.dir, self.speed)

        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            data['bullets'].remove(self)
            return

        for enemy in data['enemies']:
            if self.check_collision(enemy):
                enemy.die(data)
                data['bullets'].remove(self)
                break

    def draw(self, window):
        # pygame.draw.rect(window, RED, (self.x, self.y, self.size, self.size))
        pygame.draw.circle(window, RED, (self.x, self.y), self.radius)


class Hero(CircleGameObject):
    def __init__(self, x, y, radius, color, speed, points):
        super().__init__(x, y)
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

    def handle_wasd(self, key, data):
        dir = chr(key)
        data['bullets'].append(
            Bullet(self.x, self.y, 10, 5, 7, dir)
        )

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Enemy(CircleGameObject):
    time_spawn = 0

    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed

    def update(self, data):
        dir = random.choice(['w', 'a', 's', 'd'])
        self.move(dir, self.speed)

    def die(self, data):
        data['enemies'].remove(self)
        data['hero'].points += 1

    @classmethod
    def check_respawn(cls, data):
        time_spent = time.time() - data['time_start']
        if time_spent > cls.time_spawn:
            data['enemies'].append(
                cls(random.randint(100, WIDTH-100), random.randint(50, HEIGHT - 50), 15, RED, 4)
            )
            cls.time_spawn += 5

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(WHITE)

clock = pygame.time.Clock()


hero = Hero(100, 100, 20, BLUE, 3, 0)
enemies = [
    Enemy(45, 45, 40, RED, 2),
    Enemy(145, 45, 40, RED, 2),
    Enemy(45, 145, 40, RED, 2)
]
bullets = []

data = {
    'hor': 0,
    'vert': 0,
    'hero': hero,
    'enemies': enemies,
    'bullets': bullets,
    'time_start': time.time()
}

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

            elif event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                hero.handle_wasd(event.key, data)

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                data['vert'] = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                data['hor'] = 0

    # update
    Enemy.check_respawn(data)
    hero.update(data)
    for enemy in enemies:
        enemy.update(data)
    for bullet in bullets:
        bullet.update(data)

    # draw
    window.fill(WHITE)

    f1 = pygame.font.Font(None, 25)
    text = f1.render(f'Money: {hero.points}', True, BLACK)
    window.blit(text, (850, 10))

    hero.draw(window)
    for enemy in enemies:
        enemy.draw(window)
    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()
    clock.tick(60)
