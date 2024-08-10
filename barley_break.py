import pygame
import sys
import random

pygame.init()

# Размер окна
WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // 4
WINDOW_SIZE = WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Пятнашки")

# Шрифт
font = pygame.font.Font(None, 100)

# Создание списка плиток
tiles = list(range(1, 16))
tiles.append(0)
random.shuffle(tiles)


# Функция для рисования плиток
def draw_tiles():
    screen.fill(WHITE)
    for i in range(4):
        for j in range(4):
            value = tiles[i * 4 + j]
            if value != 0:
                pygame.draw.rect(screen, GRAY, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)
    pygame.display.flip()


# Функция для перемещения плитки
def move_tile(index):
    empty_index = tiles.index(0)
    if empty_index in [index - 1, index + 1, index - 4, index + 4]:
        tiles[empty_index], tiles[index] = tiles[index], tiles[empty_index]


# Главный игровой цикл
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                index = row * 4 + col
                move_tile(index)

        draw_tiles()


# Запуск игры
if __name__ == "__main__":
    main()
