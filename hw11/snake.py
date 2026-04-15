import pygame
import random
import sys

pygame.init()

# -------------------- SETTINGS --------------------
WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Food Size & Timer")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# -------------------- SNAKE --------------------
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL, 0)

# -------------------- FOOD --------------------
def spawn_food():
    """
    Create food with:
    - random position
    - random weight (1-3)
    - timer (lifetime)
    """
    while True:
        x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL

        if (x, y) not in snake:
            weight = random.choice([1, 2, 3])

            lifetime = random.randint(3000, 7000)  # 3–7 сек
            spawn_time = pygame.time.get_ticks()

            return {
                "pos": (x, y),
                "weight": weight,
                "spawn_time": spawn_time,
                "lifetime": lifetime
            }

food = spawn_food()

# -------------------- GAME STATE --------------------
score = 0
font = pygame.font.SysFont(None, 30)
speed = 8


def draw():
    """Draw everything"""

    screen.fill(BLACK)

    # ---- draw snake ----
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL, CELL))

    # ---- draw food ----
    fx, fy = food["pos"]
    weight = food["weight"]

    # цвет зависит от веса
    if weight == 1:
        color = RED
    elif weight == 2:
        color = YELLOW
    else:
        color = WHITE

    # 🔥 РАЗНЫЙ РАЗМЕР еды
    size = CELL - (3 - weight) * 6
    offset = (CELL - size) // 2

    pygame.draw.rect(
        screen,
        color,
        (fx + offset, fy + offset, size, size)
    )

    # ---- UI ----
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()


def move_snake():
    """Move snake and check collisions"""

    global food, score

    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)

    # ---- WALL COLLISION ----
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_over()

    # ---- SELF COLLISION ----
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # ---- FOOD COLLISION ----
    if new_head == food["pos"]:
        score += food["weight"]  # вес влияет на очки
        food = spawn_food()
    else:
        snake.pop()


def check_food_timer():
    """Remove food after time expires"""

    global food

    current_time = pygame.time.get_ticks()

    if current_time - food["spawn_time"] > food["lifetime"]:
        food = spawn_food()


def game_over():
    pygame.quit()
    sys.exit()


# -------------------- MAIN LOOP --------------------
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---- CONTROLS ----
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    move_snake()
    check_food_timer()  # проверка исчезновения еды
    draw()

pygame.quit()