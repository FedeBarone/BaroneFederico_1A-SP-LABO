import pygame
from configuracion import*
from otros_sprites import*

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #===ANIMACIONES ENEMIGO===
        self.animaciones_dragon_caminando_izquierda = obtener_animaciones_dragon_caminando_izquierda()
        self.animaciones_dragon_caminando_derecha = obtener_animaciones_dragon_caminando_derecha(self.animaciones_dragon_caminando_izquierda)
        #===INDICE ENEMIGO===
        self.indice = 0
        #===SUPERFICIE Y RECT DEL ENEMIGO===
        self.image =  self.animaciones_dragon_caminando_izquierda[self.indice]
        self.rect = self.image.get_rect()
        #===DIRECCION MOVIMIENTO ENEMIGO===
        self.direccion = -2 
        
    def update(self):
        #movimiento horizontal
        self.rect.x += self.direccion

        # Rebote en los límites horizontales
        if self.rect.left <= IZQUIERDA_PANTALLA:
            self.direccion = 2  # Cambiar dirección
        elif self.rect.right >= DERECHA_PANTALLA:
            self.direccion = -2

        self.rect.bottom = ALTO_PANTALLA - 26
        
        # Actualizar imagen del enemigo
        if self.direccion == 2:
            # Caminando hacia la derecha
            self.indice += 0.1
            if self.indice >= len(self.animaciones_dragon_caminando_derecha):
                self.indice = 0
            self.image = self.animaciones_dragon_caminando_derecha[int(self.indice)]
        else:
            # Caminando hacia la izquierda
            self.indice += 0.1
            if self.indice >= len(self.animaciones_dragon_caminando_izquierda):
                self.indice = 0
            self.image = self.animaciones_dragon_caminando_izquierda[int(self.indice)]
            