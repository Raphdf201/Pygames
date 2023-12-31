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
    game.player.all_projectiles.draw(screen)
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 900:
        game.player.move_right()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
    elif game.pressed.get(pygame.K_a) and game.player.rect.x > -30:
        game.player.move_left()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -30:
        game.player.move_left()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
