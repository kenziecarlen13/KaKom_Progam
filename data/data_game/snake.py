import pygame
import random

pygame.init()

# Konstanta
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ular Memakan Apel")

clock = pygame.time.Clock()

def get_random_apple(snake):
    """Menghasilkan posisi apel yang tidak bertabrakan dengan ular."""
    while True:
        apple = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
        if apple not in snake:
            return apple

def draw_button(text, x, y, w, h, color):
    """Menggambar tombol dan mengembalikan True jika ditekan."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font(None, 30)
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 10, y + 10))

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        if click[0] == 1:
            pygame.time.delay(200)  # Hindari double-click cepat
            return True
    return False

def login_screen():
    """Tampilan login sebelum game dimulai."""
    logged_in = False
    paid = False

    while not (logged_in and paid):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 40)

        if not logged_in:
            text = font.render("Login dengan akun Google", True, WHITE)
            screen.blit(text, (WIDTH // 6, HEIGHT // 4))
            if draw_button("Login", WIDTH // 3, HEIGHT // 3, 150, 50, BLUE):
                logged_in = True  # Perbarui status login

        elif not paid:
            text = font.render("Bayar untuk bermain", True, WHITE)
            screen.blit(text, (WIDTH // 4, HEIGHT // 4))
            if draw_button("Pay", WIDTH // 3, HEIGHT // 3, 150, 50, GREEN):
                paid = True  # Perbarui status pembayaran

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def run_game():
    snake = [(100, 100)]
    direction = (GRID_SIZE, 0)
    score = 0
    apple = get_random_apple(snake)
    running = True

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Cek tabrakan
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
            return show_game_over(score)

        snake.insert(0, new_head)
        
        if new_head == apple:
            apple = get_random_apple(snake)
            score += 1
        else:
            snake.pop()
        
        # Gambar ular dan apel
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (apple[0], apple[1], GRID_SIZE, GRID_SIZE))
        
        # Tampilkan skor
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        
        clock.tick(9 + score // 5)

def show_game_over(score):
    """Tampilkan layar game over."""
    screen.fill(BLACK)
    font = pygame.font.Font(None, 50)
    
    game_over_text = font.render("Game Over", True, RED)
    final_score_text = font.render(f"Skor Akhir: {score}", True, WHITE)
    restart_text = font.render("Tekan 'R' untuk Restart", True, WHITE)
    quit_text = font.render("Tekan 'Q' untuk Keluar", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 4))
    screen.blit(final_score_text, (WIDTH // 3, HEIGHT // 3))
    screen.blit(restart_text, (WIDTH // 4, HEIGHT // 2))
    screen.blit(quit_text, (WIDTH // 4, HEIGHT // 2 + 40))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False

# Main Loop
login_screen()  # Tampilkan layar login sebelum memulai permainan
while True:
    if not run_game():
        break

pygame.quit()
