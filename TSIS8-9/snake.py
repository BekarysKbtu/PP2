import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position and speed
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)  # Start moving right initially
snake_speed = 5
snake_speed_increase = 1

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score and level
score = 0
level = 1
foods_eaten = 0

# Walls
walls = []  # List to store wall positions


# Function to generate random walls
def generate_random_walls():
    global walls
    walls = []  # Clear existing walls

    # Generate 6 random walls at random positions
    for _ in range(6):
        while True:
            wall_length = random.randint(2, 3)  # Random length of the wall (2 or 3 blocks)
            wall_direction = random.choice(['horizontal', 'vertical'])  # Random direction of the wall
            wall_start = (
            random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))  # Random start position

            # Generate wall positions based on direction and length
            if wall_direction == 'horizontal':
                wall_positions = [(wall_start[0] + i, wall_start[1]) for i in range(wall_length)]
            else:
                wall_positions = [(wall_start[0], wall_start[1] + i) for i in range(wall_length)]

            # Check if the wall positions are too close to existing walls
            if all(wall not in walls and wall not in snake for wall in wall_positions):
                walls.extend(wall_positions)
                break


# Generate initial walls
generate_random_walls()


# Function to draw the snake
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Function to draw the food
def draw_food():
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Function to draw the walls
def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, WHITE, (wall[0] * GRID_SIZE, wall[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Function to check for collisions with walls
def check_wall_collisions():
    if snake[0] in walls:
        return True
    return False


# Function to check for collisions
def check_collisions():
    # Check if the snake collides with itself
    if snake[0] in snake[1:]:
        return True

    # Check if the snake collides with the walls or leaves the playing area
    if snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT:
        return True

    # Check for collisions with walls
    if check_wall_collisions():
        return True

    return False


# Function to handle input events
def handle_input():
    global snake_direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction[1] == 0:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction[1] == 0:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction[0] == 0:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction[0] == 0:
                snake_direction = (1, 0)


# Function to update the game state
def update():
    global food, snake, snake_speed, score, level, foods_eaten

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Check for collisions
    if check_collisions():
        return True

    # Check if the snake eats the food
    if snake[0] == food:
        snake.append(snake[-1])  # Increase the length of the snake
        score += 10
        foods_eaten += 1

        # Generate new food position
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in snake and food not in walls:
                break

        # Increase speed and level after eating certain number of foods
        if foods_eaten >= 3:
            foods_eaten = 0
            level += 1
            snake_speed += snake_speed_increase

    return False


# Function to display "You've lost" message
def display_loss_message():
    font = pygame.font.Font(None, 60)
    text = font.render("You've lost", True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))


# Function to display game statistics
def display_statistics():
    font = pygame.font.Font(None, 36)
    level_text = font.render(f"Level: {level}", True, WHITE)
    food_eaten_text = font.render(f"Food Eaten: {foods_eaten}", True, WHITE)
    screen.blit(level_text, (10, 10))
    screen.blit(food_eaten_text, (10, 50))


# Main game loop
clock = pygame.time.Clock()

game_over = False
while not game_over:
    handle_input()
    game_over = update()

    # Draw everything
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    draw_walls()

    # Display statistics
    display_statistics()

    if game_over:
        display_loss_message()

    pygame .display.update()
    clock.tick(snake_speed)

