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
MAX_SCORE = 5
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

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

# Fungsi untuk menampilkan layar akhir
def show_winner(winner_text):
    screen.fill(BLACK)
    text = big_font.render(winner_text, True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(3000)

# Loop utama
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Kontrol pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= paddle_speed
        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += paddle_speed

        # AI lawan
        if opponent.top < ball.y:
            opponent.y += paddle_speed
        if opponent.bottom > ball.y:
            opponent.y -= paddle_speed

        # Gerakan bola
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Tabrakan bola
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
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

        # Cek kemenangan
        if player_score >= MAX_SCORE:
            game_over = True
            show_winner("Player Wins!")
        elif opponent_score >= MAX_SCORE:
            game_over = True
            show_winner("Opponent Wins!")

        draw_objects()
        pygame.display.flip()
        clock.tick(FPS)
    else:
        # Setelah game over, tekan tombol apa saja untuk keluar
        keys = pygame.key.get_pressed()
        if any(keys):
            running = False

pygame.quit()
sys.exit()
