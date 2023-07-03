import pygame
from classes.constants import WIDTH, HEIGHT

"""move_player toma dos parámetros: keys y player. keys es un diccionario que representa el 
estado actual del teclado, donde cada clave del diccionario es un código de tecla y su valor 
es True si la tecla correspondiente está presionada, o False si no lo está.
 """
def move_player(keys, player):
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
"""
Estas funciones permiten controlar el movimiento del jugador en el juego utilizando el teclado.
La función move_player toma el estado del teclado como entrada y actualiza la posición del 
jugador en función de las teclas presionadas.
"""