import pygame
from configuracion import*
from otros_sprites import*

class Manzana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #===ANIMACIONES ENEMIGO===
        self.animaciones_manzana_wumpa = obtener_animaciones_manzana_wumpa()
        #===INDICE ENEMIGO===
        self.indice = 0
        #===SUPERFICIE Y RECT DEL ENEMIGO===
        self.image = self.animaciones_manzana_wumpa[self.indice]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.indice += 0.1
        if self.indice >= len(self.animaciones_manzana_wumpa):
            self.indice = 0
        self.image = self.animaciones_manzana_wumpa[int(self.indice)]
    

