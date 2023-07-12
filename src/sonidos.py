import pygame

#===SONIDO MENU PRINCIPAL===
def obtener_sonido_menu_principal():
    sonido_menu_principal = pygame.mixer.Sound("./assets/sonidos/sonido_menu.mp3")
    return sonido_menu_principal

#===SONIDO NIVEL UNO===
def obtener_sonido_nivel_uno():
    sonido_nivel_uno = pygame.mixer.Sound("./assets/sonidos/sonido_nivel_uno.mp3")
    return sonido_nivel_uno

#===SONIDO NIVEL DOS===
def obtener_sonido_nivel_dos():
    sonido_nivel_dos = pygame.mixer.Sound("./assets/sonidos/sonido_nivel_dos.mp3")
    return sonido_nivel_dos

#===SONIDO NIVEL TRES===
def obtener_sonido_nivel_tres():
    sonido_nivel_tres = pygame.mixer.Sound("./assets/sonidos/sonido_nivel_tres.mp3")
    return sonido_nivel_tres

#===SONIDO BOLA FUEGO===
def obtener_sonido_bola_fuego():
    sonido_bola_fuego = pygame.mixer.Sound("./assets/sonidos/sonido_bola_fuego.wav")
    return sonido_bola_fuego

#===SONIDO SALTO PERSONAJE===
def obtener_sonido_salto_personaje():
    sonido_salto_personaje = pygame.mixer.Sound("./assets/sonidos/sonido_salto_dino.wav")
    return  sonido_salto_personaje

#===SONIDO DANIO PERSONAJE
def obtener_sonido_danio_personaje():
    sonido_salto_personaje = pygame.mixer.Sound("./assets/sonidos/sonido_danio_dino.wav")
    return  sonido_salto_personaje

#===SONIDO MANZANA WUMPA RECOLECTADA===
def obtener_sonido_manzana_recolectada():
    sonido_salto_personaje = pygame.mixer.Sound("./assets/sonidos/manzana_ganada.wav")
    return  sonido_salto_personaje

#===SONIDO ENEMIGO ELIMINADO===
def obtener_sonido_enemigo_eliminado():
    sonido_salto_personaje = pygame.mixer.Sound("./assets/sonidos/sonido_eliminar_enemigo.wav")
    return  sonido_salto_personaje




