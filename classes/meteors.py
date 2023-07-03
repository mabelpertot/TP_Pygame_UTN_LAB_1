import pygame

from .constants import WIDTH, HEIGHT

"""
En el método __init__(), se inicializan los atributos del meteorito, como su imagen, posición inicial, 
dirección en los ejes X e Y, ángulo de rotación y velocidad.
"""

class Meteors(pygame.sprite.Sprite): #Representa un meteorito en el juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image #El atributo original_image almacena la imagen original del meteorito.
        self.image = self.original_image.copy() #El atributo image se inicializa como una copia de la imagen original.
        self.rect = self.image.get_rect() #El rectángulo de colisión (self.rect) se posiciona en las coordenadas iniciales (x, y).
        self.rect.y = y
        self.direction_x = 1 #Los atributos direction_x y direction_y determinan la dirección de movimiento del meteorito en los ejes X e Y.
        self.direction_y = 1 #Con un valor inicial de 1 indicando movimiento hacia la derecha y hacia abajo.
        self.angle = 0 #El atributo angle representa el ángulo de rotación del meteorito, con un valor inicial de 0.
        self.speed = 2

    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.bottom >= HEIGHT + 50 or self.rect.right >= WIDTH + 50:
            self.kill()

        #Se actualiza el ángulo de rotación (self.angle) restando 1 unidad y aplicando un módulo 360 para asegurar que el valor permanezca dentro del rango de 0 a 359.
        #Se rota la imagen original (self.original_image) utilizando la función pygame.transform.rotozoom() para aplicar la rotación en base al ángulo actual.
        #El resultado se asigna a self.image.
        #Se actualiza el rectángulo de colisión (self.rect) para que se ajuste al centro de la imagen rotada.
        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface): #El método draw() se encarga de dibujar el meteorito en una superficie (surface) especificada.
        surface.blit(self.image, self.rect)
        #Se utiliza el método blit() de surface para dibujar la imagen del meteorito (self.image) en la posición de su rectángulo de colisión (self.rect).

class Meteors2(pygame.sprite.Sprite): #Representa otro tipo de meteorito en el juego

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0 #El atributo direction_x se establece en 0, lo que indica que el meteorito no se mueve horizontalmente.
        self.direction_y = 1 #El atributo direction_y se establece en 1, lo que indica que el meteorito se mueve hacia abajo.
        self.angle = 0
        self.speed = 2

    def update(self):
        self.rect.y += self.speed * self.direction_y
    #Se actualiza el movimiento vertical (self.rect.y) multiplicando la velocidad (self.speed) por la dirección vertical (self.direction_y).
        if self.rect.bottom >= HEIGHT + 300:
            self.kill()

        self.angle = (self.angle - 1) % 360
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class BlackHole(pygame.sprite.Sprite): #Representa un agujero negro en el juego

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0 #Se establece en 0, lo que indica que el agujero negro no se mueve horizontalmente.
        self.direction_y = 1 #El atributo direction_y se establece en 1, lo que indica que el agujero negro se mueve hacia abajo.
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

"""
Esta clase representa un agujero negro en el juego que se mueve solo verticalmente. Además, reproduce un 
efecto de sonido específico del agujero negro. El resto de la funcionalidad y el aspecto del agujero negro 
son similares a las clases anteriores.
"""