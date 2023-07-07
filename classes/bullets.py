import pygame

class Bullet(pygame.sprite.Sprite): #La clase representa un objeto de bala en el juego.
    """
    La clase representa una bala en el juego. Al crear una instancia de la clase, se carga 
    una imagen de bala, se establece su posición inicial, velocidad y sonido de disparo.
    """
    def __init__(self, x, y): #Recibe dos parámetros: las coordenadas x e y que representan la posición inicial de la bala.
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha() 
        self.rect = self.image.get_rect() 
        self.rect.centerx = x 
        self.rect.bottom = y - 10 
        self.speed = 8 
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3') 
        self.shoot_sound.set_volume(0.4) 
        self.shoot_sound.play() 

    def update(self):  #Método de actualización de la bala. Se llama en cada fotograma para actualizar la posición de la bala.
        """ El método update se encarga de mover la bala hacia arriba en cada 
        fotograma y eliminarla si alcanza el límite superior de la pantalla.
        """
        self.rect.move_ip(0, -self.speed) 
        if self.rect.top <= 1: 
            self.kill()
            