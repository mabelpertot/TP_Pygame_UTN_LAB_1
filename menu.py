import sys # Importa el módulo sys para interactuar con el intérprete de Python.
import random # Importa el módulo random para generar números aleatorios.

import pygame # Importa el módulo pygame para crear juegos y aplicaciones multimedia.
import pygame.mixer # Importa el módulo mixer de pygame para controlar la reproducción de sonidos.

from classes.constants import WIDTH, HEIGHT, BLACK, WHITE, RED # Importa constantes desde el módulo llamado "constants".


def animate_screen(): # Define una función para animar la pantalla de menú.
    for i in range(0, 20):
        screen.blit(mainmenu_img, (0, 0)) # Dibuja la imagen del menú principal en la pantalla.
        pygame.display.flip() # Actualiza la pantalla.
        pygame.time.wait(10) # Espera 10 milisegundos.
        screen.blit(mainmenu_img, (random.randint(-5, 5), random.randint(-5, 5))) # Mueve ligeramente la imagen del menú.
        pygame.display.flip()
        pygame.time.wait(10)


pygame.mixer.init() # Inicializa el mezclador de sonido de pygame.
pygame.init() # Inicializa los módulos de pygame.
pygame.mixer.music.load('game_sounds/menu.mp3') # Carga un archivo de música de fondo.
pygame.mixer.music.set_volume(0.25) # Establece el volumen de la música de fondo.
pygame.mixer.music.play(-1) # Reproduce la música de fondo en bucle infinito.
pygame.mixer.set_num_channels(20) # Establece el número máximo de canales de sonido simultáneos.
for i in range(20): # Crea y configura 20 canales de sonido con un volumen predeterminado.
    channel = pygame.mixer.Channel(i)
    channel.set_volume(0.25)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Crea una ventana de visualización con un tamaño específico.
pygame.display.set_caption("Space Attack") # Establece el título de la ventana.
clock = pygame.time.Clock() # Crea un objeto Clock para controlar el tiempo de actualización de la pantalla.

mainmenu_img = pygame.image.load('images/mainmenu.jpg').convert() # Carga una imagen para el fondo del menú.
mainmenu_img = pygame.transform.scale(mainmenu_img, (WIDTH, HEIGHT)) # Escala la imagen para que se ajuste a la ventana.

logo_img = pygame.image.load('images/xxx.jpg').convert_alpha() # Carga una imagen del logotipo del juego con transparencia.
logo_x = (WIDTH - logo_img.get_width()) // 1 # Calcula la posición horizontal del logotipo.
logo_y = -400 # Establece una posición vertical inicial del logotipo fuera de la pantalla.

play_button_rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 25, 205, 50) # Crea un rectángulo para el botón "Play".
quit_button_rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 + 50, 205, 50) # Crea un rectángulo para el botón "Quit".

pygame.mixer.music.load('game_sounds/menu.mp3') # Carga nuevamente la música de fondo.
pygame.mixer.music.play(-1) # Reproduce la música de fondo en bucle infinito.
explosion_sound = pygame.mixer.Sound('game_sounds/explosions/explosion1.wav') # Carga un sonido de explosión.
explosion_sound.set_volume(0.25) # Establece el volumen del sonido de explosión.
selected_button = 0 # Indica el botón seleccionado actualmente.
show_menu = True  # Indica si se debe mostrar el menú o no.

while show_menu: # Bucle principal del menú.
    for event in pygame.event.get(): # Obtiene los eventos pygame.
        if event.type == pygame.QUIT: # Si se produce un evento de cierre de ventana.
            pygame.quit() # Cierra pygame.
            sys.exit() # Termina el programa.

        if event.type == pygame.MOUSEBUTTONDOWN: # Si se produce un evento de clic del mouse.
            x, y = event.pos
            if play_button_rect.collidepoint(x, y): # Si se hace clic en el botón "Play".
                explosion_sound.play() # Reproduce el sonido de explosión.
                animate_screen() # Anima la pantalla.
                show_menu = False # Deja de mostrar el menú.
                import main # Importa el módulo llamado "main".
                main.main() # Ejecuta la función "main()" del módulo importado.
                break
            elif quit_button_rect.collidepoint(x, y): # Si se hace clic en el botón "Quit".
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN: # Si se produce un evento de pulsación de tecla.
            if event.key == pygame.K_UP: # Si se pulsa la tecla hacia arriba.
                selected_button = 0 # Establece el botón seleccionado como "Play".
            elif event.key == pygame.K_DOWN: # Si se pulsa la tecla hacia abajo.
                selected_button = 1 # Establece el botón seleccionado como "Quit".
            elif event.key == pygame.K_RETURN: # Si se pulsa la tecla Enter.
                if selected_button == 0: # Si el botón seleccionado es "Play".
                    explosion_sound.play() # Reproduce el sonido de explosión.
                    animate_screen() # Anima la pantalla.
                    show_menu = False # Deja de mostrar el menú.
                    screen.fill(BLACK)  # Rellena la pantalla de negro.
                    import main # Importa el módulo llamado "main".
                    main.main() # Ejecuta la función "main()" del módulo importado.
                    break
                elif selected_button == 1: # Si el botón seleccionado es "Quit".
                    pygame.quit()   # Cierra pygame.
                    sys.exit()  # Termina el programa.
    
    screen.blit(mainmenu_img, (0, 0)) # Dibuja la imagen del menú principal en la pantalla.

    screen.blit(logo_img, (logo_x, logo_y)) # Dibuja el logotipo del juego en la pantalla.

    font = pygame.font.SysFont('Calibri', 40) # Crea una fuente de texto.
    text = font.render("Play", True, WHITE) # Renderiza el texto "Play" con la fuente y el color especificados.
    pygame.draw.rect(screen, BLACK, play_button_rect, border_radius=10) # Dibuja un rectángulo para el botón "Play".
    if selected_button == 0: # Si el botón "Play" está seleccionado.
        pygame.draw.rect(screen, RED, play_button_rect, border_radius=10, width=4) # Dibuja un borde rojo alrededor del botón.
    text_rect = text.get_rect()
    text_rect.center = play_button_rect.center
    screen.blit(text, text_rect) # Dibuja el texto en el centro del botón "Play".
    text = font.render("Exit", True, WHITE) # Renderiza el texto "Exit" con la fuente y el color especificados.
    pygame.draw.rect(screen, BLACK, quit_button_rect, border_radius=10) # Dibuja un rectángulo para el botón "Quit".
    if selected_button == 1: # Si el botón "Quit" está seleccionado.
        pygame.draw.rect(screen, RED, quit_button_rect, border_radius=10, width=4) # Dibuja un borde rojo alrededor del botón.
    text_rect = text.get_rect()
    text_rect.center = quit_button_rect.center
    screen.blit(text, text_rect) 
    pygame.display.flip() # Actualiza la pantalla.
    clock.tick(60) # Limita la velocidad de actualización a 60 cuadros por segundo.

pygame.quit() # Cierra pygame.

"""
Este bloque implementa un menú principal interactivo, donde los usuarios pueden seleccionar "Play" para iniciar el 
juego principal o "Exit" para salir del juego. Se utiliza el teclado para controlar la selección de los botones.
"""
