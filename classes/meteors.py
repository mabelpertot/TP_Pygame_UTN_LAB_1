import pygame

from .constants import WIDTH, HEIGHT

class Meteors(pygame.sprite.Sprite): #Representa un meteorito en el juego.
    """
    Representa un meteorito en un juego y contiene atributos para almacenar la imagen del meteorito, 
    su posición, dirección de movimiento, ángulo de rotación y velocidad.
    """
    def __init__(self, x, y, image): #recibe tres parámetros: x y y representan las coordenadas iniciales del meteorito, y image es la imagen del meteorito.
        super().__init__()
        self.original_image = image 
        self.image = self.original_image.copy() 
        self.rect = self.image.get_rect() 
        self.rect.y = y
        self.rect.x = x
        self.direction_x = 1 
        self.direction_y = 1 
        self.angle = 0 
        self.speed = 2 

    def update(self): #Método que actualiza el meteorito.
        """
        Estos métodos permiten actualizar la posición, la rotación y el dibujo del sprite 
        en cada iteración del bucle principal del juego.
        """
        self.rect.x += self.speed * self.direction_x 
        self.rect.y += self.speed * self.direction_y
        if self.rect.bottom >= HEIGHT + 50 or self.rect.right >= WIDTH + 50: 
            self.kill() 

        self.angle = (self.angle - 1) % 360 
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1) 
        self.rect = self.image.get_rect(center=self.rect.center) 

    def draw(self, surface):
        surface.blit(self.image, self.rect) 
       
class Meteors2(pygame.sprite.Sprite): #Representa otro tipo de meteorito en el juego
    """
    Representa otro tipo de meteorito en un juego y contiene métodos para actualizar su posición 
    y rotación, y para dibujarlo en la pantalla del juego.
    """
    def __init__(self, x, y, image): 
        super().__init__()
        self.original_image = image 
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0
        self.direction_y = 1 
        self.angle = 0
        self.speed = 2

    def update(self):
        self.rect.y += self.speed * self.direction_y
        if self.rect.bottom >= HEIGHT + 300:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class BlackHole(pygame.sprite.Sprite): #Representa un agujero negro en el juego
    """
    Las tres clases comparten similitudes en términos de herencia, atributos comunes y métodos comunes. 
    Sin embargo, se diferencian en su comportamiento, apariencia y atributos específicos que 
    controlan su movimiento y sonido.
    """
    def __init__(self, x, y, image): #Recibe tres parámetros: x y y representan las coordenadas iniciales del agujero negro, y image es la imagen del agujero negro.
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0 
        self.direction_y = 1 
        self.angle = 0
        self.speed = 2
        self.sound_effect = pygame.mixer.Sound("game_sounds/damage/black_hole.mp3")

    def update(self):
        self.rect.y += self.speed * self.direction_y

        if self.rect.bottom >= HEIGHT + 300:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

