import pygame
import random
import sys

pygame.init()

# -------------------- SETTINGS --------------------
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Levels & Speed")

clock = pygame.time.Clock()

# цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# -------------------- SNAKE --------------------
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# -------------------- FOOD --------------------
def random_food():
    """Generate food that does not spawn on snake"""
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

food = random_food()

# -------------------- GAME STATE --------------------
score = 0
level = 1
foods_for_level = 0

speed = 8  # initial speed (FPS)

# font
font = pygame.font.SysFont(None, 30)


def draw():
    """Draw everything on screen"""

    screen.fill(BLACK)

    # snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))

    # food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # score + level
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()


def move_snake():
    """Move snake forward"""
    global food, score, foods_for_level, level, speed

    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)

    # ---------------- WALL COLLISION ----------------
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_over()

    # ---------------- SELF COLLISION ----------------
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # ---------------- FOOD COLLISION ----------------
    if new_head == food:
        score += 1
        foods_for_level += 1
        food = random_food()
    else:
        snake.pop()

    # ---------------- LEVEL SYSTEM ----------------
    if foods_for_level >= 3:
        level += 1
        foods_for_level = 0

        # 🔥 INCREASE SPEED (MAIN REQUEST)
        speed += 2


def game_over():
    """End game"""
    pygame.quit()
    sys.exit()


# -------------------- MAIN LOOP --------------------
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------------- CONTROLS ----------------
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    move_snake()
    draw()

pygame.quit()