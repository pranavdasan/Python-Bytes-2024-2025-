import pygame

# Initialize pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 300, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PLAYER_COLOR = (0, 255, 0)
GROUND_COLOR = (50, 205, 50)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Run Game")

# Game variables
player_size = 30
player_x, player_y = 50, HEIGHT - player_size - 20
player_velocity_y = 0
gravity = 1
jump_strength = -15
ground_level = HEIGHT - player_size - 20

# Ground dimensions
ground_height = 20
ground_y = HEIGHT - ground_height

# Obstacle variables
obstacle_width, obstacle_height = 30, 30
obstacle_x = WIDTH  # Start off-screen to the right
obstacle_speed = 5

# Initialize clock and score
clock = pygame.time.Clock()
score = 0

# Load font
font = pygame.font.Font(None, 36)

# Game loop
running = True

while running:
    screen.fill(WHITE)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y == ground_level:
        player_velocity_y = jump_strength

    # Update player position
    player_velocity_y += gravity
    player_y += player_velocity_y


    if player_y > ground_level:
        player_y = ground_level

    player = pygame.Rect(player_x, player_y, player_size, player_size)

    # Update obstacle position
    obstacle_x -= obstacle_speed

    # Reset obstacle position if it goes off-screen
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH
        score += 1

    # Check for collision
    obstacle = pygame.Rect(obstacle_x, ground_y - obstacle_height, obstacle_width, obstacle_height)
    if player.colliderect(obstacle):
        running = False  # Game over

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # Draw the obstacle as a red triangle
    pygame.draw.polygon(screen, RED, [
        (obstacle_x, ground_y),
        (obstacle_x + obstacle_width / 2, ground_y - obstacle_height),
        (obstacle_x + obstacle_width, ground_y)
    ])

    # Draw ground
    pygame.draw.rect(screen, GROUND_COLOR, (0, ground_y, WIDTH, ground_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Refresh screen
    pygame.display.update()
    clock.tick(30)

pygame.quit()