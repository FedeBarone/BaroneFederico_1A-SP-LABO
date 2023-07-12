import pygame
from configuracion import*
from class_Bola_fuego import Bola_fuego
from img_sprites import*
from sonidos import*

class Personaje(pygame.sprite.Sprite):
#===================================================================================================================================
    def __init__(self, piso:pygame.Surface):
        super().__init__()
        #===ANIMACIONES PERSONAJE===
        self.animaciones_personaje_caminando_derecha = obtener_animaciones_personaje_caminando_derecha()
        self.animaciones_personaje_caminando_izquierda = obtener_animaciones_personaje_caminando_izquierda(
            self.animaciones_personaje_caminando_derecha)
        self.animaciones_personaje_inactivo_derecha =  obtener_animaciones_personaje_inactivo_derecha()
        self.animaciones_personaje_inactivo_izquierda = obtener_animaciones_personaje_inactivo_izquierda(
            self.animaciones_personaje_inactivo_derecha)
        self.animacion_personaje_salta_derecha = obtener_animacion_personaje_salta_derecha()
        self.animacion_personaje_salta_izquierda = obtener_animacion_personaje_salta_izquierda(self.animacion_personaje_salta_derecha)
        self.animacion_disparo_bola_fuego_derecha = obtener_animaciones_disparo_bola_fuego()
        self.animacion_disparo_bola_fuego_izquierda = obtener_animaciones_disparo_bola_fuego_izquierda(
            self.animacion_disparo_bola_fuego_derecha)
        self.animacion_personaje_danio_derecha = obtener_animaciones_danio_derecha()
        self.animacion_personaje_danio_izquierda = obtener_animaciones_danio_izquierda(self.animacion_personaje_danio_derecha)
        #===SONIDOS PERSONAJE===
        self.sonido_bola_fuego = obtener_sonido_bola_fuego()
        self.sonido_salto = obtener_sonido_salto_personaje()
        #===INDICE PERSONAJE===
        self.indice = 0
        #===SALTO PERSONAJE===
        self.salto = 0
        #===SUPERFICIE Y RECT DEL PERSONAJE===
        self.image = self.animaciones_personaje_caminando_derecha[self.indice]
        self.rect = self.image.get_rect()
        #===VELOCIDAD EJE X E Y DEL PERSONAJE===
        self.velocidad_x = 0
        self.velocidad_y = 0
        #===BANDERAS PERSONAJE===
        self.saltando = False
        self.derecha = True
        self.disparando = False
        self.golpeado = False
        #===GRAVEDAD PERSONAJE===
        self.gravedad = 1
        #===PISO PERSONAJE===
        self.piso = piso
        self.rect.bottomleft = (0, ABAJO_PANTALLA -25)
    #===================================================================================================================================
    def mover_personaje(self):
        #movimiento horizontal
        self.rect.x += self.velocidad_x
    
    def saltar(self):
        if self.salto == 0:
            self.velocidad_y = -24
            self.salto = 1
            self.sonido_salto.play()
        
        if not self.saltando:
            self.saltando = True
    
    def animar_personaje(self):
        #cambio imagen del personaje
        #derecha
        if self.golpeado:
            if self.derecha:
                    self.indice += 0.1
                    if self.indice >= len(self.animacion_personaje_danio_derecha):
                        self.indice = 0
                        self.golpeado = False
                    self.image = self.animacion_personaje_danio_derecha[int(self.indice)]
            else:
                self.indice += 0.1
                if self.indice >= len(self.animacion_personaje_danio_izquierda):
                    self.indice = 0
                    self.golpeado = False
                self.image = self.animacion_personaje_danio_izquierda[int(self.indice)]
        else:
            if not self.disparando:
                #derecha
                if self.velocidad_x > 0:
                    self.derecha = True
                    #salta
                    if self.saltando:
                        self.indice = 0
                        self.image = self.animacion_personaje_salta_derecha[int(self.indice)]
                    #camina
                    else:
                        self.indice += 0.1
                        if self.indice >= len(self.animaciones_personaje_caminando_derecha):
                            self.indice = 0
                        self.image = self.animaciones_personaje_caminando_derecha[int(self.indice)]
                #izquierda
                elif self.velocidad_x < 0:
                    self.derecha = False
                    #salta
                    if self.saltando:
                        self.indice = 0
                        self.image = self.animacion_personaje_salta_izquierda[int(self.indice)]
                    #camina
                    else:
                        self.indice += 0.1
                        if self.indice >= len(self.animaciones_personaje_caminando_izquierda):
                            self.indice = 0
                        self.image = self.animaciones_personaje_caminando_izquierda[int(self.indice)]
                
                elif self.velocidad_x == 0 and not self.saltando:
                    if self.derecha:
                        self.indice += 0.1
                        if self.indice >= len(self.animaciones_personaje_inactivo_derecha):
                            self.indice = 0
                        self.image = self.animaciones_personaje_inactivo_derecha[int(self.indice)]
                    else:
                        self.indice += 0.1
                        if self.indice >= len(self.animaciones_personaje_inactivo_izquierda):
                            self.indice = 0
                        self.image = self.animaciones_personaje_inactivo_izquierda[int(self.indice)]
               
                elif self.velocidad_x == 0 and self.saltando:
                    if self.derecha:
                        self.indice = 0
                        self.image = self.animacion_personaje_salta_derecha[int(self.indice)]
                    else:
                        self.indice = 0
                        self.image = self.animacion_personaje_salta_izquierda[int(self.indice)]
            else:
                if self.derecha:
                    self.indice += 0.1
                    if self.indice >= len(self.animacion_disparo_bola_fuego_derecha):
                        self.indice = 0
                        self.disparando = False
                    self.image = self.animacion_disparo_bola_fuego_derecha[int(self.indice)]
                else:
                    self.indice += 0.1
                    if self.indice >= len(self.animacion_disparo_bola_fuego_izquierda):
                        self.indice = 0
                        self.disparando = False
                    self.image = self.animacion_disparo_bola_fuego_izquierda[int(self.indice)]
    
    def setear_limites_pantalla_personaje(self):
        #compruebo limites
        if self.rect.left <= IZQUIERDA_PANTALLA:
            self.rect.left = IZQUIERDA_PANTALLA
        elif self.rect.right >= ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA

        if self.rect.top <= ARRIBA_PANTALLA:
            self.velocidad_y = 1
        

    def disparar_bola_fuego(self, velocidad: int, sprites, bolas_fuego):
        if self.derecha:
            bola_fuego = Bola_fuego(self.rect.midright, velocidad)
        else:
            bola_fuego = Bola_fuego(self.rect.midleft, -velocidad)

        self.sonido_bola_fuego.play()
        sprites.add(bola_fuego)
        bolas_fuego.add(bola_fuego)
        self.disparando = True

    def update(self):
        self.mover_personaje()
        self.animar_personaje()
        self.setear_limites_pantalla_personaje()

        #salto
        if self.salto != 0:
            self.rect.y += self.velocidad_y
            self.velocidad_y += self.gravedad

            if self.rect.bottom >= self.piso.rect.top:
                self.rect.bottom = self.piso.rect.top
                self.saltando = False
                self.salto = 0
                
        if self.rect.colliderect(self.piso.rect):
            print("colision piso")
            self.rect.bottom = self.piso.rect.top
            self.saltando = False 
            self.salto = 0 
            self.velocidad_y = 0

    def reiniciar(self):
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.rect.bottomleft = (0, ABAJO_PANTALLA -25)