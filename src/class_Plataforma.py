import pygame
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, tam:tuple, imagen:str):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imagen).convert_alpha(), (tam))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
