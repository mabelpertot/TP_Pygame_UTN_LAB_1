import pygame
from classes.constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def music_background(): 
    """"
    Carga y reproduce la música de fondo del juego en un bucle infinito con un volumen establecido.
    """
    pygame.mixer.music.load('game_sounds/background_music.mp3') #Carga un archivo de música de fondo llamado 
    pygame.mixer.music.set_volume(0.25) #Establece el volumen de la música de fondo al 25% de su volumen máximo
    pygame.mixer.music.play(loops=-1) #Reproduce la música de fondo en un bucle infinito

def show_game_over(score):
    """
    Muestra la pantalla de "Game Over" en la ventana de pygame. Toma el puntaje como argumento. 
    Muestra el texto "GAME OVER" en el centro de la pantalla y el texto "Final Score: {score}" debajo de él, 
    donde {score} es el puntaje pasado. Luego, reproduce una música de "game over" y hace una pausa de 4 segundos.
    """

    font = pygame.font.SysFont('Impact', 50) # Crea una fuente de texto con la fuente 'Impact' y un tamaño de 50.
    font_small = pygame.font.SysFont('Impact', 30) # Crea una fuente de texto más pequeña con la fuente 'Impact' y un tamaño de 30.
    text = font.render("GAME OVER", True, (139, 0, 0)) # Renderiza el texto "GAME OVER" con la fuente y el color especificados.
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 150)) # Obtiene el rectángulo del texto y lo posiciona en el centro de la pantalla (en el eje X) y arriba del centro (en el eje Y).
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255)) # Renderiza el texto "Final Score: {score}" con la fuente y el color especificados, donde {score} es el puntaje pasado como argumento.
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 100)) # Obtiene el rectángulo del texto del puntaje y lo posiciona en el centro de la pantalla (en el eje X) y debajo del centro (en el eje Y).
    screen.blit(text, text_rect)  # Dibuja el texto "GAME OVER" en la pantalla en la posición especificada por el rectángulo del texto.
    screen.blit(score_text, score_rect) # Dibuja el texto del puntaje en la pantalla en la posición especificada por el rectángulo del texto del puntaje.
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/gameover.mp3') # Actualiza la pantalla.
    pygame.mixer.music.play() # Reproduce la música de game over.
    pygame.time.delay(4000) # Hace una pausa de 4000 milisegundos (4 segundos).
    music_background() # Llama a la función "music_background()" 

def show_game_win():
    """
    Muestra un mensaje de victoria en la ventana de Pygame. Renderiza el texto "YOU'VE WON!" 
    utilizando la fuente 'Impact' y lo muestra centrado en la pantalla. Luego, carga y reproduce un archivo 
    de música de victoria. Después de una pausa de 1 segundo, llama a la función music_background(). 
    El bloque de código muestra un mensaje de victoria y reproduce música relacionada con la victoria en el juego.
    """

    font = pygame.font.SysFont('Impact', 50) # Crea una fuente de texto con la fuente 'Impact' y un tamaño de 50.
    text = font.render("YOU'VE WON!", True, (255, 255, 255)) # Renderiza el texto "YOU'VE WON!" con la fuente y el color especificados.
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 150)) # Obtiene el rectángulo del texto y lo posiciona en el centro de la pantalla.
    screen.blit(text, text_rect) # Dibuja el texto en la pantalla en la posición especificada por el rectángulo del texto.
    pygame.display.flip() # Actualiza la pantalla.
    pygame.mixer.music.load('game_sounds/win.mp3') # Carga un archivo de música de victoria.
    pygame.mixer.music.play() # Reproduce la música de victoria.
    pygame.time.delay(1000)  # Hace una pausa de 1000 milisegundos (1 segundo).
    music_background() # Llama a la función "music_background()"

"""" 
Estas funciones se encargan de mostrar mensajes de "Game Over" y "Game Win" en la pantalla del juego, 
reproducir sonidos relacionados y gestionar la música de fondo. 
Se encargan principalmente de realizar acciones visuales y auditivas en el juego.
"""
