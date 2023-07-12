import pygame
from configuracion import*
from class_Juego import*

def girar_imagen(lista_original:list, flip_x:bool, flip_y:bool)->list:
    """_summary_
        gira una lista de superficies
    Args:
        lista_original (list): lista a girar
        flip_x (bool): girar en horizontal
        flip_y (bool): girar en vertical

    Returns:
        list: lista girada
    """
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

#===ANIMACIONES PERSONAJE CAMINANDO DERECHA===
def obtener_animaciones_personaje_caminando_derecha()-> list:
    animaciones = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/camina_derecha_1.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/camina_derecha_2.png").convert_alpha(), 
                (TAM_PERSONAJE)),
    ]

    return animaciones

#===ANIMACIONES PERSONAJE CAMINANDO IZQUIERDA===
def obtener_animaciones_personaje_caminando_izquierda(personaje_caminando_derecha)-> list:
    personaje_caminando_izquierda = girar_imagen(personaje_caminando_derecha, True, False)

    return personaje_caminando_izquierda

#===ANIMACIONES PERSONAJE INACTIVO DERECHA===
def obtener_animaciones_personaje_inactivo_derecha()-> list:
    animaciones = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/inactivo_derecha_1.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/inactivo_derecha_2.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/inactivo_derecha_3.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/inactivo_derecha_3.png").convert_alpha(), 
                (TAM_PERSONAJE))
    ]

    return animaciones

#===ANIMACIONES PERSONAJE INACTIVO IZQUIERDA===
def obtener_animaciones_personaje_inactivo_izquierda(personaje_inactivo_derecha:list)-> list:
    personaje_inactivo_izquierda = girar_imagen(personaje_inactivo_derecha, True, False)

    return personaje_inactivo_izquierda

#===ANIMACIONES PERSONAJE DANIO DERECHA===
def obtener_animaciones_danio_derecha()-> list:
    animaciones_danio_derecha = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/danio.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                # pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/danio.png").convert_alpha(), 
                # (TAM_PERSONAJE)),
                # pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/danio.png").convert_alpha(), 
                # (TAM_PERSONAJE)),
                # pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/danio.png").convert_alpha(), 
                # (TAM_PERSONAJE)),
                # pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/danio.png").convert_alpha(), 
                # (TAM_PERSONAJE)),
    ]

    return animaciones_danio_derecha

#===ANIMACIONES PERSONAJE DANIO IZQUIERDA===
def obtener_animaciones_danio_izquierda(animaciones_danio_derecha:list)-> list:
    animaciones_danio_izquierda = girar_imagen(animaciones_danio_derecha, True, False)

    return animaciones_danio_izquierda

#===ANIMACION PERSONAJE SALTA DERECHA===
def obtener_animacion_personaje_salta_derecha()-> list:
    animaciones = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/salto_derecha.png").convert_alpha(),
                (TAM_PERSONAJE))
    ]

    return animaciones

#===ANIMACION PERSONAJE SALTA IZQUIERDA===
def obtener_animacion_personaje_salta_izquierda(personaje_saltando_derecha:list)-> list:
    personaje_saltando_izquierda = girar_imagen(personaje_saltando_derecha, True, False)

    return personaje_saltando_izquierda

#===ANIMACION VIDAS PERSONAJE===
def obtener_animaciones_vidas()-> list:
    imagen_vidas = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/vidas.png").convert_alpha(), (32, 32)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/vidas.png").convert_alpha(), (32, 32)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/vidas.png").convert_alpha(), (32, 32))
            ]
    return imagen_vidas

#===DISPARO BOLA FUEGO PERSONAJE===
def obtener_animaciones_disparo_bola_fuego()-> list:
    imagenes_disparo = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Personaje/disparo_derecha.png").convert_alpha(), 
                (TAM_PERSONAJE)),
                
        ]
    return imagenes_disparo

#===DISPARO BOLA FUEGO PERSONAJE IZQUIERDA===
def obtener_animaciones_disparo_bola_fuego_izquierda(imagenes_disparo:list)-> list:
    disparo_bola_fuego_izquierda = girar_imagen(imagenes_disparo, True, False)

    return disparo_bola_fuego_izquierda

#===ANIMACIONES ENEMIGOS NIVEL 1===
#====animaciones_pescado_volando_izquierda===
def obtener_animaciones_pescado_volando_izquierda()-> list:
    animaciones_pescado_volando_izquierda = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_uno.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_dos.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_tres.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_cuatro.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_cinco.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_seis.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_siete.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_ocho.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_nueve.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_diez.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_once.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_doce.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_trece.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/pescado_asesino/pescado_asesino_catorce.png").convert_alpha(), 
                (TAM_PESCADO_ASESINO)),
    ]

    return  animaciones_pescado_volando_izquierda

#====obtener_animaciones_pescado_volando_derecha===
def obtener_animaciones_pescado_volando_derecha(animaciones_pescado_volando_izquierda)-> list:
    animaciones_pescado_volando_derecha = girar_imagen(animaciones_pescado_volando_izquierda, True, False)

    return animaciones_pescado_volando_derecha


#===ANIMACIONES ENEMIGOS NIVEL 2===
#====animaciones_aero_cayendo===
def obtener_animaciones_aero_cayendo()-> list:
    animaciones_aero_cayendo = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/aero/aero_uno.png").convert_alpha(), 
                (TAM_AERO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/aero/aero_dos.png").convert_alpha(), 
                (TAM_AERO)),
    ]

    return animaciones_aero_cayendo


#====animaciones_pajaro_volando_izquierda===
def obtener_animaciones_pajaro_volando_izquierda()-> list:
    animaciones_pajaro_volando_izquierda = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/pajaro/pajaro_uno.png").convert_alpha(), 
                (TAM_PAJARO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/pajaro/pajaro_dos.png").convert_alpha(), 
                (TAM_PAJARO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/pajaro/pajaro_tres.png").convert_alpha(), 
                (TAM_PAJARO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/pajaro/pajaro_cuatro.png").convert_alpha(), 
                (TAM_PAJARO)),
    ]

    return  animaciones_pajaro_volando_izquierda

#====obtener_animaciones_pajaro_volando_derecha===
def obtener_animaciones_pajaro_volando_derecha(animaciones_pajaro_volando_izquierda)-> list:
    animaciones_pajaro_volando_derecha = girar_imagen(animaciones_pajaro_volando_izquierda, True, False)

    return animaciones_pajaro_volando_derecha

#===ANIMACIONES ENEMIGOS NIVEL 3===
#====animaciones_murcielago_volando_izquierda===
def obtener_animaciones_murcielago_volando_izquierda()-> list:
    animaciones_murcielago_volando_izquierda = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_uno.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_dos.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_tres.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_cuatro.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_cinco.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/murcielago/murcielago_seis.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
    ]

    return  animaciones_murcielago_volando_izquierda

#====obtener_animaciones_murcielago_volando_derecha===
def obtener_animaciones_murcielago_volando_derecha(obtener_animaciones_murcielago_volando_izquierda)-> list:
    animaciones_murcielago_volando_derecha = girar_imagen(obtener_animaciones_murcielago_volando_izquierda, True, False)

    return animaciones_murcielago_volando_derecha

#====animaciones_fake_mask_cayendo===
def obtener_animaciones_fake_mask_cayendo()-> list:
    animaciones_fake_mask_cayendo = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_uno.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_dos.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_tres.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_cuatro.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_cinco.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_seis.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_seis.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/fake_mask/fake_mask_seis.png").convert_alpha(), 
                (TAM_FAKE_MASK)),
    ]

    return animaciones_fake_mask_cayendo