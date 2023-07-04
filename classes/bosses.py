import pygame
import random
import math

from .constants import WIDTH, HEIGHT



class Boss1(pygame.sprite.Sprite): #Representa al jefe en el juego.
    """ En el método __init__(), inicializan los atributos del jefe, como su imagen, posición, velocidad, 
    dirección, temporizador de disparo y cantidad de disparos realizados."""
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6
        self.direction = random.choice([(-1, 0), (1, 0)])
        self.shoot_timer = 0
        self.shots_fired = 0

    """
    En el método update(), se actualiza la posición del jefe para que se mueva de forma sinusoidal 
    en el eje X e Y.
    Si el número de disparos realizados es menor que 10, el jefe se mueve en una dirección horizontal, 
    disparando balas cada 60 fotogramas.
    Una vez que se han realizado 10 disparos, el jefe aumenta su velocidad y persigue al jugador.
    """

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 3
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 3
        if self.shots_fired < 10:
            dx, dy = self.direction
            self.rect.x += dx * self.speed
            self.rect.y = max(self.rect.y, 50)

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction = (1, 0)
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction = (-1, 0)

            self.shoot_timer += 1
            if self.shoot_timer >= 60:
                bullet1 = Boss1Bullet(self.rect.centerx - 20, self.rect.bottom)
                bullet2 = Boss1Bullet(self.rect.centerx + 20, self.rect.bottom)
                bullet3 = Boss1Bullet(self.rect.centerx, self.rect.bottom)
                enemy_bullets_group.add(bullet1, bullet2, bullet3)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            self.speed = 10
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

class Boss1Bullet(pygame.sprite.Sprite): #Representa las balas disparadas por el jefe.

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bulletboss1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 8
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss1shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()
    """
    En el método update(), se actualiza la posición de la bala para que se mueva hacia abajo.
    Si la bala sale de la pantalla, se elimina.
    """
    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.kill()

class Boss2(pygame.sprite.Sprite): #Representa al segundo jefe en el juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        self.direction_x, self.direction_y = self.direction
        self.shoot_timer = 0
        self.shots_fired = 0

    """
    En el método update(), se actualiza la posición del jefe para que se mueva de forma sinusoidal en el eje X e Y.
    Si el número de disparos realizados es menor que 20, el jefe se mueve en una dirección determinada por la dirección 
    actual y la velocidad. Se aplican restricciones para mantener al jefe dentro de los límites de la pantalla. 
    Si alcanza un borde, la dirección se ajusta para rebotar en la dirección opuesta.
    """

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2
        if self.shots_fired < 20:
            dx, dy = self.direction
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                self.speed = 5 / math.sqrt(2)
            else:
                self.speed = 5
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction_x = 1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction_x = -1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.top < 70:
                self.rect.top = 70
                self.direction_y = 1
                if self.direction_x == 0:
                    self.direction_x = 1
            elif self.rect.bottom > HEIGHT - 5:
                self.rect.bottom = HEIGHT - 5
                self.direction_y = -1
                if self.direction_x == 0:
                    self.direction_x = 1
            """
            Una vez que se han realizado 20 disparos, el jefe aumenta su velocidad y persigue al jugador. 
            La dirección se calcula en función de la posición del jugador.
            """                 
            self.direction = (self.direction_x, self.direction_y)
            self.shoot_timer += 1
            if self.shoot_timer >= 100: #Cada 100 fotogramas, el jefe dispara una bala hacia el jugador. 
                dx = player.rect.centerx - self.rect.centerx
                dy = player.rect.centery - self.rect.centery
                direction = pygame.math.Vector2(dx, dy).normalize() #La dirección de la bala se determina según la posición del jugador.
                bullet = Boss2Bullet(self.rect.centerx, self.rect.bottom, direction)
                enemy_bullets_group.add(bullet)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            if self.speed != 5:
                self.speed = 5 / math.sqrt(2)
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

            self.direction_x = direction.x / abs(direction.x) if direction.x != 0 else 0
            self.direction_y = direction.y / abs(direction.y) if direction.y != 0 else 0
            self.direction = (self.direction_x, self.direction_y)

    """
    En el método __init__(), se inicializan los atributos de la bala, como su imagen, posición, 
    velocidad, dirección de movimiento, y el sonido de disparo."""

class Boss2Bullet(pygame.sprite.Sprite): #Representa una bala disparada por el segundo jefe.

    def __init__(self, x, y, direction):
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss2.png').convert_alpha()
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 8 #Determina la velocidad de la bala.
        self.direction = direction #Indica la dirección y sentido de movimiento de la bala.
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    """
    Se calcula el ángulo de rotación necesario para orientar la imagen de la bala en la dirección de movimiento.
    Se rota la imagen original de la bala según el ángulo calculado y se actualiza el rectángulo de colisión.
    Si la bala sale de la pantalla por la parte superior, se elimina.
    """

    def update(self): #Se actualiza la posición de la bala en función de su dirección y velocidad.
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        angle = math.atan2(self.direction.y, self.direction.x)
        angle = math.degrees(angle)

        self.image = pygame.transform.rotate(self.image_orig, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.top > HEIGHT:
            self.kill()

class Boss3(pygame.sprite.Sprite): #Representa al tercer jefe en el juego.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        self.direction_x, self.direction_y = self.direction
        self.shoot_timer = 0
        self.shots_fired = 0
        self.teleport_timer = 0
        self.teleport_interval = 160

    """
    En el método update(), se actualiza la posición del jefe para que se mueva de forma sinusoidal en el eje X e Y, de manera similar a los jefes anteriores.
    Si el número de disparos realizados es menor que 20, el jefe se mueve en una dirección determinada por la dirección actual y la velocidad, también de manera similar a los jefes anteriores.
    Se aplican restricciones para mantener al jefe dentro de los límites de la pantalla, al igual que en los jefes anteriores.
    Cada 120 fotogramas, el jefe dispara una bala hacia el jugador. La dirección de la bala se determina según la posición del jugador.
    """

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2
        if self.shots_fired < 20: #Una vez que se han realizado 20 disparos,
            dx, dy = self.direction #el jefe aumenta su velocidad y persigue al jugador,
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                self.speed = 5 / math.sqrt(2)
            else:
                self.speed = 5
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction_x = 1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction_x = -1
                if self.direction_y == 0:
                    self.direction_y = 1
            elif self.rect.top < 70:
                self.rect.top = 70
                self.direction_y = 1
                if self.direction_x == 0:
                    self.direction_x = 1
            elif self.rect.bottom > HEIGHT - 5:
                self.rect.bottom = HEIGHT - 5
                self.direction_y = -1
                if self.direction_x == 0:
                    self.direction_x = 1

            self.direction = (self.direction_x, self.direction_y)
            self.shoot_timer += 1
            if self.shoot_timer >= 120:
                dx = player.rect.centerx - self.rect.centerx
                dy = player.rect.centery - self.rect.centery
                direction = pygame.math.Vector2(dx, dy).normalize()
                bullet = Boss3Bullet(self.rect.centerx, self.rect.bottom, direction)
                enemy_bullets_group.add(bullet)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            if self.speed != 5:
                self.speed = 5 / math.sqrt(2)
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

            self.direction_x = direction.x / abs(direction.x) if direction.x != 0 else 0
            self.direction_y = direction.y / abs(direction.y) if direction.y != 0 else 0
            self.direction = (self.direction_x, self.direction_y)

        """
        Además, se agrega la capacidad de teletransportarse cada cierto intervalo de tiempo. 
        Después de un número determinado de fotogramas (teleport_interval), el jefe cambia su posición a una
        posición aleatoria dentro de los límites establecidos.
        """

        self.teleport_timer += 1
        if self.teleport_timer >= self.teleport_interval:
            self.rect.centerx = random.randint(50, WIDTH - 50)
            self.rect.centery = random.randint(100, HEIGHT - 100)
            self.teleport_timer = 0

class Boss3Bullet(pygame.sprite.Sprite): #Representa una bala disparada por el tercer jefe en el juego.

    def __init__(self, x, y, direction):
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss3.png').convert_alpha()
        self.image = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 15
        self.direction = direction
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        angle = math.atan2(self.direction.y, self.direction.x)
        angle = math.degrees(angle)

        self.image = pygame.transform.rotate(self.image_orig, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.top > HEIGHT:
            self.kill()
