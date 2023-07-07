import pygame
from classes.constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def music_background(): 
    """"
    Carga y reproduce la música de fondo del juego en un bucle infinito con un volumen establecido.
    """
    pygame.mixer.music.load('game_sounds/background_music.mp3') 
    pygame.mixer.music.set_volume(0.25) 
    pygame.mixer.music.play(loops=-1) 

def show_game_over(score): #Recibe como parametro: score (el puntaje). 
    """
    Muestra la pantalla de "Game Over" en la ventana de pygame.
    Muestra el texto "GAME OVER" en el centro de la pantalla y el texto "Final Score: {score}" debajo de él, 
    donde {score} es el puntaje pasado. Luego, reproduce una música de "game over" y hace una pausa de 4 segundos.
    """

    font = pygame.font.SysFont('Impact', 50) 
    font_small = pygame.font.SysFont('Impact', 30) 
    text = font.render("GAME OVER", True, (139, 0, 0)) 
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 150)) 
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255)) 
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 100)) 
    screen.blit(text, text_rect)  
    screen.blit(score_text, score_rect) 
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/gameover.mp3') 
    pygame.mixer.music.play() 
    pygame.time.delay(4000) 
    music_background() 

def show_game_win():
    """
    Muestra un mensaje de victoria en la ventana de Pygame. Renderiza el texto "YOU'VE WON!" 
    utilizando la fuente 'Impact' y lo muestra centrado en la pantalla. Luego, carga y reproduce un archivo 
    de música de victoria. Después de una pausa de 1 segundo, llama a la función music_background(). 
    El bloque de código muestra un mensaje de victoria y reproduce música relacionada con la victoria en el juego.
    """

    font = pygame.font.SysFont('Impact', 50) 
    text = font.render("YOU'VE WON!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 150)) 
    screen.blit(text, text_rect) 
    pygame.display.flip() 
    pygame.mixer.music.load('game_sounds/win.mp3') 
    pygame.mixer.music.play() 
    pygame.time.delay(1000)  
    music_background() 

"""" 
Estas funciones se encargan de mostrar mensajes de "Game Over" y "Game Win" en la pantalla del juego, 
reproducir sonidos relacionados y gestionar la música de fondo. 
Se encargan principalmente de realizar acciones visuales y auditivas en el juego.
"""
