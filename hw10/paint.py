import pygame
import math

pygame.init()

# экран
WIDTH, HEIGHT = 900, 600
UI_HEIGHT = 70

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Improved Paint")

clock = pygame.time.Clock()

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
GRAY = (220, 220, 220)
DARK = (180, 180, 180)
ACTIVE = (120, 200, 255)

screen.fill(WHITE)

# состояние
tool = "brush"
color = BLACK

start_pos = None
drawing = False


# кнопки
brush_btn = pygame.Rect(150, 15, 80, 40)
rect_btn = pygame.Rect(240, 15, 80, 40)
circle_btn = pygame.Rect(330, 15, 80, 40)
eraser_btn = pygame.Rect(420, 15, 80, 40)

# цветовые кнопки
red_btn = pygame.Rect(10, 15, 30, 30)
green_btn = pygame.Rect(50, 15, 30, 30)
blue_btn = pygame.Rect(90, 15, 30, 30)


def draw_button(rect, text, active=False):
    pygame.draw.rect(screen, ACTIVE if active else DARK, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    font = pygame.font.SysFont(None, 22)
    img = font.render(text, True, BLACK)
    screen.blit(img, (rect.x + 8, rect.y + 12))


def draw_ui():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, UI_HEIGHT))

    # цвета
    pygame.draw.rect(screen, RED, red_btn)
    pygame.draw.rect(screen, GREEN, green_btn)
    pygame.draw.rect(screen, BLUE, blue_btn)

    # инструменты
    draw_button(brush_btn, "Brush", tool == "brush")
    draw_button(rect_btn, "Rect", tool == "rect")
    draw_button(circle_btn, "Circle", tool == "circle")
    draw_button(eraser_btn, "Eraser", tool == "eraser")

    # текущий цвет
    pygame.draw.rect(screen, color, (520, 20, 40, 30))
    pygame.draw.rect(screen, BLACK, (520, 20, 40, 30), 2)


running = True
while running:
    clock.tick(60)

    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # если клик по UI — НЕ рисуем
            if y <= UI_HEIGHT:

                # выбор цвета
                if red_btn.collidepoint(event.pos):
                    color = RED
                elif green_btn.collidepoint(event.pos):
                    color = GREEN
                elif blue_btn.collidepoint(event.pos):
                    color = BLUE

                # инструменты
                elif brush_btn.collidepoint(event.pos):
                    tool = "brush"
                elif rect_btn.collidepoint(event.pos):
                    tool = "rect"
                elif circle_btn.collidepoint(event.pos):
                    tool = "circle"
                elif eraser_btn.collidepoint(event.pos):
                    tool = "eraser"

            else:
                # старт фигур
                if tool in ["rect", "circle"]:
                    start_pos = event.pos
                    drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "rect" and start_pos:
                end = event.pos

                x = min(start_pos[0], end[0])
                y = min(start_pos[1], end[1])
                w = abs(start_pos[0] - end[0])
                h = abs(start_pos[1] - end[1])

                pygame.draw.rect(screen, color, (x, y, w, h), 2)

            elif tool == "circle" and start_pos:
                end = event.pos

                radius = int(math.hypot(
                    end[0] - start_pos[0],
                    end[1] - start_pos[1]
                ))

                pygame.draw.circle(screen, color, start_pos, radius, 2)

            start_pos = None
            drawing = False

    # рисование мышью
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        # только на canvas
        if pos[1] > UI_HEIGHT:

            if tool == "brush":
                pygame.draw.circle(screen, color, pos, 5)

            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, pos, 15)

    pygame.display.flip()

pygame.quit()