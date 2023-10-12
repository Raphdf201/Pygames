import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.health_max = 100
        self.damage = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.sprite = pygame.image.load('Assets/player.png')
        self.rect = self.sprite.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def launch_projectile(self):
        projectile = Projectile()
        self.all_projectiles.add(projectile)

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
