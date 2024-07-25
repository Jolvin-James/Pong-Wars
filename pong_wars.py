import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Define colors
DAY_COLOR = (209, 232, 227)
NIGHT_COLOR = (23, 43, 54)
DAY_BALL_COLOR = NIGHT_COLOR
NIGHT_BALL_COLOR = DAY_COLOR

# Define screen size
screen_width = 800
screen_height = 800

# Define square size
SQUARE_SIZE = 25

# Define the number of squares
num_squares_x = screen_width // SQUARE_SIZE
num_squares_y = screen_height // SQUARE_SIZE

# Initialize Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Wars")

# Initialize clock for controlling the frame rate
clock = pygame.time.Clock()

# Initialize font
font = pygame.font.Font(None, 36)

# Initialize squares array
squares = [[DAY_COLOR if i < num_squares_x / 2 else NIGHT_COLOR for j in range(num_squares_y)] for i in range(num_squares_x)]

# Initialize ball positions and velocities
x1, y1 = screen_width // 4, screen_height // 2
dx1, dy1 = 12.5, -12.5

x2, y2 = (screen_width // 4) * 3, screen_height // 2
dx2, dy2 = -12.5, 12.5

# Initialize iteration count
iteration = 0

# Function to draw ball
def draw_ball(x, y, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), SQUARE_SIZE // 2)

# Function to draw squares
def draw_squares():
    for i in range(num_squares_x):
        for j in range(num_squares_y):
            pygame.draw.rect(screen, squares[i][j], (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to update square and bounce ball
def update_square_and_bounce(x, y, dx, dy, color):
    updated_dx, updated_dy = dx, dy

    # Check multiple points around the ball's circumference
    for angle in range(0, 360, 45):
        angle_rad = math.radians(angle)
        check_x = x + math.cos(angle_rad) * (SQUARE_SIZE / 2)
        check_y = y + math.sin(angle_rad) * (SQUARE_SIZE / 2)

        i = int(check_x // SQUARE_SIZE)
        j = int(check_y // SQUARE_SIZE)

        if 0 <= i < num_squares_x and 0 <= j < num_squares_y:
            if squares[i][j] != color:
                squares[i][j] = color

                # Determine bounce direction based on the angle
                if abs(math.cos(angle_rad)) > abs(math.sin(angle_rad)):
                    updated_dx = -updated_dx
                else:
                    updated_dy = -updated_dy

                # Add some randomness to the bounce
                updated_dx += random.uniform(-0.01, 0.01)
                updated_dy += random.uniform(-0.01, 0.01)

    return updated_dx, updated_dy

# Function to update score element
def update_score_element():
    day_score = sum(row.count(DAY_COLOR) for row in squares)
    night_score = sum(row.count(NIGHT_COLOR) for row in squares)
    score_text = f"day {day_score} | night {night_score}"
    score_surface = font.render(score_text, True, DAY_COLOR)
    screen.blit(score_surface, (20, 30))

# Function to check boundary collision
def check_boundary_collision(x, y, dx, dy):
    if x + dx > screen_width - SQUARE_SIZE / 2 or x + dx < SQUARE_SIZE / 2:
        dx = -dx
    if y + dy > screen_height - SQUARE_SIZE / 2 or y + dy < SQUARE_SIZE / 2:
        dy = -dy

    return dx, dy

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic
    iteration += 1
    if iteration % 1000 == 0:
        print("iteration", iteration)

    # Draw background and squares
    screen.fill(DAY_COLOR)
    draw_squares()

    # Draw and update ball 1
    draw_ball(x1, y1, DAY_BALL_COLOR)
    dx1, dy1 = update_square_and_bounce(x1, y1, dx1, dy1, DAY_COLOR)
    dx1, dy1 = check_boundary_collision(x1, y1, dx1, dy1)
    x1 += dx1
    y1 += dy1

    # Draw and update ball 2
    draw_ball(x2, y2, NIGHT_BALL_COLOR)
    dx2, dy2 = update_square_and_bounce(x2, y2, dx2, dy2, NIGHT_COLOR)
    dx2, dy2 = check_boundary_collision(x2, y2, dx2, dy2)
    x2 += dx2
    y2 += dy2

    # Update score element
    update_score_element()

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()