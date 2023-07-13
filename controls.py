import pygame

def move_player(keys, player):
    """
    Esta función toma dos parámetros: keys y player. keys es un diccionario que representa el 
    estado actual del teclado, donde cada clave del diccionario es un código de tecla y su valor 
    es True si la tecla correspondiente está presionada, o False si no lo está.
    Este bloque de código controla el movimiento del jugador en las ocho direcciones posibles: 
    izquierda, derecha, arriba, abajo y las diagonales.
    """

    if keys[pygame.K_LEFT]: 
        if keys[pygame.K_UP]:
            player.move_up_left() 
        elif keys[pygame.K_DOWN]: 
            player.move_down_left() 
        else: 
            player.move_left() 
    elif keys[pygame.K_RIGHT]: 
        if keys[pygame.K_UP]: 
            player.move_up_right() 
        elif keys[pygame.K_DOWN]: 
            player.move_down_right() 
        else: 
            player.move_right() 
    elif keys[pygame.K_UP]: 
        player.move_up() 
    elif keys[pygame.K_DOWN]: 
        player.move_down() 
    else: 
        player.stop() 
