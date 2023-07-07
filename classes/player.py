import pygame

from .constants import WIDTH, HEIGHT


class Player: #Representa al jugador en el juego.
    """
    Implementación de los métodos de movimiento del jugador, así como los métodos de parada
    para cada dirección de movimiento.
    """

    def __init__(self): #Actualiza la posición el movimiento y la orientación del jugador en el juego.
        self.rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 100, 100, 100)  #Crea un rectángulo para representar la posición y el tamaño del jugador. 
       #El jugador se coloca en el centro horizontal de la pantalla (WIDTH//2 - 100), en la parte inferior de la pantalla y tiene un tamaño de 100x100 píxeles.
        self.speed = 10 #Establece la velocidad de movimiento del jugador en 10.
        self.image = pygame.image.load('images/player.png').convert_alpha() #Carga la imagen del jugador desde un archivo  y la asigna al atributo "image" del jugador. El método convert_alpha() se utiliza para optimizar la imagen para su uso.
        self.original_image = self.image.copy() # Crea una copia de la imagen original del jugador y la asigna al atributo "original_image". Esto se utiliza para mantener una referencia a la imagen original antes de realizar transformaciones.
        self.direction = 'down' #Establece la dirección de movimiento inicial del jugador como "abajo".

    def move_left(self): # Define el método de movimiento hacia la izquierda del jugador.
        if self.rect.left > 0: #Verifica si el lado izquierdo del rectángulo del jugador está dentro de los límites de la ventana de juego (mayor que 0).
            self.rect.x -= self.speed #Resta la velocidad del jugador a la coordenada x de su rectángulo, moviéndolo hacia la izquierda.
            self.direction = 'left' #Establece la dirección del jugador como "izquierda".
            self.image = pygame.transform.flip(self.original_image, True, False)
            #Voltea horizontalmente la imagen original del jugador y la asigna como la nueva imagen del jugador. Esto se utiliza para mostrar al jugador mirando hacia la izquierda.
    """
    El resto de los métodos siguen una estructura similar para mover al jugador en diferentes 
    direcciones y actualizar su imagen en consecuencia.
    """
    def move_right(self): #Define el movimiento del jugador hacia la derecha.
        if self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.direction = 'right'
            self.image = self.original_image

    def move_up(self): #Define el movimiento del jugador hacia arriba.
        if self.rect.top > 0:
            self.rect.y -= self.speed
            self.direction = 'up'

    def move_down(self): #Define el movimiento del jugador hacia abajo.
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            self.direction = 'down'

    #Combinan movimientos diagonales.
    def move_up_left(self):
        if self.rect.top > 0 and self.rect.left > 0:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.direction = 'up_left'

    def move_up_right(self):
        if self.rect.top > 0 and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.direction = 'up_right'

    def move_down_left(self):
        if self.rect.bottom < HEIGHT and self.rect.left > 0:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.direction = 'down_left'

    def move_down_right(self):
        if self.rect.bottom < HEIGHT and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.direction = 'down_right'

    #Se pueden implementar para detener el movimiento en la dirección correspondiente.
    def stop(self):
        pass

    def stop_left(self):
        pass

    def stop_right(self):
        pass

    def stop_up(self):
        pass

    def stop_down(self):
        pass
