import pygame
import random

pygame.init()

# -------------------------
# SCREEN SETTINGS
# -------------------------
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game - Coins Extension")

clock = pygame.time.Clock()

# -------------------------
# COLORS
# -------------------------
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
YELLOW = (255, 215, 0)

# -------------------------
# PLAYER CAR
# -------------------------
car = pygame.Rect(180, 500, 40, 60)

# -------------------------
# COIN SYSTEM
# -------------------------
coins = []  # list of coin rectangles
coin_spawn_timer = 0
coin_score = 0

# font for UI
font = pygame.font.SysFont("Arial", 24)

running = True
while running:

    # -------------------------
    # BACKGROUND
    # -------------------------
    screen.fill(GRAY)

    # -------------------------
    # EVENTS
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------------
    # PLAYER MOVEMENT
    # -------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car.x > 0:
        car.x -= 5
    if keys[pygame.K_RIGHT] and car.x < WIDTH - car.width:
        car.x += 5

    # -------------------------
    # SPAWN COINS RANDOMLY
    # -------------------------
    coin_spawn_timer += 1

    if coin_spawn_timer > 50:  # every ~0.8 seconds
        x = random.randint(20, WIDTH - 20)
        coin_rect = pygame.Rect(x, 0, 20, 20)
        coins.append(coin_rect)
        coin_spawn_timer = 0

    # -------------------------
    # MOVE & CHECK COINS
    # -------------------------
    for coin in coins[:]:
        coin.y += 5  # coin falling speed

        # collision with car
        if car.colliderect(coin):
            coins.remove(coin)
            coin_score += 1

        # remove if off screen
        elif coin.y > HEIGHT:
            coins.remove(coin)

        # draw coin
        pygame.draw.circle(screen, YELLOW, coin.center, 10)

    # -------------------------
    # DRAW CAR
    # -------------------------
    pygame.draw.rect(screen, WHITE, car)

    # -------------------------
    # SCORE DISPLAY (TOP RIGHT)
    # -------------------------
    score_text = font.render(f"Coins: {coin_score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 140, 10))

    # -------------------------
    # UPDATE SCREEN
    # -------------------------
    pygame.display.update()
    clock.tick(60)

pygame.quit()