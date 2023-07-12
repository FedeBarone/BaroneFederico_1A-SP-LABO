import pygame
from configuracion import*
        
class Enemigo_aereo(pygame.sprite.Sprite):
    def __init__(self, animaciones_enemigo_aereo_izquierda: pygame.Surface, animaciones_enemigo_aereo_derecha: pygame.Surface):
        super().__init__()
        #===ANIMACIONES ENEMIGO===
        self.animaciones_izquierda = animaciones_enemigo_aereo_izquierda
        self.animaciones_derecha = animaciones_enemigo_aereo_derecha
        #===INDICE ENEMIGO===
        self.indice = 0
        #===SUPERFICIE Y RECT DEL ENEMIGO===
        self.image = self.animaciones_izquierda[self.indice]  # Corregido a animaciones_izquierda
        self.rect = self.image.get_rect()
        #===DIRECCION MOVIMIENTO ENEMIGO===
        self.direccion = 3
        
    def update(self):
        # Movimiento horizontal
        self.rect.x += self.direccion

        # Rebote en los límites horizontales
        if self.rect.left <= IZQUIERDA_PANTALLA:
            self.direccion = 3  # Cambia la dirección a izquierda cuando choca con el límite izquierdo

        elif self.rect.right >= DERECHA_PANTALLA:
            self.direccion = -3 # Cambia la dirección a derecha cuando choca con el límite derecho

        self.rect.bottom = ALTO_PANTALLA - 400

        # Actualizar imagen del enemigo
        if self.direccion == 3:
            # Caminando hacia la derecha
            self.indice += 0.1
            if self.indice >= len(self.animaciones_derecha):
                self.indice = 0
            self.image = self.animaciones_derecha[int(self.indice)]
        else:
            # Caminando hacia la izquierda
            self.indice += 0.1
            if self.indice >= len(self.animaciones_derecha):
                self.indice = 0
            self.image = self.animaciones_izquierda[int(self.indice)]
