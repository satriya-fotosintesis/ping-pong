import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kecepatan permainan
FPS = 60
clock = pygame.time.Clock()

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Bola
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Kecepatan paddle
paddle_speed = 7

# Skor
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Fungsi untuk menggambar objek
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Tampilkan skor
    player_text = font.render(f'{player_score}', True, WHITE)
    opponent_text = font.render(f'{opponent_score}', True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 20, 20))
    screen.blit(opponent_text, (WIDTH // 2 - 40, 20))

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= paddle_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += paddle_speed

    # AI lawan sederhana
    if opponent.top < ball.y:
        opponent.y += paddle_speed
    if opponent.bottom > ball.y:
        opponent.y -= paddle_speed

    # Gerakan bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Tabrakan bola dengan atas/bawah
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Tabrakan bola dengan paddle
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Skor
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    draw_objects()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

