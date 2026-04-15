import pygame
import sys
import math

pygame.init()

# -------------------- SCREEN --------------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint - Shapes + Colors")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

screen.fill(WHITE)

# -------------------- STATE --------------------
tool = "square"
color = BLACK
start_pos = None

# -------------------- UI --------------------
font = pygame.font.SysFont(None, 22)

# инструменты
square_btn = pygame.Rect(10, 10, 100, 30)
rt_btn = pygame.Rect(120, 10, 150, 30)
eq_btn = pygame.Rect(280, 10, 170, 30)
rhomb_btn = pygame.Rect(460, 10, 120, 30)

# цвета
color_buttons = [
    (RED, pygame.Rect(10, 50, 30, 30)),
    (GREEN, pygame.Rect(50, 50, 30, 30)),
    (BLUE, pygame.Rect(90, 50, 30, 30)),
    (BLACK, pygame.Rect(130, 50, 30, 30)),
    (YELLOW, pygame.Rect(170, 50, 30, 30)),
]


def draw_ui():
    """Draw UI panel"""

    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 90))

    # кнопки инструментов
    pygame.draw.rect(screen, GRAY, square_btn)
    pygame.draw.rect(screen, GRAY, rt_btn)
    pygame.draw.rect(screen, GRAY, eq_btn)
    pygame.draw.rect(screen, GRAY, rhomb_btn)

    screen.blit(font.render("Square", True, BLACK), (20, 15))
    screen.blit(font.render("Right Triangle", True, BLACK), (130, 15))
    screen.blit(font.render("Equilateral", True, BLACK), (290, 15))
    screen.blit(font.render("Rhombus", True, BLACK), (470, 15))

    # кнопки цветов
    for col, rect in color_buttons:
        pygame.draw.rect(screen, col, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # текущий цвет
    pygame.draw.rect(screen, color, (250, 50, 40, 30))
    pygame.draw.rect(screen, BLACK, (250, 50, 40, 30), 2)

    screen.blit(font.render("Current", True, BLACK), (250, 35))


# -------------------- SHAPES --------------------
def draw_square(start, end):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    size = max(abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, (x, y, size, size), 2)


def draw_right_triangle(start, end):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(screen, color, points, 2)


def draw_equilateral_triangle(start, end):
    x1, y1 = start
    x2, y2 = end
    base = abs(x2 - x1)
    height = int(base * math.sqrt(3) / 2)

    p1 = (x1, y2)
    p2 = (x2, y2)
    p3 = (x1 + base // 2, y2 - height)

    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)


def draw_rhombus(start, end):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(screen, color, points, 2)


# -------------------- MAIN LOOP --------------------
running = True
while running:
    clock.tick(60)

    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------------- CLICK ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:

            # выбор цвета
            for col, rect in color_buttons:
                if rect.collidepoint(event.pos):
                    color = col

            # выбор инструмента
            if square_btn.collidepoint(event.pos):
                tool = "square"
            elif rt_btn.collidepoint(event.pos):
                tool = "right"
            elif eq_btn.collidepoint(event.pos):
                tool = "equilateral"
            elif rhomb_btn.collidepoint(event.pos):
                tool = "rhombus"

            # начало рисования
            elif event.pos[1] > 90:
                start_pos = event.pos

        # ---------------- DRAW ----------------
        elif event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos

            if tool == "square":
                draw_square(start_pos, end_pos)
            elif tool == "right":
                draw_right_triangle(start_pos, end_pos)
            elif tool == "equilateral":
                draw_equilateral_triangle(start_pos, end_pos)
            elif tool == "rhombus":
                draw_rhombus(start_pos, end_pos)

            start_pos = None

    pygame.display.flip()

pygame.quit()