import pygame,os
from classes.constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))

""""
music_background->Carga un archivo de música de fondo utilizando el módulo pygame.mixer.music. 
Ajusta el volumen de la música a 0.25 y la reproduce en bucle (loops=-1).
"""

def music_background():
    pygame.mixer.music.load('game_sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)

"""
show_game_over -> toma un parámetro score que representa la puntuación final del jugador. 
Dentro de la función, se configuran las fuentes de texto utilizando pygame.font.SysFont 
Se crea un mensaje de "GAME OVER" utilizando la fuente de 50 píxeles y se renderiza en 
una superficie de texto. Se obtiene el rectángulo que enmarca el texto y se centra en la 
pantalla utilizando text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50)).
 Se blit (dibuja) el texto en la superficie de la pantalla (screen.blit(text, text_rect)) 
 y se actualiza la pantalla con pygame.display.flip() para mostrar los mensajes de "GAME OVER" 
 y la puntuación final.
"""

def show_game_over(score):
    font = pygame.font.SysFont('Impact', 50)
    font_small = pygame.font.SysFont('Impact', 30)
    text = font.render("GAME OVER", True, (139, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/gameover.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(4000)
    music_background()

"""
show_game_win -> configura la fuente de texto utilizando pygame.font.SysFont.
Se crea un mensaje de "AWESOME! GO ON!" utilizando la fuente de 50 píxeles y se renderiza en 
una superficie de texto. Se obtiene el rectángulo que enmarca el texto y se centra en la 
pantalla utilizando text.get_rect(center=(WIDTH/2, HEIGHT/2)).
Luego, se blit (dibuja) el texto en la superficie de la pantalla (screen.blit(text, text_rect)) y se 
actualiza la pantalla con pygame.display.flip() para mostrar el mensaje de "Game Win".
"""

def show_game_win():
    font = pygame.font.SysFont('Impact', 50)
    text = font.render("AWESOME! GO ON!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
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