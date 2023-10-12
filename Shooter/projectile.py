import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 3
        self.sprite = pygame.image.load('assets/projectile.png')
        self.rect = self.sprite.get_rect()
