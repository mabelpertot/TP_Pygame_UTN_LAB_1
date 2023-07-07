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
        self.image = image #Se establece como la imagen proporcionada.
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.rect.x = x #Establecer la posición inicial del objeto de recarga de balas en X
        self.rect.y = y #Establecer la posición inicial del objeto de recarga de balas en Y
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

    def draw(self, surface): #Recibe dos parámetro: Es la superficie de juego en la que se desea dibujar el objeto de recarga de balas.
        surface.blit(self.image, self.rect) #se utiliza para dibujar la imagen del objeto de recarga de balas en la superficie de juego especificada.
    
class HealthRefill(pygame.sprite.Sprite): #Representa un objeto de recarga de salud en un juego.
    """
     La clase representa un objeto de recarga de salud en un juego. Tiene métodos para 
     inicializar el objeto, actualizar su posición y dibujarlo en una superficie de juego.
     """
    def __init__(self, x, y, image): #Recibe los parámetros x e y, que representan las coordenadas de posición del objeto de recarga de salud, y image, que es la imagen del objeto.
        super().__init__()
        self.image = image #Imagen del objeto de recarga de salud.
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.rect.x = x #Establece la coordenada x del rectángulo del objeto.
        self.rect.y = y # establece la coordenada y del rectángulo del objeto.
        self.speed = 1 #Establece la velocidad del objeto en el juego.
        self.direction_x = random.choice([-2, 2]) #Esto elige aleatoriamente una dirección en X para el movimiento de la bala.
        self.direction_y = random.choice([-2, 2]) #Esto elige aleatoriamente una dirección en Y para el movimiento de la bala..
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/health_refill.wav")
        self.sound_effect.set_volume(0.4) #Se establece el volumen del sonido 

    def update(self):
        """
        Actualiza la posición del objeto en cada iteración del juego y verifica si se cumple
        una condición para cambiar la dirección del objeto.
        """
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

class DoubleRefill(pygame.sprite.Sprite): #Representa un objeto de recarga doble en un juego.
    """
    La clase representa un objeto de recarga doble en un juego. Tiene métodos para 
    inicializar el objeto, actualizar su posición y dibujarlo en una superficie de juego. 
    El método update actualiza la posición del objeto y verifica la dirección de movimiento. 
    El método draw se encarga de dibujar el objeto en la superficie. 
    """
    def __init__(self, x, y, image): #Recibe los parámetros x e y, que representan las coordenadas de posición del objeto de recarga doble, y image, que es la imagen del objeto.
        self.image = image #Imagen del objeto de recarga doble.
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.rect.x = x #Establece la coordenada x del rectángulo del objeto.
        self.rect.y = y #Establece la coordenada y del rectángulo del objeto.
        self.speed = 2 #Define la velocidad de movimiento del objeto.
        self.direction_x = random.choice([-2, 2]) #Esto elige aleatoriamente una dirección en X para el movimiento del objeto.
        self.direction_y = random.choice([-2, 2]) ## Esto elige aleatoriamente una dirección en Y para el movimiento del objeto.
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/double_refill.mp3") #Carga un efecto de sonido desde un archivo de sonido.
        self.sound_effect.set_volume(0.4) #Establece el volumen del sonido.

    def update(self): #Actualiza la posición del objeto en cada iteración del juego y verifica si se cumple una condición para cambiar la dirección del objeto.
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
        if random.randint(0, 50) == 0: #Verifica aleatoriamente si se cumple una condición para cambiar la dirección del objeto en forma inversa.
            self.direction_x *= - 1
            self.direction_y *= - 1

    def draw(self, surface): #Recibe el parametro 'surface' Superficie de juego en la que se desea dibujar el objeto.
        surface.blit(self.image, self.rect) # Dibuja el objeto en la pantalla.

class ExtraScore(pygame.sprite.Sprite): #Representa un objeto de puntuación extra en un juego.
    """
    Representa un objeto de puntuación extra en un juego. Tiene métodos para inicializar el objeto, 
    actualizar su posición, dibujarlo en una superficie de juego y eliminarlo cuando alcance una posición determinada.
    """
    def __init__(self, x, y, image): #Recibe los parámetros x, y e image, que representan la posición y la imagen del objeto de puntuación extra.
        super().__init__()
        self.original_image = image # se establece como una copia de la imagen original para permitir modificaciones sin afectar la imagen original. 
        self.image = self.original_image.copy() #Crea una copia de la imagen original para que se pueda modificar sin afectar la original.
        self.rect = self.image.get_rect() #Crea un rectángulo que encierra el objeto y se utiliza para gestionar su posición y colisiones.
        self.speed = 2 #Define la velocidad de movimiento del objeto.
        self.rect.x = x #Establece la coordenada x del rectángulo del objeto.
        self.rect.y = y #Establece la coordenada Y del rectángulo del objeto.
        self.direction_x = 0 #Establece la dirección horizontal del movimiento del objeto como cero, NO se mueve horizontalmente.
        self.direction_y = 1 #Establece la dirección vertical del movimiento del objeto como 1, SE mueve hacia abajo.
        self.sound_effect = pygame.mixer.Sound("game_sounds/refill/extra_score.mp3")
        self.sound_effect.set_volume(0.4)

    def update(self):
        self.rect.y += self.speed * self.direction_y
        #Actualiza la posición del objeto en cada iteración del juego. Incrementa la posición vertical (self.rect.y) del objeto según su velocidad (self.speed) y dirección vertical (self.direction_y).
        if self.rect.bottom >= HEIGHT + 100: #Verifica si la parte inferior del objeto ha alcanzado o superado una posición más allá de la pantalla.
            self.kill() #Elimina el objeto del grupo de sprites al alcanzar o superar esa posición, lo que significa que ya no se mostrará ni se actualizará.

    def draw(self, surface): #se utiliza para dibujar el objeto en una superficie de juego. 
        surface.blit(self.image, self.rect) #Se utiliza el método blit de la superficie para dibujar la imagen del objeto en la posición definida por su rectángulo.
