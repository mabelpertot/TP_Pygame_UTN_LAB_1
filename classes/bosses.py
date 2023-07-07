import pygame
import random
import math

from .constants import WIDTH, HEIGHT

class Boss1(pygame.sprite.Sprite): #Representa al jefe en el juego.
    """
    La clase representa a un jefe en el juego y tiene atributos que controlan su imagen, 
    posición, velocidad, dirección, temporizador de disparo y cantidad de disparos realizadosL
    """
    def __init__(self, x, y, image): # Recibe tres parámetros: x (posición horizontal inicial), y (posición vertical inicial) e image (imagen del jefe).
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))         
        self.speed = 6 
        self.direction = random.choice([(-1, 0), (1, 0)]) 
        self.shoot_timer = 0 
        self.shots_fired = 0 

    def update(self, enemy_bullets_group, player): #El método actualiza el estado de la bala del jefe. Toma dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        Este método actualiza el estado de la bala del jefe en el juego. 
        La bala se mueve de forma oscilatoria y cambia su comportamiento después de haber realizado 10 disparos. 
        Puede seguir al jugador y disparar nuevas balas en intervalos regulares. 
        """
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
    """
    La clase representa las balas disparadas por el jefe en el juego y tiene
    atributos que controlan su imagen, posición, velocidad y sonido de disparo.
    """
    def __init__(self, x, y): #Recibe dos parámetros: x (posición horizontal inicial) y y (posición vertical inicial).
        super().__init__()
        self.image = pygame.image.load('images/bullets/bulletboss1.png').convert_alpha() 
        self.rect = self.image.get_rect() 
        self.rect.centerx = x 
        self.rect.bottom = y + 10 
        self.speed = 8 
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss1shoot.mp3') 
        self.shoot_sound.set_volume(0.4) 
        self.shoot_sound.play() 

    def update(self): #Actualiza la posición y la orientación de una bala disparada por el jefe en el juego.
        """
        Este método se utiliza para actualizar la posición de la bala en cada fotograma y verificar si ha salido de la pantalla. 
        Si la bala ha salido de la pantalla, se elimina del juego.
        """
        self.rect.move_ip(0, self.speed)        
        if self.rect.top > HEIGHT: 
            self.kill() 

class Boss2(pygame.sprite.Sprite): #Representa al segundo jefe en el juego.
    """
    La clase representa al segundo jefe en el juego y contiene atributos para su imagen, 
    posición, velocidad, dirección de movimiento, temporizador de disparo y contador de disparos.
    """
    def __init__(self, x, y, image): #Recibe tres parámetros: x (posición horizontal inicial), y (posición vertical inicial) e image (imagen del  segundo jefe).
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect(center=(x, y)) 
        self.speed = 5 
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])       
        self.direction_x, self.direction_y = self.direction 
        self.shoot_timer = 0
        self.shots_fired = 0 

    def update(self, enemy_bullets_group, player): #El método actualiza el estado de la bala del segundo jefe. Toma dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        El método update actualiza la posición del jefe para lograr un movimiento sinusoidal en los ejes X e Y. 
        Aplica restricciones para mantener al jefe dentro de los límites de la pantalla y ajusta la dirección 
        del movimiento si el jefe alcanza un borde.
        """
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

            #Restricciones de los límites de la pantalla:
            if self.rect.left < 5: 
                self.rect.left = 5 
                self.direction_x = 1 
                if self.direction_y == 0: 
                    self.direction_y = 1 
                    
            #Propósito similar para los bordes derecho, superior e inferior de la pantalla.
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
            Actualiza el comportamiento del segundo jefe en el juego. Si el número de disparos realizados es 
            menor que 20, el jefe se mueve hacia el jugador y dispara una bala cada 100 fotogramas. Si el número 
            de disparos alcanza 20, el jefe persigue al jugador y dispara balas en su dirección. 
            """
            self.direction = (self.direction_x, self.direction_y) 
            self.shoot_timer += 1 
            if self.shoot_timer >= 100: 
               
                dx = player.rect.centerx - self.rect.centerx 
                dy = player.rect.centery - self.rect.centery 
                direction = pygame.math.Vector2(dx, dy).normalize() 
                
                bullet = Boss2Bullet(self.rect.centerx, self.rect.bottom, direction)
                
                enemy_bullets_group.add(bullet) 
                self.shoot_timer = 0 
                self.shots_fired += 1 

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

class Boss2Bullet(pygame.sprite.Sprite): #Representa una bala disparada por el segundo jefe.
    """
    La clase representa una bala disparada por el segundo jefe. Al crear un objeto Boss2Bullet, se carga una imagen de bala, 
    se establecen sus atributos iniciales como posición, velocidad y dirección, y se reproduce un sonido de disparo.
    """
    def __init__(self, x, y, direction): #Recibe tres parámetros: x, y (posición inicial de la bala) y direction (la dirección del movimiento de la bala).
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss2.png').convert_alpha()
        self.image = self.image_orig 
        self.rect = self.image.get_rect()
        self.rect.centerx = x 
        self.rect.bottom = y + 10 
        self.speed = 8 
        self.direction = direction 
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3') 
        self.shoot_sound.set_volume(0.4) 
        self.shoot_sound.play()

    def update(self): #Actualiza la posición y la orientación de una bala disparada por el segundo jefe en el juego.
        """ 
        La bala se mueve en la dirección determinada por su atributo direction y velocidad speed. Además, 
        se calcula el ángulo de rotación necesario para orientar la imagen de la bala en la dirección de movimiento. 
        Si la bala sale de la pantalla por la parte superior, se elimina.""" 
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        angle = math.atan2(self.direction.y, self.direction.x) 
        angle = math.degrees(angle) 

        self.image = pygame.transform.rotate(self.image_orig, -angle) 
        self.rect = self.image.get_rect(center=self.rect.center) 

        if self.rect.top > HEIGHT: 
            self.kill() 

class Boss3(pygame.sprite.Sprite): #Representa al tercer jefe en el juego.
    """
    La clase representan las propiedades del tercer jefe en el juego, como su posición, velocidad, 
    dirección de movimiento, temporizadores y contador de disparos.
    """
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

    def update(self, enemy_bullets_group, player): #Actualiza el estado de la instancia del jefe. Recibe dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        El método actualiza el estado del tercer jefe en el juego. El jefe se mueve de forma oscilante en los ejes x e y, 
        persigue al jugador si se han realizado menos de 20 disparos, y se ajusta a los límites de la pantalla.
        """
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
    """
    Esta clase representa una bala disparada por el tercer jefe en el juego. Al inicializarse, 
    carga la imagen de la bala, establece su posición y velocidad, reproduce un sonido de disparo y 
    actualiza su estado en cada fotograma moviéndose en una dirección y rotando visualmente la imagen de la bala. 
    Si la bala sale de la pantalla, se elimina del juego.
    """
    def __init__(self, x, y, direction): #Recibe tres parámetros: las coordenadas x e y donde se creará la bala y la dirección en la que se moverá.
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

    def update(self): #Actualiza el estado de la bala en cada fotograma.
        """
        Este método actualiza la posición y rotación de la bala en función de su dirección y velocidad. 
        Además, comprueba si la bala ha salido de la pantalla y la elimina en ese caso.
        """
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)
        angle = math.atan2(self.direction.y, self.direction.x) 
        angle = math.degrees(angle) 

        self.image = pygame.transform.rotate(self.image_orig, -angle) 
        self.rect = self.image.get_rect(center=self.rect.center) 

        if self.rect.top > HEIGHT: 
            self.kill() 
