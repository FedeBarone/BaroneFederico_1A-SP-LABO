import pygame
from configuracion import*
from otros_sprites import*

class Minotauro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #===ANIMACIONES ENEMIGO===
        self.animaciones_minotauro_caminando_derecha = obtener_animaciones_minotauro_caminando_derecha()
        self.animaciones_minotauro_caminando_izquierda = obtener_animaciones_minotauro_caminando_izquierda(self.animaciones_minotauro_caminando_derecha)
        #===INDICE ENEMIGO===
        self.indice = 0
        #===SUPERFICIE Y RECT DEL ENEMIGO===
        self.image =  self.animaciones_minotauro_caminando_derecha[self.indice]
        self.rect = self.image.get_rect()
        #===DIRECCION MOVIMIENTO ENEMIGO===
        self.direccion = -3  # Iniciar moviéndose hacia la derecha
        
    def update(self):
        #movimiento horizontal
        self.rect.x += self.direccion# Mover en la dirección actual

        # Rebote en los límites horizontales
        if self.rect.left <= IZQUIERDA_PANTALLA:
            self.direccion = 3  # Cambiar dirección
        elif self.rect.right >= DERECHA_PANTALLA:
            self.direccion = -3

        self.rect.bottom = ALTO_PANTALLA - 26
        
        # Actualizar imagen del enemigo
        if self.direccion == 3:
            # Caminando hacia la derecha
            self.indice += 0.1
            if self.indice >= len(self.animaciones_minotauro_caminando_derecha):
                self.indice = 0
            self.image = self.animaciones_minotauro_caminando_derecha[int(self.indice)]
        else:
            # Caminando hacia la izquierda
            self.indice += 0.1
            if self.indice >= len(self.animaciones_minotauro_caminando_izquierda):
                self.indice = 0
            self.image = self.animaciones_minotauro_caminando_izquierda[int(self.indice)]

