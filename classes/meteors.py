import pygame

from .constants import WIDTH, HEIGHT

class Meteors(pygame.sprite.Sprite): #Representa un meteorito en el juego.
    """
    Representa un meteorito en un juego y contiene atributos para almacenar la imagen del meteorito, 
    su posición, dirección de movimiento, ángulo de rotación y velocidad.
    """
    def __init__(self, x, y, image): #recibe tres parámetros: x y y representan las coordenadas iniciales del meteorito, y image es la imagen del meteorito.
        super().__init__()
        self.original_image = image #Se almacena la imagen original del meteorito.
        self.image = self.original_image.copy() #Se crea una copia de la imagen original y se asigna al atributo image. Esto se hace para poder rotar la imagen sin afectar a la original.
        self.rect = self.image.get_rect() #Se crea un rectángulo de colisión a partir de la imagen y se asigna al atributo rect. El rectángulo se posiciona en las coordenadas iniciales (x, y).
        self.rect.y = y
        self.rect.x = x
        self.direction_x = 1 #Determinan la dirección de movimiento del meteorito en los ejes X. Con valor inicial 1 indica movimiento hacia la derecha y hacia abajo.
        self.direction_y = 1 #Determinan la dirección de movimiento del meteorito en los ejes Y. Con valor inicial 1 indica movimiento hacia la derecha y hacia abajo.
        self.angle = 0 #Representa el ángulo de rotación del meteorito, con un valor inicial de 0.
        self.speed = 2 #Representa la velocidad en que se mueve el meteorito en el juego.

    def update(self): #Método de actualización el meteorito.
        """
        Estos métodos permiten actualizar la posición, la rotación y el dibujo del sprite 
        en cada iteración del bucle principal del juego.
        """
        self.rect.x += self.speed * self.direction_x #Actualiza la posición del meteorito según su velocidad y direcciones sumando el desplazamiento en las coordenadas x e y.
        self.rect.y += self.speed * self.direction_y
        if self.rect.bottom >= HEIGHT + 50 or self.rect.right >= WIDTH + 50: #Verifica si el rectángulo está fuera de los límites de la ventana del juego. Si el rectángulo se encuentra más allá del borde inferior o del borde derecho
            self.kill() #se elimina

        self.angle = (self.angle - 1) % 360 #Actualiza el ángulo de rotación restando 1 y obteniendo el resto de la división por 360. Esto produce un efecto de rotación continua.
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1) #rota y redimensiona la imagen original según el ángulo y un factor de escala de 1. El resultado se guarda.
        self.rect = self.image.get_rect(center=self.rect.center) #Actualiza el rectángulo para que el centro permanezca en la misma posición

    def draw(self, surface): #Recibe un único argumento: surface: La superficie en la cual se va a dibujar el sprite.
        surface.blit(self.image, self.rect) #Dibuja el sprite en la superficie especificada (surface) utilizando el método blit()
        #Se encarga de dibujar el sprite en dicha superficie.

class Meteors2(pygame.sprite.Sprite): #Representa otro tipo de meteorito en el juego
    """
    Representa otro tipo de meteorito en un juego y contiene métodos para actualizar su posición 
    y rotación, y para dibujarlo en la pantalla del juego.
    """
    def __init__(self, x, y, image): 
        super().__init__()
        self.original_image = image #Se almacena la imagen original del meteorito. 
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

