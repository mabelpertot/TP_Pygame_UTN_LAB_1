import sys 
import random 


import pygame 
import pygame.mixer 

from classes.constants import WIDTH, HEIGHT, BLACK, WHITE, RED 
from database import create_scores_table,save_score, check_if_table_exists,get_highest_score, get_highscore_name, show_scores

def animate_screen(): # Define una función para animar la pantalla de menú.
    """ 
    Implementa un menú interactivo que permite al usuario seleccionar "Play" para iniciar el juego principal o 
    "Exit" para salir del juego. Utiliza tanto el teclado como el mouse para controlar la selección de los botones
    y anima la pantalla durante la transición al juego principal.
    """

    for i in range(0, 20):
        screen.blit(mainmenu_img, (0, 0)) # Dibuja la imagen del menú principal en la pantalla.
        pygame.display.flip() # Actualiza la pantalla.
        pygame.time.wait(10) # Espera 10 milisegundos.
        screen.blit(mainmenu_img, (random.randint(-5, 5), random.randint(-5, 5))) # Mueve ligeramente la imagen del menú.
        pygame.display.flip()
        pygame.time.wait(10)

pygame.mixer.init() 
pygame.init() 
pygame.mixer.music.load('game_sounds/menu.mp3') 
pygame.mixer.music.set_volume(0.25) 
pygame.mixer.music.play(-1)
pygame.mixer.set_num_channels(20) 

#Repite los pasos 3 a 5 un total de 20 veces para crear una animación en la pantalla del menú.
for i in range(20): 
    channel = pygame.mixer.Channel(i)
    channel.set_volume(0.25)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Space Attack") 
clock = pygame.time.Clock() 

mainmenu_img = pygame.image.load('images/mainmenu.jpg').convert() 
mainmenu_img = pygame.transform.scale(mainmenu_img, (WIDTH, HEIGHT)) 

logo_img = pygame.image.load('images/xxx.jpg').convert_alpha() 
logo_x = (WIDTH - logo_img.get_width()) // 1 
logo_y = -400 

play_button_rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 25, 205, 50) 
quit_button_rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 + 50, 205, 50) 
score_button_rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 + 130, 205, 50)

pygame.mixer.music.load('game_sounds/menu.mp3') 
pygame.mixer.music.play(-1) 
explosion_sound = pygame.mixer.Sound('game_sounds/explosions/explosion1.wav') 
explosion_sound.set_volume(0.25) 
selected_button = 0 
show_menu = True  

while show_menu: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: 
            x, y = event.pos
            if play_button_rect.collidepoint(x, y): 
                explosion_sound.play() 
                animate_screen() 
                show_menu = False
                break

            elif score_button_rect.collidepoint(x, y):
                explosion_sound.play()
                animate_screen()
                show_menu = False
                break

            elif quit_button_rect.collidepoint(x, y):
                pygame.quit()
                sys.exit()
            else:
                selected_button = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                selected_button = 0 
            elif event.key == pygame.K_DOWN: 
                selected_button = 1 
            elif event.key == pygame.K_RETURN: 
                if selected_button == 0:
                    explosion_sound.play() 
                    animate_screen() 
                    show_menu = False 
                    screen.fill(BLACK)  
                    import main 
                    main.main() 
                    break
                elif selected_button == 1: 
                    pygame.quit()   
                    sys.exit()  
    
    screen.blit(mainmenu_img, (0, 0)) # Dibuja la imagen del menú principal en la pantalla.

    screen.blit(logo_img, (logo_x, logo_y)) # Dibuja el logotipo del juego en la pantalla.

    font = pygame.font.SysFont('Calibri', 40) 
    #Botón "Play"
    text = font.render("Play", True, WHITE) 
    pygame.draw.rect(screen, BLACK, play_button_rect, border_radius=10) 
    if selected_button == 0: 
        pygame.draw.rect(screen, RED, play_button_rect, border_radius=10, width=4) 
    text_rect = text.get_rect()
    text_rect.center = play_button_rect.center
    screen.blit(text, text_rect) 
    #Botón "Exit"
    text = font.render("Exit", True, WHITE) 
    pygame.draw.rect(screen, BLACK, quit_button_rect, border_radius=10) 
    if selected_button == 1: 
        pygame.draw.rect(screen, RED, quit_button_rect, border_radius=10, width=4) 
    text_rect = text.get_rect()
    text_rect.center = quit_button_rect.center
    screen.blit(text, text_rect) 
    #Botón "Score"
    text = font.render("Score", True, WHITE) 
    pygame.draw.rect(screen, BLACK, score_button_rect, border_radius=10) 
    if selected_button == 2: 
        pygame.draw.rect(screen, RED, score_button_rect, border_radius=10, width=4) 
    text_rect = text.get_rect()
    text_rect.center = score_button_rect.center
    screen.blit(text, text_rect) 



    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 

