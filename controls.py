import pygame
from classes.constants import WIDTH, HEIGHT


def move_player(keys, player):
    """
    Esta función toma dos parámetros: keys y player. keys es un diccionario que representa el 
    estado actual del teclado, donde cada clave del diccionario es un código de tecla y su valor 
    es True si la tecla correspondiente está presionada, o False si no lo está.
    Este bloque de código controla el movimiento del jugador en las ocho direcciones posibles: 
    izquierda, derecha, arriba, abajo y las diagonales.
    """
   

    if keys[pygame.K_LEFT]: #Verifica si la tecla de flecha izquierda está siendo presionada.
        if keys[pygame.K_UP]: #Verifica si la tecla de flecha arriba está siendo presionada.
            player.move_up_left() #Si se presionan las teclas de flecha izquierda y arriba al mismo tiempo, se llama al método move_up_left() del objeto player para moverlo en diagonal hacia arriba y hacia la izquierda.
        elif keys[pygame.K_DOWN]: #Verifica si la tecla de flecha abajo está siendo presionada.
            player.move_down_left() #Si se presionan las teclas de flecha izquierda y abajo al mismo tiempo, se llama al método move_down_left() del objeto player para moverlo en diagonal hacia abajo y hacia la izquierda.
        else: #Si solo se presiona la tecla de flecha izquierda sin las teclas de flecha arriba o abajo
            player.move_left() #se llama al método move_left() del objeto player para moverlo hacia la izquierda.
    elif keys[pygame.K_RIGHT]: #Verifica si la tecla de flecha derecha está siendo presionada.
        if keys[pygame.K_UP]: #Verifica si la tecla de flecha arriba está siendo presionada.
            player.move_up_right() #Si se presionan las teclas de flecha derecha y arriba al mismo tiempo, se llama al método move_up_right() del objeto player para moverlo en diagonal hacia arriba y hacia la derecha.
        elif keys[pygame.K_DOWN]: #Verifica si la tecla de flecha abajo está siendo presionada.
            player.move_down_right() #Si se presionan las teclas de flecha derecha y abajo al mismo tiempo, se llama al método move_down_right() del objeto player para moverlo en diagonal hacia abajo y hacia la derecha.
        else: #Si solo se presiona la tecla de flecha derecha sin las teclas de flecha arriba o abajo
            player.move_right() #se llama al método move_right() del objeto player para moverlo hacia la derecha.
    elif keys[pygame.K_UP]: #Si solo se presiona la tecla de flecha arriba sin las teclas de flecha izquierda o derecha
        player.move_up() #Se llama al método move_up() del objeto player para moverlo hacia arriba.
    elif keys[pygame.K_DOWN]: #Si solo se presiona la tecla de flecha abajo sin las teclas de flecha izquierda o derecha
        player.move_down() #Se llama al método move_down() del objeto player para moverlo hacia abajo.
    else: #Si no se presiona ninguna de las teclas de flecha
        player.stop() #se llama al método stop() del objeto player para detener su movimiento.
