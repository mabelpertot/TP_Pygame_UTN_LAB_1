import pygame

"""
def __init__(self, x, y): es el constructor de la clase. Toma dos parámetros: x y y, 
representan las coordenadas de la posición inicial de la bala."""

class Bullet(pygame.sprite.Sprite): #La clase representa un objeto de bala en el juego.

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x #Se establece la posición inicial del rectángulo de colisión en el centro horizontal (self.rect.centerx = x).
        self.rect.bottom = y - 10 # y justo encima de la posición y (self.rect.bottom = y - 10)
        self.speed = 8
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    #Es el método de actualización de la bala. Se llama en cada fotograma para actualizar la posición de la bala.
    def update(self):
        self.rect.move_ip(0, -self.speed)
    #se mueve el rectángulo de colisión hacia arriba (self.rect.move_ip(0, -self.speed)).
        if self.rect.top <= 1:
            self.kill()
    #Se verifica si la parte superior del rectángulo de colisión (self.rect.top) está por debajo o igual a 1. 
    # Si es así, significa que la bala ha salido de la pantalla, por lo que se elimina llamando al método kill().

"""
Esta clase representa una bala en el juego. Al crear una instancia de Bullet, se carga una imagen de bala, 
se establece su posición inicial, se reproduce un sonido de disparo y se actualiza su posición en cada fotograma. 
Si la bala sale de la pantalla, se elimina."""