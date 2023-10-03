import pygame
pygame.init()

# Fenêtre
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1600, 900))

background = pygame.image.load('assets/bg.jpg')

running = True
while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
