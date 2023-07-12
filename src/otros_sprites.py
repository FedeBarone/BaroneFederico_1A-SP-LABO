import pygame
from configuracion import*

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


#===ANIMACION MANZANA WUMPA===
def obtener_animaciones_manzana_wumpa()-> list:
    animaciones_manzana_wumpa = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_uno.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_dos.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_tres.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_cuatro.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_cinco.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Escenarios/frutas_puntaje/fruta_wumpa_seis.png").convert_alpha(), 
                (TAM_MURCIELAGO)),
                
        ]
    return animaciones_manzana_wumpa


#===ANIMACION DRAGON CAMINANDO IZQUIERDA===
def obtener_animaciones_dragon_caminando_izquierda()-> list:
    animaciones_dragon_caminando_izquierda = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_uno.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_dos.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_tres.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_cuatro.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_cinco.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_seis.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_siete.png").convert_alpha(), 
                (TAM_DRAGON)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_uno/dragon/dragon_ocho.png").convert_alpha(), 
                (TAM_DRAGON)),
    ]

    return animaciones_dragon_caminando_izquierda

#===ANIMACION DRAGON CAMINANDO DERECHA===
def obtener_animaciones_dragon_caminando_derecha(animaciones_dragon_caminando_izquierda)-> list:
    animaciones_dragon_caminando_derecha = girar_imagen(animaciones_dragon_caminando_izquierda, True, False)

    return animaciones_dragon_caminando_derecha


#====animaciones_luchador_caminanado_derecha===
def obtener_animaciones_luchador_caminando_derecha()-> list:
    animaciones_luchador_caminando_derecha = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_uno.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_dos.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_tres.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_cuatro.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_cinco.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_seis.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_siete.png").convert_alpha(), 
                (TAM_LUCHADOR)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_dos/luchador/luchador_ocho.png").convert_alpha(), 
                (TAM_LUCHADOR)),
    ]

    return animaciones_luchador_caminando_derecha

#====animaciones_luchador_caminando_izquierda===
def obtener_animaciones_luchador_caminando_izquierda(animaciones_luchador_caminando_derecha)-> list:
    animaciones_luchador_caminando_izquierda = girar_imagen(animaciones_luchador_caminando_derecha, True, False)

    return animaciones_luchador_caminando_izquierda



#====animaciones_minotauro_caminanado_derecha===
def obtener_animaciones_minotauro_caminando_derecha()-> list:
    animaciones_minotauro_caminando_derecha = [
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_uno.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_dos.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_tres.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_cuatro.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_cinco.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_seis.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_siete.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_ocho.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_nueve.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_diez.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_once.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_doce.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_trece.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_catorce.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_quince.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_dieciseis.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_diecisiete.png").convert_alpha(), 
                (TAM_MINOTAURO)),
                pygame.transform.scale(pygame.image.load("./assets/imagenes/Enemigos/enemigos_nivel_tres/minotauro/minotauro_dieciocho.png").convert_alpha(), 
                (TAM_MINOTAURO)),
    ]

    return animaciones_minotauro_caminando_derecha

#====animaciones_minotauro_caminando_izquierda===
def obtener_animaciones_minotauro_caminando_izquierda(animaciones_minotauro_caminando_derecha)-> list:
    animaciones_minotauro_caminando_izquierda = girar_imagen(animaciones_minotauro_caminando_derecha, True, False)

    return animaciones_minotauro_caminando_izquierda
