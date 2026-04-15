import pygame
import random
import sys

pygame.init()

# -------------------- SCREEN --------------------
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer - Fixed Coins & Road")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 60, 60)
BLUE = (60, 60, 255)
GOLD = (255, 215, 0)
GRAY = (150, 150, 150)

# -------------------- ROAD LIMITS --------------------
ROAD_LEFT = 100
ROAD_RIGHT = 500

# -------------------- PLAYER --------------------
player = pygame.Rect(280, 600, 40, 60)
player_speed = 6

# -------------------- ENEMY --------------------
enemy = pygame.Rect(random.randint(ROAD_LEFT, ROAD_RIGHT), -100, 40, 60)
enemy_speed = 4

# -------------------- COIN --------------------
def spawn_coin():
    """Spawn coin only on road with random weight"""
    x = random.randint(ROAD_LEFT, ROAD_RIGHT)
    weight = random.choice([1, 2, 3])  # coin value
    return pygame.Rect(x, -50, 25, 25), weight

coin, coin_value = spawn_coin()

# -------------------- GAME STATE --------------------
score = 0
coins_collected = 0

COINS_FOR_SPEEDUP = 5  # N coins → speed up enemy

font = pygame.font.SysFont(None, 28)


def draw():
    """Draw everything"""

    screen.fill(GRAY)

    # road
    pygame.draw.rect(screen, BLACK, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))

    # player
    pygame.draw.rect(screen, BLUE, player)

    # enemy
    pygame.draw.rect(screen, RED, enemy)

    # coin (size depends on weight)
    radius = 8 + coin_value * 4
    pygame.draw.circle(screen, GOLD, coin.center, radius)

    # UI
    text = font.render(
        f"Score: {score}  Coins: {coins_collected}  Enemy Speed: {enemy_speed}",
        True,
        WHITE
    )
    screen.blit(text, (10, 10))

    pygame.display.flip()


def move_enemy():
    """Move enemy down and respawn"""
    global enemy

    enemy.y += enemy_speed

    if enemy.y > HEIGHT:
        enemy.x = random.randint(ROAD_LEFT, ROAD_RIGHT)
        enemy.y = -100


def move_coin():
    """Move coin down"""
    global coin, coin_value

    coin.y += 3

    if coin.y > HEIGHT:
        coin, coin_value = spawn_coin()


def check_collisions():
    """Check all collisions"""

    global score, coin, coin_value
    global coins_collected, enemy_speed

    # PLAYER - COIN
    if player.colliderect(coin):
        score += coin_value
        coins_collected += 1

        coin, coin_value = spawn_coin()

        # increase enemy speed every N coins
        if coins_collected % COINS_FOR_SPEEDUP == 0:
            enemy_speed += 1

    # PLAYER - ENEMY
    if player.colliderect(enemy):
        game_over()


def game_over():
    """End game"""
    pygame.quit()
    sys.exit()


# -------------------- MAIN LOOP --------------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- CONTROLS ----------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > ROAD_LEFT:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < ROAD_RIGHT - player.width:
        player.x += player_speed

    # ---------------- UPDATE ----------------
    move_enemy()
    move_coin()
    check_collisions()
    draw()

pygame.quit()