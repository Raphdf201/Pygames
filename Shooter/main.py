import pygame
from game import Game
from player import Player

pygame.init()

# Fenêtre
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')
game = Game()

running = True
while running:
    screen.blit(background, (0, -200))
    screen.blit(game.player.sprite, game.player.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("Input : D")
                game.player.move_right()
            elif event.key == pygame.K_a:
                print("Input : A")
                game.player.move_left()
            elif event.key == pygame.K_LEFT:
                print("Input : LEFT")
                game.player.move_left()
            elif event.key == pygame.K_RIGHT:
                print("Input : RIGHT")
                game.player.move_right()
