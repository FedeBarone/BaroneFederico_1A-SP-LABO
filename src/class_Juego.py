import pygame
import sys
from random import randrange
import json
from configuracion import *
from class_Personaje import Personaje
from class_Dragon import Dragon
from class_Luchador import Luchador
from class_Enemigo_aereo import Enemigo_aereo
from class_Minotauro import Minotauro
from class_Enemigo_paracaidista import Enemigo_paracaidista
from class_Plataforma import Plataforma
from class_Manzana import Manzana
from imagenes import*
from sonidos import*
from plataformas import*
from img_sprites import*

class Juego:
#===================================================CONSTRUCTOR===========================================================================
    def __init__(self) -> None:
        pygame.init()
    #===RELOJ===
        self.RELOJ = pygame.time.Clock()
    #===PANTALLA===
        self.PANTALLA = pygame.display.set_mode(TAM_PANTALLA)
        self.nombre_pantalla = pygame.display.set_caption("Dino Rage")
    #===ICONO===
        self.icono = obtener_icono_juego()
        pygame.display.set_icon(self.icono)
    #====FUENTE===
        self.fuente = obtener_fuente()
    #===FONDOS / SONIDOS===
        #FONDO / SONIDO MENU PRINCIPAL
        self.fondo = obtener_fondo_menu_principal()
        self.fondo_sonido = obtener_sonido_menu_principal()
        self.fondo_game_over = obtener_fondo_game_over()
        self.fondo_sonido.play(loops = -1)
        self.fondo_sonido.set_volume(0.5)
        #FONDO / SONIDO NIVEL 1
        self.fondo_nivel_uno = obtener_fondo_nivel_uno()
        self.sonido_nivel_uno = obtener_sonido_nivel_uno()
        #FONDO / SONIDO NIVEL 2
        self.fondo_nivel_dos = obtener_fondo_nivel_dos()
        self.sonido_nivel_dos = obtener_sonido_nivel_dos()
        #FONDO / SONIDO NIVEL 3
        self.fondo_nivel_tres = obtener_fondo_nivel_tres()
        self.sonido_nivel_tres = obtener_sonido_nivel_tres()
        #===ANIMACIONES ENEMIGOS TIPOS===
        self.animaciones_pescado_asesino_volando_izquierda = obtener_animaciones_pescado_volando_izquierda()
        self.animaciones_pescado_asesino_volando_derecha = obtener_animaciones_pescado_volando_derecha(
            self.animaciones_pescado_asesino_volando_izquierda)
        self.animacion_aero_cayendo = obtener_animaciones_aero_cayendo()
        self.animaciones_pajaro_izquierda = obtener_animaciones_pajaro_volando_izquierda()
        self.animaciones_pajaro_derecha = obtener_animaciones_pajaro_volando_derecha(self.animaciones_pajaro_izquierda)
        self.animacion_fake_mask_cayendo = obtener_animaciones_fake_mask_cayendo()
        self.animaciones_murcielago_izquierda = obtener_animaciones_murcielago_volando_izquierda()
        self.animaciones_murcielago_derecha = obtener_animaciones_murcielago_volando_derecha(self.animaciones_murcielago_izquierda)
        #===OTROS SONIDOS Y ANIMACIONES===
        self.sonido_danio = obtener_sonido_danio_personaje()
        self.sonido_manzana_wumpa = obtener_sonido_manzana_recolectada()
        self.sonido_enemigo_eliminado = obtener_sonido_enemigo_eliminado()
    #===PISOS / PLATAFORMAS===
        #PISOS
        self.piso_nivel_uno = Plataforma(0, 200, (ANCHO_PANTALLA, 30),
                                            "./assets/imagenes/Escenarios/nivel_uno/piso_nivel_uno.png")

        self.piso_nivel_dos = Plataforma(0, 0, (ANCHO_PANTALLA, 90),
                                            "./assets/imagenes/Escenarios/nivel_dos/piso_nivel_dos.png")

        self.piso_nivel_tres = Plataforma(0, 0, (ANCHO_PANTALLA, 80),
                                            "./assets/imagenes/Escenarios/nivel_tres/plataforma_nivel_tres.png")
        #PLATAFORMAS
        self.lista_plataformas_nivel_uno = obtener_plataformas_nivel_uno()
        self.lista_plataformas_nivel_dos = obtener_plataformas_nivel_dos()
        self.lista_plataformas_nivel_tres = obtener_plataformas_nivel_tres()
    #===GRUPOS SPRITES===
        self.plataformas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.bolas_fuego = pygame.sprite.Group()
        self.manzanas = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
    #===BANDERAS===
        self.se_esta_jugando = False
        self.se_esta_ejecutando = False
        self.juego_terminado = False
        self.pausado = False
        self.nivel_completado = False
        self.nivel = None
    #===PUNTAJE===
        self.puntuacion = 0
    #===VIDAS/ BARRA VIDA===
        self.imagen_vidas = obtener_animaciones_vidas()
        self.vidas = VIDAS
        self.barra_vida = BARRA_VIDA
        self.barra_vida_maxima = BARRA_VIDA
        self.vidas_iniciales = VIDAS
    #===TIEMPO===
        self.minutos = 1
        self.segundos = 0
        self.milisegundos = 0
    #===OPCIONES MENU JUEGO===
        self.opcion_jugar = self.fuente.render("Jugar", True, VERDE)
        self.opcion_jugar_rect = self.opcion_jugar.get_rect()
        self.opcion_jugar_rect.center = (CENTRO_X, CENTRO_Y + 100)

        self.opcion_nivel_uno = self.fuente.render("NIVEL 1", True, AZUL)
        self.opcion_nivel_uno_rect = self.opcion_nivel_uno.get_rect()
        self.opcion_nivel_uno_rect.center = (CENTRO_X, CENTRO_Y - 150)

        self.opcion_nivel_dos = self.fuente.render("NIVEL 2", True, AZUL)
        self.opcion_nivel_dos_rect = self.opcion_nivel_dos.get_rect()
        self.opcion_nivel_dos_rect.center = (CENTRO_X, CENTRO_Y)

        self.opcion_nivel_tres = self.fuente.render("NIVEL 3", True, AZUL)
        self.opcion_nivel_tres_rect = self.opcion_nivel_tres.get_rect()
        self.opcion_nivel_tres_rect.center = (CENTRO_X, CENTRO_Y + 150)

    #===MUESTRO MENU PRINCIPAL===
    def mostrar_pantalla_inicio(self)-> None:
        """_summary_
        Muestra el menu principal y el seleccionador de niveles
        """
        en_el_menu = True
        seleccionando_nivel = False

        while en_el_menu:
            self.RELOJ.tick(FPS)

            self.PANTALLA.blit(self.fondo, ORIGEN_COORDENADA)

            if not seleccionando_nivel:
                self.dibujar_texto("Dino Rage", ROJO, CENTRO)
                self.PANTALLA.blit(self.opcion_jugar, self.opcion_jugar_rect)

            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if not seleccionando_nivel:
                        if self.opcion_jugar_rect.collidepoint(evento.pos):
                            seleccionando_nivel = True
                    elif seleccionando_nivel:
                        if self.opcion_nivel_uno_rect.collidepoint(evento.pos):
                            self.fondo_sonido.stop()
                            self.nivel = 1
                            en_el_menu = False
                        elif self.opcion_nivel_dos_rect.collidepoint(evento.pos):
                            self.fondo_sonido.stop()
                            self.nivel = 2
                            en_el_menu = False
                        elif self.opcion_nivel_tres_rect.collidepoint(evento.pos):
                            self.fondo_sonido.stop()
                            self.nivel = 3
                            en_el_menu = False

            if seleccionando_nivel:
                self.PANTALLA.blit(self.opcion_nivel_uno, self.opcion_nivel_uno_rect)
                self.PANTALLA.blit(self.opcion_nivel_dos, self.opcion_nivel_dos_rect)
                self.PANTALLA.blit(self.opcion_nivel_tres, self.opcion_nivel_tres_rect)

            pygame.display.flip()

        self.reiniciar_juego()

    #===REINICIO / INICIO EL JUEGO===
    def reiniciar_juego(self)-> None:
        """_summary_
        Setea todos los metodos y atributos en su valor por default para que el juego comience de cero
        """
        self.sonido_nivel_uno.stop()
        self.sonido_nivel_dos.stop()
        self.sonido_nivel_tres.stop()
        self.puntuacion = 0
        self.minutos = 1
        self.segundos = 0
        self.milisegundos = 0
        self.sprites.empty()
        self.enemigos.empty()
        self.plataformas.empty()
        self.bolas_fuego.empty()
        self.manzanas.empty()
        self.imagen_vidas = obtener_animaciones_vidas()
        self.reiniciar_vidas()
        self.cargar_nivel()
        self.jugar()
    
    #===JUEGO AL JUEGO===
    def jugar(self)-> None:
        """_summary_
        Bucle principal del juego que se encarga de actualizar  y renderizar el juego, entre otras cosas
        """
        self.se_esta_ejecutando = True
        self.se_esta_jugando = True
        self.juego_terminado = False

        while self.se_esta_ejecutando:
            self.RELOJ.tick(FPS)
            self.manejar_eventos()
            if self.se_esta_jugando:
                if not self.pausado:
                    self.update()
                self.renderizar()

                if self.nivel_completado:
                    self.mostrar_pantalla_nivel_completado()
                    self.nivel_completado = False
                    self.mostrar_pantalla_inicio()

                if len(self.enemigos) == 0:
                    tiempo_restante = self.segundos
                    puntuacion_extra = tiempo_restante * 100
                    self.puntuacion += puntuacion_extra  
                    self.nivel_completado = True

        self.mostrar_pantalla_inicio()
    
    #===CONDICION NIVEL COMPLETADO===
    def ejecutar_condicion_completado(self)-> None:
        """_summary_
        Verifica que todos los enemigos hayan sido eliminados para poder ganar el nivel
        """
        len(self.enemigos) == 0
    
    #===DECREMENTO EL TIEMPO===
    def decrementar_contador(self):
        if self.milisegundos == 0:
            if self.segundos == 0:
                if self.minutos == 0:
                    self.se_esta_jugando = False
                    self.juego_terminado = True
                    self.fondo = obtener_fondo_menu_principal()
                else:
                    self.minutos -= 1
                    self.segundos = 60
            else:
                self.segundos -= 1
                self.milisegundos = 60
        else:
            self.milisegundos -= 1
    
    #===RENDERIZO LA PANTALLA===
    def renderizar(self)-> None:
        """_summary_
        Se encarga de mostrar o renderizar diferentes elementos en la pantalla del juego
        """
        if self.juego_terminado:
            self.mostrar_pantalla_juego_perdido()
        elif self.se_esta_jugando:
            self.PANTALLA.blit(self.fondo, ORIGEN_COORDENADA)
            self.sprites.draw(self.PANTALLA)
            if self.pausado:
                self.mostrar_pausa()
        else:
            self.mostrar_pantalla_inicio()

        self.dibujar_texto_con_dato("Puntaje", self.puntuacion, ROJO, (ANCHO_PANTALLA - 297, 35))

        texto_tiempo = self.fuente.render(f"{self.minutos:02d}:{self.segundos:02d}", True, ROJO)
        texto_tiempo_rect = texto_tiempo.get_rect()
        texto_tiempo_rect.topright = (ANCHO_PANTALLA - 550, 18)
        self.PANTALLA.blit(texto_tiempo, texto_tiempo_rect)

        self.dibujar_vidas()

        self.dibujar_barra_vida()
        #pygame.draw.rect(self.PANTALLA, "Red", self.rectangulo_arriba)

        pygame.display.flip()

    #===MANEJO EVENTOS E INPUT DEL PERSONAJE / JUEGO===
    def manejar_eventos(self)-> None:
        """_summary_
        Maneja los eventos de teclado
        """
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.personaje.velocidad_x = -5
                elif evento.key == pygame.K_RIGHT:
                    self.personaje.velocidad_x = 5
                elif evento.key == pygame.K_UP:
                    self.personaje.saltar()
                elif evento.key == pygame.K_SPACE:
                    self.personaje.disparar_bola_fuego(VELOCIDAD_BOLA_FUEGO, self.sprites, self.bolas_fuego)
                elif evento.key == pygame.K_p:
                    if not self.pausado:
                        if self.nivel == 1:
                            self.sonido_nivel_uno.stop()
                        elif self.nivel == 2:
                            self.sonido_nivel_dos.stop()
                        elif self.nivel == 3:
                            self.sonido_nivel_tres.stop()
                        self.pausado = True
                    else:
                        if self.nivel == 1:
                            self.sonido_nivel_uno.play()
                        elif self.nivel == 2:
                            self.sonido_nivel_dos.play()
                        elif self.nivel == 3:
                            self.sonido_nivel_tres.play()
                        self.pausado = False
                elif evento.key == pygame.K_r:
                    self.reiniciar_juego()
                elif evento.key == pygame.K_n:
                    self.mostrar_seleccion_nivel()
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and self.personaje.velocidad_x < 0:
                    self.personaje.velocidad_x = 0
                if evento.key == pygame.K_RIGHT and self.personaje.velocidad_x > 0:
                    self.personaje.velocidad_x = 0
    
    #===MUESTRO NIVELES===
    def mostrar_seleccion_nivel(self) -> None:
        """_summary_
        Muestra la pantalla de selección de nivel
        """
        seleccionando_nivel = True

        while seleccionando_nivel:
            self.RELOJ.tick(FPS)

            self.PANTALLA.blit(self.fondo, ORIGEN_COORDENADA)
            self.PANTALLA.blit(self.opcion_nivel_uno, self.opcion_nivel_uno_rect)
            self.PANTALLA.blit(self.opcion_nivel_dos, self.opcion_nivel_dos_rect)
            self.PANTALLA.blit(self.opcion_nivel_tres, self.opcion_nivel_tres_rect)

            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.opcion_nivel_uno_rect.collidepoint(evento.pos):
                        self.fondo_sonido.stop()
                        self.nivel = 1
                        seleccionando_nivel = False
                    elif self.opcion_nivel_dos_rect.collidepoint(evento.pos):
                        self.fondo_sonido.stop()
                        self.nivel = 2
                        seleccionando_nivel = False
                    elif self.opcion_nivel_tres_rect.collidepoint(evento.pos):
                        self.fondo_sonido.stop()
                        self.nivel = 3
                        seleccionando_nivel = False

            pygame.display.flip()

        self.reiniciar_juego()
    
    #===MUESTRO JUEGO PERDIDO===
    def mostrar_pantalla_juego_perdido(self)-> None:
        """_summary_
        Muestra una pantalla cuando se pierde la partida
        """
        self.sonido_nivel_uno.stop()
        self.sonido_nivel_dos.stop()
        self.sonido_nivel_tres.stop()
        self.fondo_sonido.play(loops = -1)
        self.fondo_sonido.set_volume(0.5)
        self.PANTALLA.blit(self.fondo_game_over, ORIGEN_COORDENADA)
        self.dibujar_texto("Game over", ROJO, CENTRO)
        pygame.display.flip()
        pygame.time.delay(3000)
        self.se_esta_ejecutando = False
    
    #===LEO PUNTAJE MAS ALTO===
    def cargar_puntaje_mas_alto(self):
        try:
            with open("archivo.txt", "r") as file:
                self.puntaje_mas_alto = int(file.read())
        except FileNotFoundError:
            self.puntaje_mas_alto = 0

    #===MUESTRO NIVEL COMPLETADO===
    def mostrar_pantalla_nivel_completado(self)-> None:
        """_summary_
        Muestra una pantalla cuando se completa un nivel
        """
        self.cargar_puntaje_mas_alto()
        self.sonido_nivel_uno.stop()
        self.sonido_nivel_dos.stop()
        self.sonido_nivel_tres.stop()
        self.fondo = obtener_fondo_menu_principal()
        self.fondo_sonido.stop()
        self.fondo_sonido.play(loops=-1)
        self.fondo_sonido.set_volume(0.5)
        self.PANTALLA.blit(self.fondo_game_over, ORIGEN_COORDENADA)
        self.dibujar_texto("Nivel Completado", VERDE, CENTRO)
        self.dibujar_texto_con_dato("Puntaje", self.puntuacion, ROJO, (CENTRO_X, CENTRO_Y + 100))
        
        if self.puntuacion > self.puntaje_mas_alto:
            self.puntaje_mas_alto = self.puntuacion
            self.dibujar_texto_con_dato("Nuevo puntaje mas alto", self.puntaje_mas_alto, ROJO, (CENTRO_X, CENTRO_Y + 300))
            with open("archivo.txt", "w") as file:
                file.write(str(self.puntuacion))
        else:
            self.dibujar_texto_con_dato("Puntaje mas alto", self.puntaje_mas_alto, ROJO, (CENTRO_X, CENTRO_Y + 300))
        
        pygame.display.flip()
        pygame.time.delay(3000)
        self.se_esta_ejecutando = False
    
    #===MUESTRO PAUSA===
    def mostrar_pausa(self)-> None:
        """_summary_
        Muestra un texto de "en pausa" cuando se presiona la tecla 'p' para pausar el juego
        """
        self.dibujar_texto("EN PAUSA", VERDE, CENTRO)
    
    #===DIBUJO LAS VIDAS===
    def dibujar_vidas(self)-> None:
        """_summary_
        Copia en la pantalla los iconos de las vidas del personaje en una posicion especifica de la pantalla
        """

        self.dibujar_texto("VIDAS:", ROJO, (ANCHO_PANTALLA - 1075, 35))

        for i in range(len(self.imagen_vidas)):
            imagen_vidas_rect = self.imagen_vidas[i].get_rect()
            if i == 0:
                imagen_vidas_rect.topleft = (ANCHO_PANTALLA - 1000, 20)
            elif i == 1:
                imagen_vidas_rect.topleft = (ANCHO_PANTALLA - 950, 20)
            elif i == 2:
                imagen_vidas_rect.topleft = (ANCHO_PANTALLA - 900, 20)

            self.PANTALLA.blit(self.imagen_vidas[i], imagen_vidas_rect)
    
    #===DIBUJO BARRA DE VIDA===
    def dibujar_barra_vida(self)-> None:
        """_summary_
        Dibuja dos rectangulos que representan la barra de vida del personaje
        """
        self.dibujar_texto("DINO", ROJO, (ANCHO_PANTALLA - 1110, 95))

        pygame.draw.rect(self.PANTALLA, ROJO, (40, 113, self.barra_vida, 25))
        pygame.draw.rect(self.PANTALLA, BLANCO, (40, 113, self.barra_vida_maxima, 25), 2)
    
    #===REINICIO VIDAS===
    def reiniciar_vidas(self)-> None:
        """_summary_
        Reinicia la barra de vida una vez que se agota por el danio causado por los enemigos
        """
        self.vidas = self.vidas_iniciales
        self.barra_vida = self.barra_vida_maxima
    
    #===CARGO NIVELES===
    def cargar_nivel(self)-> None:
        """_summary_
        Carga todo lo necesario para que se ejecute cada uno de los niveles
        """
        if self.nivel == 1:
            #FONDO NIVEL UNO
            self.fondo = self.fondo_nivel_uno
            #SONIDO NIVEL UNO
            self.sonido_nivel_uno.play(loops = -1)
            self.sonido_nivel_uno.set_volume(0.5)
            #PISO / PLATAFORMAS NIVEL UNO
            self.piso_nivel_uno = self.piso_nivel_uno
            self.lista_plataformas_nivel_uno = self.lista_plataformas_nivel_uno
            #PISO / PLATAFORMAS NIVEL UNO
            self.personaje = Personaje(self.piso_nivel_uno)
            self.piso_nivel_uno.rect.top = self.personaje.rect.bottom
            self.personaje.golpeado = False
            #AGREGO A SPRITES
            self.plataformas.add(self.lista_plataformas_nivel_uno)
            self.sprites.add(self.personaje)
            self.sprites.add(self.piso_nivel_uno)
            self.sprites.add(self.lista_plataformas_nivel_uno)
            #ENEMIGOS NIVEL UNO
            self.generar_dragones_nivel_uno()
            self.generar_pescados_asesinos_nivel_uno()
            #MANZANA
            self.generar_manzanas(self.lista_plataformas_nivel_uno)

        elif self.nivel == 2:
            #FONDO NIVEL DOS
            self.fondo = self.fondo_nivel_dos
            #SONIDO NIVEL DOS
            self.fondo_musica = self.sonido_nivel_dos
            self.sonido_nivel_dos.play(loops=-1)
            self.sonido_nivel_dos.set_volume(0.5)
            #PISO / PLATAFORMAS NIVEL UNO
            self.piso_nivel_dos = self.piso_nivel_dos
            self.lista_plataformas_nivel_dos = self.lista_plataformas_nivel_dos
            #PISO / PLATAFORMAS NIVEL UNO
            self.personaje = Personaje(self.piso_nivel_dos)
            self.piso_nivel_dos.rect.top = self.personaje.rect.bottom
            self.personaje.golpeado = False
            #AGREGO A SPRITES
            self.plataformas.add(self.lista_plataformas_nivel_dos)
            self.sprites.add(self.personaje)
            self.sprites.add(self.piso_nivel_dos)
            self.sprites.add(self.lista_plataformas_nivel_dos)
            #ENEMIGOS NIVEL DOS
            self.generar_luchadores_nivel_dos()
            self.generar_aeros_nivel_dos()
            self.generar_pajaros_nivel_dos()
            #MANZANAS
            self.generar_manzanas(self.lista_plataformas_nivel_dos)

        elif self.nivel == 3:
            #FONDO NIVEL TRES
            self.fondo = self.fondo_nivel_tres
            #SONIDO NIVEL TRESS
            self.fondo_musica = self.sonido_nivel_dos
            self.sonido_nivel_tres.play(loops=-1)
            self.sonido_nivel_tres.set_volume(0.5)
            #self.generar_enemigos()
            #PISO / PLATAFORMAS NIVEL UNO
            self.piso_nivel_tres = self.piso_nivel_tres
            self.lista_plataformas_nivel_tres = self.lista_plataformas_nivel_tres
            #PISO / PLATAFORMAS NIVEL UNO
            self.personaje = Personaje(self.piso_nivel_tres)
            self.piso_nivel_tres.rect.top = self.personaje.rect.bottom
            self.personaje.golpeado = False
            #ADDS A SPRITES
            self.plataformas.add(self.lista_plataformas_nivel_tres)
            self.sprites.add(self.personaje)
            self.sprites.add(self.piso_nivel_tres)
            self.sprites.add(self.lista_plataformas_nivel_tres)
            #ENEMIGOS NIVEL UNO
            self.generar_minotauros_nivel_tres()
            self.generar_fake_mask_nivel_tres()
            self.generar_murcielagos_nivel_tres()
            #MANZANAS
            self.generar_manzanas(self.lista_plataformas_nivel_tres)
    
    def colisionar_personaje_con_plataformas(self, lista_plataformas: list):
        for plataforma in lista_plataformas:
            if self.personaje.rect.colliderect(plataforma.rect):
                self.rectangulo_arriba = pygame.Rect(plataforma.rect.left, plataforma.rect.top - 10, plataforma.rect.width, 20)
                self.rectangulo_abajo = pygame.Rect(plataforma.rect.left, plataforma.rect.top + 55, plataforma.rect.width, 20)
                if self.personaje.rect.colliderect(self.rectangulo_arriba):
                    print("F")
                    self.personaje.rect.bottom = plataforma.rect.top
                    self.personaje.saltando = False
                    self.personaje.velocidad_y = 0
                    self.personaje.salto = 0
                    break
                elif self.personaje.rect.colliderect(self.rectangulo_abajo):
                    print("B")
                    self.personaje.rect.top = plataforma.rect.bottom
                    self.personaje.saltando = False
                    self.personaje.velocidad_y = 1
                    self.personaje.salto = 0
                    break

        if not self.personaje.saltando:
            en_plataforma = False
            for plataforma in lista_plataformas:
                self.rectangulo_arriba = pygame.Rect(plataforma.rect.left, plataforma.rect.top - 10, plataforma.rect.width, 20)
                if self.personaje.rect.colliderect(self.rectangulo_arriba):
                    print("S")
                    self.personaje.rect.bottom = plataforma.rect.top
                    self.personaje.saltando = False
                    self.personaje.velocidad_y = 0
                    self.personaje.salto = 0
                    en_plataforma = True
                    break

            if not en_plataforma:
                print("N")
                self.personaje.velocidad_y += self.personaje.gravedad
                self.personaje.rect.y += self.personaje.velocidad_y
    
    def colisiones_plataformas_nivel(self)-> None:
        if self.nivel == 1:
            self.colisionar_personaje_con_plataformas(self.lista_plataformas_nivel_uno)
        elif self.nivel == 2:
            self.colisionar_personaje_con_plataformas(self.lista_plataformas_nivel_dos)
        elif self.nivel == 3:
            self.colisionar_personaje_con_plataformas(self.lista_plataformas_nivel_tres)
    
    #===COLISIONES===
    def detectar_colisiones(self)-> None:
        """_summary_
        Detecta algunas colisiones
        """
        for bola_fuego in self.bolas_fuego:
            lista = pygame.sprite.spritecollide(bola_fuego, self.enemigos, True)
            if len(lista) != 0:
                bola_fuego.kill()
                self.sonido_enemigo_eliminado.play()
                if self.nivel == 1:
                    self.puntuacion += 120
                elif self.nivel == 2:
                    self.puntuacion += 250
                elif self.nivel == 3:
                    self.puntuacion += 400

        lista = pygame.sprite.spritecollide(self.personaje, self.enemigos, False)
        if len(lista) != 0:
            self.personaje.golpeado = True
            self.sonido_danio.play()
            self.barra_vida -= 2
            if self.barra_vida == 0:
                self.vidas -= 1
                if len(self.imagen_vidas) > 0:
                    self.imagen_vidas.pop(0)
                if self.vidas == 0:
                    self.se_esta_jugando = False
                    self.juego_terminado = True
                    self.fondo = obtener_fondo_menu_principal()
                else:
                    self.barra_vida = self.barra_vida_maxima
        
        lista_colisiones_manzanas = pygame.sprite.spritecollide(self.personaje, self.manzanas, True)
        if len(lista_colisiones_manzanas) != 0:
            self.sonido_manzana_wumpa.play()
            if self.nivel == 1:
                self.puntuacion += 120
            elif self.nivel == 2:
                self.puntuacion += 250
            elif self.nivel == 3:
                self.puntuacion += 400

        self.colisiones_plataformas_nivel()
    
    #===ELEMENTOS KILL===
    def eliminar_elementos_fuera_pantalla(self)-> None:
        """_summary_
        Elimina al sprite del grupo al que pertenezca una vez que haga contacto con las coordenadas elegidas de la pantalla
        """

        for bola_fuego in self.bolas_fuego:
            if bola_fuego.rect.right >= ANCHO_PANTALLA or bola_fuego.rect.left <= IZQUIERDA_PANTALLA:
                bola_fuego.kill()
    
    #===GENERO MANZANAS===
    def generar_manzanas(self, plataformas: list):
        for plataforma in plataformas:
            manzana_wumpa = Manzana()
            manzana_wumpa.rect.midtop = plataforma.rect.midtop
            manzana_wumpa.rect.top = manzana_wumpa.rect.top - 30
            self.manzanas.add(manzana_wumpa)
            self.sprites.add(manzana_wumpa)
    
    #===ENEMIGOS NIVEL UNO===
    def generar_dragones_nivel_uno(self):
        dragones_pos_x = [350, 800, 900, 1200, 1350, 1500, 1700, 1900, 2200] 
        for i in range(len(dragones_pos_x)):
            dragon = Dragon()
            dragon.rect.x = dragones_pos_x[i]
            self.enemigos.add( dragon)
            self.sprites.add( dragon)
    
    def generar_pescados_asesinos_nivel_uno(self):
        pescados_asesinos_pos_x = [600, 900, 1200, 1300, 1450, 1600, 1700, 2100, 2500] 
        for i in range(len(pescados_asesinos_pos_x)):
            self.animaciones_pescado_asesino_volando_izquierda = self.animaciones_pescado_asesino_volando_izquierda
            self.animaciones_pescado_asesino_volando_derecha = self.animaciones_pescado_asesino_volando_derecha
            pescado_asesino = Enemigo_aereo(self.animaciones_pescado_asesino_volando_izquierda, self.animaciones_pescado_asesino_volando_derecha)
            pescado_asesino.rect.x = pescados_asesinos_pos_x[i]
            self.enemigos.add(pescado_asesino)
            self.sprites.add(pescado_asesino)
    
    #===ENEMIGOS NIVEL DOS===
    def generar_luchadores_nivel_dos(self):
        luchadores_pos_x = [320, 500, 1000, 1250, 1450, 1600, 1700, 2100, 2300] 
        for i in range(len(luchadores_pos_x)):
            luchador = Luchador()
            luchador.rect.x =  luchadores_pos_x[i]
            self.enemigos.add(luchador)
            self.sprites.add(luchador)
    
    def generar_aeros_nivel_dos(self):
        for _ in range(10):
            self.animacion_aero_cayendo = self.animacion_aero_cayendo
            aero = Enemigo_paracaidista(self.animacion_aero_cayendo)
            aero.rect.y =  randrange(ARRIBA_PANTALLA, ABAJO_PANTALLA)
            aero.rect.x = randrange(10, 1000)
            self.enemigos.add(aero)
            self.sprites.add(aero)

    def generar_pajaros_nivel_dos(self):
        pajaros_pos_x = [550, 750, 900, 1000, 1200, 1350, 1500, 1700, 2100] 
        for i in range(len(pajaros_pos_x)):
            self.animaciones_pajaro_izquierda = self.animaciones_pajaro_izquierda
            self.animaciones_pajaro_derecha = self.animaciones_pajaro_derecha
            pajaro = Enemigo_aereo(self.animaciones_pajaro_izquierda, self.animaciones_pajaro_derecha)
            pajaro.rect.x =  pajaros_pos_x[i]
            self.enemigos.add(pajaro)
            self.sprites.add(pajaro)
    
    #===ENEMIGOS NIVEL TRES===
    def generar_minotauros_nivel_tres(self):
        minotauros_pos_x = [300, 550, 900, 1000, 1200, 1350, 1500, 1700, 2100, 2250, 2500]
        for i in range(len(minotauros_pos_x)):
            minotauro = Minotauro()
            minotauro.rect.x =  minotauros_pos_x[i]
            self.enemigos.add(minotauro )
            self.sprites.add(minotauro )
    
    def generar_fake_mask_nivel_tres(self):
        for _ in range(13):
            self.animacion_fake_mask_cayendo = self.animacion_fake_mask_cayendo
            fake_mask = Enemigo_paracaidista(self.animacion_fake_mask_cayendo)
            fake_mask.rect.y =  randrange(ARRIBA_PANTALLA, ABAJO_PANTALLA)
            fake_mask.rect.x = randrange(10, 1000)
            self.enemigos.add(fake_mask)
            self.sprites.add(fake_mask)
    
    def generar_murcielagos_nivel_tres(self):
        murcielagos_pos_x = [550, 900, 1000, 1200, 1350, 1500, 1700, 2100, 2300, 2700] 
        for i in range(len(murcielagos_pos_x)):
            self.animaciones_murcielago_izquierda = self.animaciones_murcielago_izquierda
            self.animaciones_murcielago_derecha = self.animaciones_murcielago_derecha
            murcielago = Enemigo_aereo(self.animaciones_murcielago_izquierda, self.animaciones_murcielago_derecha)
            murcielago.rect.x =  murcielagos_pos_x[i]
            self.enemigos.add(murcielago)
            self.sprites.add(murcielago)
    
    #===DIBUJO TEXTO===
    def dibujar_texto(self, string:str, color: tuple, tam: tuple):
        texto = self.fuente.render(f"{string}", True, color)
        texto_rect = texto.get_rect()
        texto_rect.center = tam
        self.PANTALLA.blit(texto, texto_rect)
    
    #===DIBUJO TEXTO CON DATO===
    def dibujar_texto_con_dato(self, string:str, dato: int, color: tuple, tam: tuple):
        texto = self.fuente.render(f"{string}: {dato}", True, color)
        texto_rect = texto.get_rect()
        texto_rect.center = tam
        self.PANTALLA.blit(texto, texto_rect)

    #===ACTUALIZO===
    def update(self)-> None:
        """_summary_
        Actualiza los sprites y metodos de la clase
        """
        self.eliminar_elementos_fuera_pantalla()
        #NECESITO ACTULIZAR
        self.detectar_colisiones()
        #ACTUALIZA LOS SPRITES
        self.sprites.update()
        self.decrementar_contador()


