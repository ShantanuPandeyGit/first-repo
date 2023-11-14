importpygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Create a snake
snake = pygame.Rect(100, 100, 20, 20)

# Create a food
food = pygame.Rect(200, 200, 20, 20)

# Create a clock
clock = pygame.time.Clock()

# Game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the snake
    snake.x += snake.dx
    snake.y += snake.dy

    # Check if the snake hit the wall
    if snake.x < 0 or snake.x >= 800 or snake.y < 0 or snake.y >= 600:
        game_over()

    # Check if the snake ate the food
    if snake.colliderect(food):
        snake.length += 1
        food.x = random.randint(0, 800)
        food.y = random.randint(0, 600)

    # Draw the snake
    pygame.draw.rect(screen, (255, 0, 0), snake)

    # Draw the food
    pygame.draw.rect(screen, (0, 255, 0), food)

    # Update the screen
    pygame.display.update()

    # Delay
    clock.tick(10)

# Game over function
def game_over():
    pygame.quit()
    sys.exit()