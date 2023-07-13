import pygame

from .constants import WIDTH, HEIGHT


class Player: #Representa al jugador en el juego.
    """
    Implementación de los métodos de movimiento del jugador, así como los métodos de parada
    para cada dirección de movimiento.
    """

    def __init__(self): #Actualiza la posición el movimiento y la orientación del jugador en el juego.
        self.rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 100, 100, 100) 
        self.speed = 10 
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.original_image = self.image.copy() 
        self.direction = 'down' 

    def move_left(self): # Define el método de movimiento hacia la izquierda del jugador.
        if self.rect.left > 0: 
            self.rect.x -= self.speed 
            self.direction = 'left' 
            self.image = pygame.transform.flip(self.original_image, True, False)
            
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

