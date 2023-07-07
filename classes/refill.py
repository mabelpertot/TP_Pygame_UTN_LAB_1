import pygame
import random

from .constants import WIDTH, HEIGHT

class BulletRefill(pygame.sprite.Sprite): #Representa un objeto de recarga de balas en un juego.
    """
    Esta clase define un objeto de recarga de balas en un juego. Tiene atributos para la imagen, 
    la posición, la velocidad y las direcciones de movimiento del objeto. También incluye un efecto 
    de sonido asociado al objeto.
    """
    def __init__(self, x, y, image): #Recibe los parámetros x e y que representan las coordenadas de posición del objeto de recarga de balas, y image que es la imagen del objeto.
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
        self.speed = 1 
        self.direction_x = random.choice([-2, 2]) 
        self.direction_y = random.choice([-2, 2]) 
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/bullet_refill.wav")
        self.sound_effect.set_volume(0.4)

    """Es el método de actualización del objeto que se llama en cada iteración del bucle principal del juego. 
    Actualiza la posición del objeto en función de su velocidad y dirección."""
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
    
class HealthRefill(pygame.sprite.Sprite): #Representa un objeto de recarga de salud en un juego.
    """
     La clase representa un objeto de recarga de salud en un juego. Tiene métodos para 
     inicializar el objeto, actualizar su posición y dibujarlo en una superficie de juego.
     """
    def __init__(self, x, y, image): #Recibe los parámetros x e y, que representan las coordenadas de posición del objeto de recarga de salud, y image, que es la imagen del objeto.
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y
        self.speed = 1 
        self.direction_x = random.choice([-2, 2]) 
        self.direction_y = random.choice([-2, 2])
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/health_refill.wav")
        self.sound_effect.set_volume(0.4) 

    def update(self):
        """
        Actualiza la posición del objeto en cada iteración del juego y verifica si se cumple
        una condición para cambiar la dirección del objeto.
        """
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH) 
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT) 
        if random.randint(0, 50) == 0: 
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface): #Método que dibuja el objeto en la pantalla. Recibe una superficie donde se realizará el dibujo.
        surface.blit(self.image, self.rect) 

class DoubleRefill(pygame.sprite.Sprite): #Representa un objeto de recarga doble en un juego.
    """
    La clase representa un objeto de recarga doble en un juego. Tiene métodos para 
    inicializar el objeto, actualizar su posición y dibujarlo en una superficie de juego. 
    El método update actualiza la posición del objeto y verifica la dirección de movimiento. 
    El método draw se encarga de dibujar el objeto en la superficie. 
    """
    def __init__(self, x, y, image): #Recibe los parámetros x e y, que representan las coordenadas de posición del objeto de recarga doble, y image, que es la imagen del objeto.
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

    def update(self): #Actualiza la posición del objeto en cada iteración del juego y verifica si se cumple una condición para cambiar la dirección del objeto.
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

class ExtraScore(pygame.sprite.Sprite): #Representa un objeto de puntuación extra en un juego.
    """
    Representa un objeto de puntuación extra en un juego. Tiene métodos para inicializar el objeto, 
    actualizar su posición, dibujarlo en una superficie de juego y eliminarlo cuando alcance una posición determinada.
    """
    def __init__(self, x, y, image): #Recibe los parámetros x, y e image, que representan la posición y la imagen del objeto de puntuación extra.
        super().__init__()
        self.original_image = image 
        self.image = self.original_image.copy() 
        self.rect = self.image.get_rect() 
        self.speed = 2 
        self.rect.x = x 
        self.rect.y = y 
        self.direction_x = 0 
        self.direction_y = 1 
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/extra_score.mp3")
        self.sound_effect.set_volume(0.4)

    def update(self):
        self.rect.y += self.speed * self.direction_y
        
        if self.rect.bottom >= HEIGHT + 100: 
            self.kill() 

    def draw(self, surface): 
        surface.blit(self.image, self.rect) 
