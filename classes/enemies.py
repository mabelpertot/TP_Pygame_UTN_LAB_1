import pygame
import random

from .constants import WIDTH, HEIGHT, ENEMY_FORCE

"""
En el método __init__(), se inicializan los atributos del enemigo, como su imagen, posición, 
velocidad y dirección de movimiento.
"""

class Enemy1(pygame.sprite.Sprite): #Representa un enemigo en el juego. 

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image #La imagen del enemigo se establece a partir de un objeto image pasado como argumento.
        self.rect = self.image.get_rect(center=(x, y)) #El rectángulo de colisión se posiciona en el centro de la imagen.
        self.speed = 4
        self.direction = random.choice([(-1, -1), (-1, 1), (1, -1), (1, 1)])
    #Almacena una tupla que representa la dirección y sentido del movimiento del enemigo, seleccionada aleatoriamente
    
    """
    En el método update(), se actualiza la posición del enemigo en función de su dirección y velocidad.
    Se desplaza el rectángulo de colisión en las coordenadas x e y según la dirección y velocidad actuales.
    Se verifican los límites de la pantalla para evitar que el enemigo se salga de ella. Si el enemigo alcanza un 
    límite, se selecciona una nueva dirección aleatoria que permita al enemigo continuar dentro de la pantalla.
    """
    def update(self, enemy_group):
        dx, dy = self.direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        if self.rect.left < 5:
            self.rect.left = 5
            self.direction = random.choice([(1, 0), (0, -1), (0, 1), (1, -1), (1, 1)])
        elif self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5
            self.direction = random.choice([(-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)])

        if self.rect.top < 5:
            self.rect.top = 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)])
        elif self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5
            self.direction = random.choice([(1, 0), (-1, 0), (0, -1), (1, -1), (-1, -1)])

        """
        Se verifica si el enemigo colisiona con otros enemigos en el grupo enemy_group mediante 
        el uso de la función spritecollide().
        """
        collided_with = pygame.sprite.spritecollide(self, enemy_group, False)
        for other_enemy in collided_with:
            if other_enemy != self:
                distance_vec = pygame.math.Vector2(other_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
                distance = distance_vec.length()
                angle = distance_vec.angle_to(pygame.math.Vector2(1, 0))
                """
                Se calcula la distancia entre los centros de los rectángulos de colisión de los enemigos 
                y se obtiene la distancia y el ángulo entre ellos."""
                repel_vec = pygame.math.Vector2(1, 0).rotate(angle)
                repel_vec *= (1 - (distance / (self.rect.width + other_enemy.rect.width)))
                repel_vec *= ENEMY_FORCE
                """
                Se calcula un vector de repulsión proporcional a la distancia entre los enemigos y se 
                escala por una constante de fuerza (ENEMY_FORCE)."""
                self_dir = pygame.math.Vector2(self.direction)
                other_dir = pygame.math.Vector2(other_enemy.direction)

                if distance != 0:
                    new_dir = self_dir.reflect(distance_vec).normalize()
                    other_new_dir = other_dir.reflect(-distance_vec).normalize()

                    self.direction = new_dir.x, new_dir.y
                    other_enemy.direction = other_new_dir.x, other_new_dir.y

                self.rect.move_ip(-repel_vec.x, -repel_vec.y)
                other_enemy.rect.move_ip(repel_vec.x, repel_vec.y)
    """
    este código implementa el comportamiento de un enemigo en el juego. El enemigo se mueve en una dirección 
    aleatoria y se repelerá de otros enemigos en caso de colisión, ajustando sus direcciones de movimiento y 
    separándolos.
    """

"""
En el método __init__(), se inicializan los atributos del enemigo, como su imagen, posición, velocidad, 
dirección de movimiento, temporizador de disparo y contador de disparos.
"""

class Enemy2(pygame.sprite.Sprite): #Representa un tipo de enemigo.

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.direction = random.choice([(-1, 0), (1, 0)])
        self.shoot_timer = 0  #se utiliza como temporizador para controlar el intervalo entre disparos del enemigo.
        self.shots_fired = 0 # lleva la cuenta de la cantidad de disparos realizados por el enemigo.
    
    def update(self, enemy_group, enemy_bullets_group, player):
        if self.shots_fired < 10: #Si el número de disparos realizados (shots_fired) es menor a 10:

            dx, dy = self.direction #El enemigo se desplaza en la dirección establecida por direction 
            self.rect.x += dx * self.speed #A una velocidad determinada por speed.
            self.rect.y = max(self.rect.y, 5)

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction = (1, 0)
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction = (-1, 0)

            collided_with = pygame.sprite.spritecollide(self, enemy_group, False)
            for other_enemy in collided_with:
                if other_enemy != self:
                    distance_vec = pygame.math.Vector2(other_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
                    distance = distance_vec.length()
                    angle = distance_vec.angle_to(pygame.math.Vector2(1, 0))

                    repel_vec = pygame.math.Vector2(1, 0).rotate(angle)
                    repel_vec *= (1 - (distance / (self.rect.width + other_enemy.rect.width)))
                    repel_vec *= ENEMY_FORCE

                    self_dir = pygame.math.Vector2(self.direction)
                    other_dir = pygame.math.Vector2(other_enemy.direction)

                    if distance != 0:
                        new_dir = self_dir.reflect(distance_vec).normalize()
                        other_new_dir = other_dir.reflect(-distance_vec).normalize()

                        self.direction = new_dir.x, new_dir.y
                        other_enemy.direction = other_new_dir.x, other_new_dir.y

                    self.rect.move_ip(-repel_vec.x, -repel_vec.y)
                    other_enemy.rect.move_ip(repel_vec.x, repel_vec.y)

            self.shoot_timer += 1 #Se incrementa el temporizador de disparo (shoot_timer).
            if self.shoot_timer >= 60: #Si el temporizador de disparo alcanza un valor mayor o igual a 60, se crea una instancia de Enemy2Bulleten la posición del enemigo.
                bullet = Enemy2Bullet(self.rect.centerx, self.rect.bottom) #Se crea una instancia de Enemy2Bulleten la posición del enemigo
                enemy_bullets_group.add(bullet) #Se agrega al grupo enemy_bullets_group.
                self.shoot_timer = 0 #Luego se reinicia el temporizador.
                self.shots_fired += 1 #y se incrementa el contador de disparos.
        else:
            self.speed = 10 #Si el número de disparos realizados es igual o mayor a 10. La velocidad del enemigo se incrementa a 10.
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()
            #Se calcula la dirección hacia el jugador (player) y se ajusta la posición del enemigo en función de dicha dirección y la velocidad.
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

"""
En el método __init__(), se inicializan los atributos de la bala, como su imagen, posición, velocidad y 
sonido de disparo.
"""

class Enemy2Bullet(pygame.sprite.Sprite): #Representa una bala disparada por el enemigo.

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet4.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 6
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot2.mp3')
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.kill()
