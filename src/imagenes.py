import pygame
from configuracion import*

def obtener_icono_juego():
    icono = pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert(), TAM_PANTALLA)
    return icono

def obtener_fuente():
    fuente = pygame.font.Font("./assets/fuente/fuentee.otf", 40)
    return fuente

def obtener_fondo_menu_principal():
    fondo = pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/fondo_principal.jpg").convert(), TAM_PANTALLA)
    return fondo

def obtener_fondo_game_over():
    fondo_game_over = pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/game_over.png").convert(), 
                                                TAM_PANTALLA)
    return  fondo_game_over

def obtener_fondo_nivel_uno():
    fondo_nivel_uno = pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/nivel_uno/fondo_nivel_uno.jpg").convert(),
                                                TAM_PANTALLA)
    return fondo_nivel_uno

def obtener_fondo_nivel_dos():
    fondo_nivel_dos =  pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/nivel_dos/fondo_nivel_dos.jpg").convert(), 
                                                TAM_PANTALLA)
    return fondo_nivel_dos

def obtener_fondo_nivel_tres():
    fondo_nivel_tres = pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/nivel_tres/fondo_nivel_tres.jpg").convert(), 
                                                TAM_PANTALLA)
    return fondo_nivel_tres