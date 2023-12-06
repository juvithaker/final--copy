# main_menu.py

import pygame
from utils import blit_text_center

def main_menu():
    pygame.init()

    # Set up your main menu screen, blit images, and handle events
    # For simplicity, we'll just display a basic menu with a "Start" option

    WIDTH, HEIGHT = 800, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Racing Game - Main Menu")

    run_menu = True
    clock = pygame.time.Clock()

    while run_menu:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_menu = False  # Exit the menu and start the game

        WIN.fill((0, 0, 0))  # Fill the screen with a black background

        # Display the menu text
        blit_text_center(WIN, pygame.font.SysFont("comicsans", 44), "Car Racing Game", HEIGHT // 4)
        blit_text_center(WIN, pygame.font.SysFont("comicsans", 28), "Press SPACE to start", HEIGHT // 2)

        pygame.display.flip()

    pygame.quit()