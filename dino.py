import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

dino_x = 80
dino_y = 300
dino_w = 40
dino_h = 50

jump = False
jump_speed = 15
gravity = 1
velocity_y = 0

obstacles = []

score = 0
speed = 8

running = True
game_over = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jump:
                    jump = True
                    velocity_y = -15

    if not game_over:

        if jump:
            dino_y += velocity_y
            velocity_y += gravity

            if dino_y >= 300:
                dino_y = 300
                jump = False

        if len(obstacles) == 0 or obstacles[-1].x < WIDTH - random.randint(250, 400):
            obstacles.append(
                pygame.Rect(WIDTH, 320, 25, 30)
            )

        for obs in obstacles:
            obs.x -= speed

        obstacles = [obs for obs in obstacles if obs.x > -50]

        dino_rect = pygame.Rect(dino_x, dino_y, dino_w, dino_h)

        for obs in obstacles:
            if dino_rect.colliderect(obs):
                game_over = True

        score += 1

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (0, 350), (WIDTH, 350), 2)

    pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_w, dino_h))

    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)

    score_text = font.render(f"Score: {score//10}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER", True, BLACK)
        screen.blit(over_text, (WIDTH//2 - 100, HEIGHT//2))

    pygame.display.update()

pygame.quit()
