import pygame
from configuracion import*
class Bola_fuego(pygame.sprite.Sprite):
    def __init__(self, mitad_abajo: tuple, velocidad: int) -> None:
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/bola_fuego.png"), (TAM_BOLA_FUEGO))
        self.rect = self.image.get_rect()
        self.rect.midbottom = mitad_abajo
        self.velocidad_x = velocidad
    
    def update(self):
        self.rect.x += self.velocidad_x
