import pygame

class Bullet(pygame.sprite.Sprite): #La clase representa un objeto de bala en el juego.
    """
    La clase representa una bala en el juego. Al crear una instancia de la clase, se carga 
    una imagen de bala, se establece su posición inicial, velocidad y sonido de disparo.
    """
    def __init__(self, x, y): #Recibe dos parámetros: las coordenadas x e y que representan la posición inicial de la bala.
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha() #Se carga la imagen de la bala desde un archivo y se almacena en el atributo image.
        self.rect = self.image.get_rect() #Se obtiene el rectángulo de colisión de la imagen de la bala y se almacena en el atributo rect.
        self.rect.centerx = x #Se establece la posición inicial del rectángulo de colisión en el centro horizontal (self.rect.centerx = x).
        self.rect.bottom = y - 10 # y justo encima de la posición y (self.rect.bottom = y - 10)
        self.speed = 8 #Establece la velocidad de la bala a 8, determinando qué tan rápido se moverá en el juego.
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3') # Carga un efecto de sonido de disparo del archivo de sonido especificado y lo asigna al atributo self.shoot_sound.
        self.shoot_sound.set_volume(0.4) #Establece el volumen del efecto de sonido de disparo al 40% de su volumen máximo.
        self.shoot_sound.play() #Reproduce el efecto de sonido de disparo.

    def update(self):  #Método de actualización de la bala. Se llama en cada fotograma para actualizar la posición de la bala.
        """ El método update se encarga de mover la bala hacia arriba en cada 
        fotograma y eliminarla si alcanza el límite superior de la pantalla.
        """
        self.rect.move_ip(0, -self.speed) #El rectángulo de colisión de la bala se mueve hacia arriba según la velocidad especificada.
        if self.rect.top <= 1: #Se verifica si la parte superior del rectángulo de colisión ha alcanzado o superado el límite superior de la pantalla.
            self.kill()
            #Si la parte superior del rectángulo de colisión está por debajo o en el límite superior de la pantalla, se llama al método kill() para eliminar la instancia de la bala.