import pygame
import random

from .constants import WIDTH, HEIGHT

"""
class BulletRefill(pygame.sprite.Sprite): define la clase BulletRefill que hereda de pygame.sprite.Sprite, 
lo que permite que el objeto sea utilizado en un grupo de sprites.
def __init__(self, x, y, image): es el método constructor de la clase. Recibe las coordenadas x e y para 
establecer la posición inicial del objeto y la imagen utilizada para representarlo.
super().__init__() llama al constructor de la clase base pygame.sprite.Sprite para inicializar correctamente 
el objeto.
"""

class BulletRefill(pygame.sprite.Sprite): #Representa un objeto de recarga de balas en un juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.rect.x = x
        self.rect.y = y
        self.speed = 1 #Define la velocidad de movimiento del objeto.
        self.direction_x = random.choice([-2, 2]) #Elige aleatoriamente una dirección horizontal para el movimiento del objeto (-2 o 2).
        self.direction_y = random.choice([-2, 2]) #Elige aleatoriamente una dirección vertical para el movimiento del objeto (-2 o 2).
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/bullet_refill.wav")
        self.sound_effect.set_volume(0.4)

    """Es el método de actualización del objeto que se llama en cada iteración del bucle principal del juego. 
    Actualiza la posición del objeto en función de su velocidad y dirección."""
    def update(self):
        self.rect.y += self.speed * self.direction_y #Actualiza la posición vertical del objeto en función de su velocidad y dirección.
        self.rect.x += self.speed * self.direction_x #Actualiza la posición horizontal del objeto en función de su velocidad y dirección.
        self.rect.left = max(self.rect.left, 0) #limita la posición del objeto para que no se salga del lado izquierdo de la pantalla.
        self.rect.right = min(self.rect.right, WIDTH) #limita la posición del objeto para que no se salga del lado derecho de la pantalla.
        self.rect.top = max(self.rect.top, 0) #limita la posición del objeto para que no se salga del lado superior de la pantalla.
        self.rect.bottom = min(self.rect.bottom, HEIGHT) #limita la posición del objeto para que no se salga del lado inferior de la pantalla.
        if random.randint(0, 50) == 0: #Verifica aleatoriamente si se cumple una condición para cambiar la dirección del objeto en forma inversa.
            self.direction_x *= - 1 #Es el método que dibuja el objeto en la pantalla. Recibe una superficie donde se realizará el dibujo.
            self.direction_y *= - 1 #Dibuja la imagen del objeto en la posición definida por su rectángulo.

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    """clase para un objeto de recarga de balas en un juego, controla su movimiento aleatorio en la pantalla, 
    reproduce un efecto de sonido al ser recogido y proporciona métodos para su actualización y dibujo."""

"""class HealthRefill(pygame.sprite.Sprite): define la clase HealthRefill que hereda de pygame.sprite.Sprite, 
    permitiendo que el objeto sea utilizado en un grupo de sprites.
    def __init__(self, x, y, image): es el método constructor de la clase. Recibe las coordenadas x e y 
    para establecer la posición inicial del objeto y la imagen utilizada para representarlo.
    super().__init__() llama al constructor de la clase base pygame.sprite.Sprite para inicializar correctamente 
    el objeto.
"""

class HealthRefill(pygame.sprite.Sprite): #Representa un objeto de recarga de salud en un juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.rect.x = x #Establece la coordenada x del rectángulo del objeto.
        self.rect.y = y # establece la coordenada y del rectángulo del objeto.
        self.speed = 1
        self.direction_x = random.choice([-2, 2])
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/health_refill.wav")
        self.sound_effect.set_volume(0.4)

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH) #limita la posición del objeto para que no se salga del lado derecho de la pantalla.
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT) #limita la posición del objeto para que no se salga del lado inferior de la pantalla.
        if random.randint(0, 50) == 0: #Verifica aleatoriamente si se cumple una condición para cambiar la dirección del objeto en forma inversa.
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface): #Es el método que dibuja el objeto en la pantalla. Recibe una superficie donde se realizará el dibujo.
        surface.blit(self.image, self.rect) #Dibuja la imagen del objeto en la posición definida por su rectángulo.

    """clase para un objeto de recarga de salud en un juego, controla su movimiento aleatorio en la pantalla, 
    reproduce un efecto de sonido al ser recogido y proporciona métodos para su actualización y dibujo."""

"""class DoubleRefill(pygame.sprite.Sprite): define la clase DoubleRefill que hereda de pygame.sprite.Sprite, 
lo que permite que el objeto sea utilizado en un grupo de sprites.
def __init__(self, x, y, image): es el método constructor de la clase. Recibe las coordenadas x e y para 
establecer la posición inicial del objeto y la imagen utilizada para representarlo.
super().__init__() llama al constructor de la clase base pygame.sprite.Sprite para inicializar correctamente 
el objeto."""

class DoubleRefill(pygame.sprite.Sprite): #Representa un objeto de recarga doble en un juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction_x = random.choice([-2, 2])
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/double_refill.mp3")
        self.sound_effect.set_volume(0.4)

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
        if random.randint(0, 50) == 0:
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    """clase para un objeto de recarga doble en un juego, controla su movimiento aleatorio en la pantalla, 
    reproduce un efecto de sonido al ser recogido y proporciona métodos para su actualización y dibujo."""

"""
class ExtraScore(pygame.sprite.Sprite): define la clase ExtraScore que hereda de pygame.sprite.Sprite, lo que 
permite que el objeto sea utilizado en un grupo de sprites.
def __init__(self, x, y, image): es el método constructor de la clase. Recibe las coordenadas x e y para establecer 
la posición inicial del objeto y la imagen utilizada para representarlo.
super().__init__() llama al constructor de la clase base pygame.sprite.Sprite para inicializar correctamente el 
objeto.
"""

class ExtraScore(pygame.sprite.Sprite): #Representa un objeto de puntuación extra en un juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy() #Crea una copia de la imagen original para que se pueda modificar sin afectar la original.
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.speed = 2
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 0 #Establece la dirección horizontal del movimiento del objeto como cero, NO se mueve horizontalmente.
        self.direction_y = 1 #Establece la dirección vertical del movimiento del objeto como 1, SE mueve hacia abajo.
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/extra_score.mp3")
        self.sound_effect.set_volume(0.4)

    def update(self):
        self.rect.y += self.speed * self.direction_y

        if self.rect.bottom >= HEIGHT + 100: #Verifica si la parte inferior del objeto ha alcanzado o superado una posición más allá de la pantalla.
            self.kill() #Elimina el objeto del grupo de sprites al alcanzar o superar esa posición, lo que significa que ya no se mostrará ni se actualizará.

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    """
    Clase para un objeto de puntuación extra en un juego, controla su movimiento hacia abajo en la pantalla, 
    reproduce un efecto de sonido al ser recogido y proporciona métodos para su actualización y dibujo."""    
