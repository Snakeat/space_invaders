import pygame 

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """creating bullet"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 7, 14)
        self.color = 204, 220, 57
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """bullet move"""
        self.y -= self.speed 
        self.rect.y = self.y 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)