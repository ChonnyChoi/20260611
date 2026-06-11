import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Gravity Simulator")

clock = pygame.time.Clock()

trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_alpha(40)

stars = [
    (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    )
    for _ in range(300)
]


class Planet:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)

        angle = random.uniform(0, math.pi * 2)

        self.vx = math.cos(angle) * random.uniform(1, 3)
        self.vy = math.sin(angle) * random.uniform(1, 3)

        self.size = random.randint(4, 10)
        self.hue = random.randint(0, 360)

    def update(self, mx, my):

        dx = mx - self.x
        dy = my - self.y

        dist = math.sqrt(dx * dx + dy * dy)

        if dist > 5:
            force = 500 / (dist + 50)

            self.vx += dx / dist * force * 0.02
            self.vy += dy / dist * force * 0.02

        speed_limit = 8

        speed = math.sqrt(self.vx**2 + self.vy**2)

        if speed > speed_limit:
            self.vx *= speed_limit / speed
            self.vy *= speed_limit / speed

        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1

        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

        self.hue += 1
        if self.hue > 360:
            self.hue = 0

    def draw(self):

        color = pygame.Color(0)

        color.hsva = (self.hue, 100, 100, 100)

        pygame.draw.circle(
            trail_surface,
            color,
            (int(self.x), int(self.y)),
            self.size
        )

        pygame.draw.circle(
            screen,
            color,
            (int(self.x), int(self.y)),
            self.size
        )


planets = [Planet() for _ in range(50)]

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()

    screen.fill((5, 5, 15))

    for sx, sy, size in stars:
        pygame.draw.circle(screen, (255, 255, 255), (sx, sy), size)

    screen.blit(trail_surface, (0, 0))

    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(10)
    fade.fill((0, 0, 0))
    trail_surface.blit(fade, (0, 0))

    for planet in planets:
        planet.update(mx, my)
        planet.draw()

    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (mx, my),
        20,
        2
    )

    pygame.display.flip()

pygame.quit()
