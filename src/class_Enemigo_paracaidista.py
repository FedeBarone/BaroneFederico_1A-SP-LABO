import pygame
from configuracion import*

class Enemigo_paracaidista(pygame.sprite.Sprite):
    def __init__(self, animaciones_enemigo_paracaidista_cayendo: pygame.Surface):
        super().__init__()
        #===ANIMACIONES ENEMIGO===
        self.animaciones_fake_mask_cayendo = animaciones_enemigo_paracaidista_cayendo
        #===INDICE ENEMIGO===
        self.indice = 0
        #===SUPERFICIE Y RECT DEL ENEMIGO===
        self.image = self.animaciones_fake_mask_cayendo[self.indice]
        self.rect = self.image.get_rect()
        #===DIRECCION MOVIMIENTO ENEMIGO===
        self.velocidad_y = 4
        
    def update(self):
        #movimiento vertical
        self.rect.y += self.velocidad_y

        if self.rect.y >= ABAJO_PANTALLA:
                self.rect.y = ARRIBA_PANTALLA

        self.indice += 0.1
        if self.indice >= len(self.animaciones_fake_mask_cayendo):
            self.indice = 0
        self.image =  self.animaciones_fake_mask_cayendo[int(self.indice)]
