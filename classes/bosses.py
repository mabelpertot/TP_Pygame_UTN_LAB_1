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
        self.image = image #Asigna la imagen del jefe al atributo image de la instancia.
        self.rect = self.image.get_rect(center=(x, y)) #Crea un rectángulo del tamaño de la imagen del jefe y lo posiciona en el punto (x, y). El rectángulo se guarda en el atributo rect de la instancia.
        self.speed = 6 # Establece la velocidad del jefe en 6. Esto determina qué tan rápido se mueve el jefe en el juego.
        self.direction = random.choice([(-1, 0), (1, 0)]) #Elige aleatoriamente una dirección de movimiento para el jefe. Puede ser hacia la izquierda ((-1, 0)) o hacia la derecha ((1, 0)).
        self.shoot_timer = 0 #Inicializa el temporizador de disparo del jefe en 0. Este temporizador se utiliza para controlar la frecuencia de los disparos del jefe.
        self.shots_fired = 0 #Inicializa la cantidad de disparos realizados por el jefe en 0. Este atributo se utiliza para llevar un registro de cuántos disparos ha realizado el jefe.

    def update(self, enemy_bullets_group, player): #El método actualiza el estado de la bala del jefe. Toma dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        Este método actualiza el estado de la bala del jefe en el juego. 
        La bala se mueve de forma oscilatoria y cambia su comportamiento después de haber realizado 10 disparos. 
        Puede seguir al jugador y disparar nuevas balas en intervalos regulares. 
        """
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 3 #Mueve la posición horizontal de la bala utilizando una función sinusoidal en función del tiempo actual para crear un movimiento oscilatorio.
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 3 #Mueve la posición vertical de la bala utilizando una función sinusoidal en función del tiempo actual para crear un movimiento oscilatorio.
        if self.shots_fired < 10: #Verifica si la cantidad de disparos realizados por la bala es menor a 10.
            dx, dy = self.direction #Asigna las componentes de dirección horizontal y vertical de la bala a las variables dx y dy.
            self.rect.x += dx * self.speed #Mueve la posición horizontal de la bala en función de su dirección y velocidad.
            self.rect.y = max(self.rect.y, 50) #Limita la posición vertical mínima de la bala a 50 para evitar que se mueva por encima de esa línea.

            if self.rect.left < 5: #Verifica si el borde izquierdo de la bala está fuera de los límites izquierdos de la pantalla.
                self.rect.left = 5 #Ajusta el borde izquierdo de la bala al límite izquierdo de la pantalla.
                self.direction = (1, 0) #Cambia la dirección de la bala a la derecha.
            elif self.rect.right > WIDTH - 5: #Verifica si el borde derecho de la bala está fuera de los límites derechos de la pantalla.
                self.rect.right = WIDTH - 5 #Ajusta el borde derecho de la bala al límite derecho de la pantalla.
                self.direction = (-1, 0) #Cambia la dirección de la bala a la izquierda.

            self.shoot_timer += 1 #Incrementa el temporizador de disparo en 1.
            if self.shoot_timer >= 60: #Verifica si el temporizador de disparo ha alcanzado el valor 60.
                bullet1 = Boss1Bullet(self.rect.centerx - 20, self.rect.bottom) #Crea una instancia de la clase Boss1Bullet con una posición relativa a la bala del segundo jefe.
                bullet2 = Boss1Bullet(self.rect.centerx + 20, self.rect.bottom) #Crea otra instancia de la clase Boss1Bullet con una posición relativa a la bala del segundo jefe.
                bullet3 = Boss1Bullet(self.rect.centerx, self.rect.bottom) #Crea una tercera instancia de la clase Boss1Bullet con una posición relativa a la bala del segundo jefe.
                enemy_bullets_group.add(bullet1, bullet2, bullet3) #Agrega las instancias de las balas creadas al grupo de balas enemigas.
                self.shoot_timer = 0 #Reinicia el temporizador de disparo a cero.
                self.shots_fired += 1 #Incrementa la cantidad de disparos realizados por la bala en uno.
        else: #Si se han realizado 10 disparos o más, se ejecuta este bloque de código.
            self.speed = 10 #Establece la velocidad de la bala a 10.
            dx = player.rect.centerx - self.rect.centerx #Calcula la diferencia horizontal entre la posición del jugador y la posición de la bala.
            dy = player.rect.centery - self.rect.centery #Calcula la diferencia vertical entre la posición del jugador y la posición de la bala.
            direction = pygame.math.Vector2(dx, dy).normalize() #Crea un vector a partir de las diferencias dx y dy y lo normaliza, lo que significa que se convierte en un vector de longitud 1 pero con la misma dirección.

            self.rect.x += direction.x * self.speed #Mueve la posición horizontal de la bala en función de la dirección horizontal normalizada y la velocidad.
            self.rect.y += direction.y * self.speed #Mueve la posición vertical de la bala en función de la dirección vertical normalizada y la velocidad.

class Boss1Bullet(pygame.sprite.Sprite): #Representa las balas disparadas por el jefe.
    """
    La clase representa las balas disparadas por el jefe en el juego y tiene
    atributos que controlan su imagen, posición, velocidad y sonido de disparo.
    """
    def __init__(self, x, y): #Recibe dos parámetros: x (posición horizontal inicial) y y (posición vertical inicial).
        super().__init__()
        self.image = pygame.image.load('images/bullets/bulletboss1.png').convert_alpha() #Carga la imagen de la bala del jefe y la asigna al atributo image de la instancia. convert_alpha() se utiliza para optimizar la imagen y habilitar la transparencia.
        self.rect = self.image.get_rect() #Crea un rectángulo del tamaño de la imagen de la bala y lo guarda en el atributo rect de la instancia.
        self.rect.centerx = x #Establece la posición horizontal del centro del rectángulo de la bala en x.
        self.rect.bottom = y + 10 #Establece la posición vertical inferior del rectángulo de la bala en y + 10. Esto ajusta la posición vertical de la bala para que no esté justo en la posición del jefe.
        self.speed = 8 # Establece la velocidad de la bala en 8. Esto determina qué tan rápido se mueve la bala en el juego.
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss1shoot.mp3') #Carga el sonido de disparo de la bala del jefe y lo asigna al atributo shoot_sound de la instancia.
        self.shoot_sound.set_volume(0.4) #Establece el volumen del sonido de disparo de la bala en 0.4.
        self.shoot_sound.play() #Reproduce el sonido de disparo de la bala.

    def update(self): #Actualiza la posición y la orientación de una bala disparada por el jefe en el juego.
        """
        Este método se utiliza para actualizar la posición de la bala en cada fotograma y verificar si ha salido de la pantalla. 
        Si la bala ha salido de la pantalla, se elimina del juego.
        """
        self.rect.move_ip(0, self.speed)
        #Mueve el rectángulo de la bala verticalmente según la velocidad especificada. El método move_ip() actualiza la posición del rectángulo in-place.
        if self.rect.top > HEIGHT: #Verifica si la parte superior del rectángulo de la bala ha pasado la altura de la pantalla (HEIGHT). Esto comprueba si la bala ha salido de la pantalla por la parte inferior.
            self.kill() #Si la bala ha salido de la pantalla, se llama al método kill(). Esto elimina la instancia de la bala del grupo de sprites al que pertenece. La bala se elimina del juego.

class Boss2(pygame.sprite.Sprite): #Representa al segundo jefe en el juego.
    """
    La clase representa al segundo jefe en el juego y contiene atributos para su imagen, 
    posición, velocidad, dirección de movimiento, temporizador de disparo y contador de disparos.
    """
    def __init__(self, x, y, image): #Recibe tres parámetros: x (posición horizontal inicial), y (posición vertical inicial) e image (imagen del  segundo jefe).
        super().__init__()
        self.image = image #Asigna la imagen del jefe al atributo image.
        self.rect = self.image.get_rect(center=(x, y)) #Obtiene el rectángulo que rodea al jefe y lo posiciona en el centro especificado por las coordenadas (x, y). El rectángulo se utiliza para gestionar la posición y colisiones del jefe.
        self.speed = 5 # Establece la velocidad del jefe.
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        #Elige aleatoriamente una dirección de movimiento para el jefe. Las direcciones posibles son izquierda, derecha, arriba, abajo, diagonal izquierda-arriba, diagonal derecha-arriba, diagonal izquierda-abajo y diagonal derecha-abajo.
        self.direction_x, self.direction_y = self.direction
        # Asigna las componentes X e Y de la dirección a los atributos direction_x y direction_y respectivamente. Esto permite acceder de forma separada a las componentes de la dirección del movimiento del jefe.
        self.shoot_timer = 0 # Inicializa el temporizador de disparo del jefe a cero.
        self.shots_fired = 0 #Inicializa el contador de disparos realizados por el jefe a cero.

    def update(self, enemy_bullets_group, player): #El método actualiza el estado de la bala del segundo jefe. Toma dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        El método update actualiza la posición del jefe para lograr un movimiento sinusoidal en los ejes X e Y. 
        Aplica restricciones para mantener al jefe dentro de los límites de la pantalla y ajusta la dirección 
        del movimiento si el jefe alcanza un borde.
        """
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2 #Actualiza la posición X del jefe utilizando una función sinusoidal con respecto al tiempo. Esto crea un movimiento sinusoidal en el eje X.
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2 #Actualiza la posición Y del jefe utilizando una función sinusoidal con respecto al tiempo. Esto crea un movimiento sinusoidal en el eje Y.
        if self.shots_fired < 20: #Verifica si el número de disparos realizados por el jefe es menor que 20.
            dx, dy = self.direction #Asigna las componentes X e Y de la dirección del movimiento del jefe a las variables dx y dy respectivamente.
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]: #Verifica si la dirección del jefe es una de las direcciones diagonales.
                self.speed = 5 / math.sqrt(2)
                #Establece la velocidad del jefe en un valor menor para el movimiento diagonal. Se utiliza la fórmula 5 / sqrt(2) para mantener una velocidad constante en todas las direcciones.
            else: #Si la dirección del jefe no es diagonal.
                self.speed = 5 #Establece la velocidad del jefe en 5 para el movimiento en direcciones horizontales y verticales.
            self.rect.x += dx * self.speed #Actualiza la posición X del jefe multiplicando la dirección X por la velocidad.
            self.rect.y += dy * self.speed #Actualiza la posición Y del jefe multiplicando la dirección Y por la velocidad.
            #Restricciones de los límites de la pantalla:
            if self.rect.left < 5: #Si el jefe alcanza el borde izquierdo de la pantalla.
                self.rect.left = 5 #Establece la posición del jefe en el borde izquierdo.
                self.direction_x = 1 #Invierte la dirección en el eje X para rebotar en la dirección opuesta.
                if self.direction_y == 0: #Si la dirección en el eje Y es cero (movimiento horizontal).
                    self.direction_y = 1 # Establece la dirección en el eje Y como 1 (movimiento hacia abajo).
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
            self.direction = (self.direction_x, self.direction_y) #Actualiza la dirección del movimiento del jefe con las componentes X e Y actualizadas.
            self.shoot_timer += 1 #Incrementa el temporizador de disparo en 1.
            if self.shoot_timer >= 100: 
                #Verifica si el temporizador de disparo ha alcanzado o superado el valor de 100. Esto significa que ha pasado un cierto número de fotogramas y es hora de que el jefe dispare.
                dx = player.rect.centerx - self.rect.centerx #Calcula la diferencia en la posición X entre el centro del jugador y el centro del jefe.
                dy = player.rect.centery - self.rect.centery #Calcula la diferencia en la posición Y entre el centro del jugador y el centro del jefe.
                direction = pygame.math.Vector2(dx, dy).normalize() 
                #Crea un vector a partir de las diferencias calculadas y lo normaliza para obtener una dirección unitaria. Esta dirección determinará la trayectoria de la bala disparada hacia el jugador.
                bullet = Boss2Bullet(self.rect.centerx, self.rect.bottom, direction)
                #Crea una instancia de la clase Boss2Bullet, pasando la posición inicial de la bala (centro del jefe en el eje X y parte inferior del jefe en el eje Y) y la dirección de la bala.
                enemy_bullets_group.add(bullet) #Agrega la bala al grupo de balas del enemigo.
                self.shoot_timer = 0 #Reinicia el temporizador de disparo a cero.
                self.shots_fired += 1 #Incrementa el contador de disparos realizados por el jefe.
        else:
            if self.speed != 5: #Verifica si la velocidad del jefe no es igual a 5. Si es así, significa que el jefe está en un estado especial y la velocidad se ajusta.
                self.speed = 5 / math.sqrt(2) #Establece la velocidad del jefe en un valor menor para el movimiento diagonal.
            dx = player.rect.centerx - self.rect.centerx #Calcula la diferencia en la posición X entre el centro del jugador y el centro del jefe.
            dy = player.rect.centery - self.rect.centery #Calcula la diferencia en la posición Y entre el centro del jugador y el centro del jefe.
            direction = pygame.math.Vector2(dx, dy).normalize() #Crea un vector a partir de las diferencias calculadas y lo normaliza para obtener una dirección unitaria.

            self.rect.x += direction.x * self.speed #Actualiza la posición X del jefe multiplicando la dirección X por la velocidad.
            self.rect.y += direction.y * self.speed #Actualiza la posición Y del jefe multiplicando la dirección Y por la velocidad.

            self.direction_x = direction.x / abs(direction.x) if direction.x != 0 else 0 #Calcula la dirección en el eje X normalizando la dirección X anteriormente calculada.
            self.direction_y = direction.y / abs(direction.y) if direction.y != 0 else 0 #Calcula la dirección en el eje Y normalizando la dirección Y anteriormente calculada.
            self.direction = (self.direction_x, self.direction_y) #Actualiza la dirección del movimiento del jefe con las componentes X e Y actualizadas.

class Boss2Bullet(pygame.sprite.Sprite): #Representa una bala disparada por el segundo jefe.
    """
    La clase representa una bala disparada por el segundo jefe. Al crear un objeto Boss2Bullet, se carga una imagen de bala, 
    se establecen sus atributos iniciales como posición, velocidad y dirección, y se reproduce un sonido de disparo.
    """
    def __init__(self, x, y, direction): #Recibe tres parámetros: x, y (posición inicial de la bala) y direction (la dirección del movimiento de la bala).
        super().__init__()
        self.image_orig = pygame.image.load('images/bullets/bulletboss2.png').convert_alpha()
        # Carga la imagen de la bala del segundo jefe y la almacena en self.image_orig. convert_alpha() se utiliza para asegurar la compatibilidad con transparencias.
        self.image = self.image_orig #Asigna la imagen original de la bala a self.image.
        self.rect = self.image.get_rect() #Obtiene el rectángulo de colisión de la imagen de la bala y lo asigna a self.rect.
        self.rect.centerx = x #Establece la coordenada x del centro del rectángulo de colisión de la bala.
        self.rect.bottom = y + 10 #Establece la coordenada y del borde inferior del rectángulo de colisión de la bala.
        self.speed = 8 #Establece la velocidad de la bala en 8 unidades por fotograma.
        self.direction = direction #Asigna la dirección y sentido de movimiento de la bala.
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3') #Carga el sonido de disparo de la bala del segundo jefe.
        self.shoot_sound.set_volume(0.4) #Establece el volumen del sonido de disparo.
        self.shoot_sound.play()

    def update(self): #Actualiza la posición y la orientación de una bala disparada por el segundo jefe en el juego.
        """ 
        La bala se mueve en la dirección determinada por su atributo direction y velocidad speed. Además, 
        se calcula el ángulo de rotación necesario para orientar la imagen de la bala en la dirección de movimiento. 
        Si la bala sale de la pantalla por la parte superior, se elimina.""" 
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)
        #Actualiza la posición de la bala en función de su dirección y velocidad. Mueve el rectángulo de colisión de la bala en la cantidad determinada por la dirección en los ejes X e Y multiplicada por la velocidad.
        angle = math.atan2(self.direction.y, self.direction.x) #Calcula el ángulo en radianes entre la dirección Y y la dirección X de la bala utilizando la función atan2() de la biblioteca math.
        angle = math.degrees(angle) #Convierte el ángulo calculado de radianes a grados.

        self.image = pygame.transform.rotate(self.image_orig, -angle) # Rota la imagen original de la bala utilizando el ángulo calculado. La rotación se realiza en sentido contrario a las agujas del reloj (-angle) para que la imagen apunte en la dirección del movimiento de la bala.
        self.rect = self.image.get_rect(center=self.rect.center) #Actualiza el rectángulo de colisión de la bala para que coincida con la nueva posición y orientación de la imagen.

        if self.rect.top > HEIGHT: #Verifica si la parte superior del rectángulo de la bala ha salido de la pantalla (supera la altura de la pantalla). Si es así, significa que la bala ha salido de la pantalla y se debe eliminar.
            self.kill() #Elimina la bala del grupo de sprites al llamar al método kill()

class Boss3(pygame.sprite.Sprite): #Representa al tercer jefe en el juego.
    """
    La clase representan las propiedades del tercer jefe en el juego, como su posición, velocidad, 
    dirección de movimiento, temporizadores y contador de disparos.
    """
    def __init__(self, x, y, image): #Recibe tres parámetros: x, y que representan la posición inicial del jefe, y image que es la imagen del jefe.
        super().__init__()
        self.image = image #Asigna la imagen del jefe al atributo image de la instancia.
        self.rect = self.image.get_rect(center=(x, y)) #Obtiene el rectángulo que delimita el jefe a partir de la imagen, y lo posiciona en el centro especificado por las coordenadas x e y.
        self.speed = 5 #Establece la velocidad del jefe en 5.
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)])
        #Elige aleatoriamente una dirección de movimiento para el jefe a partir de una lista de opciones. La dirección es una tupla de dos valores que representan los componentes horizontal y vertical del movimiento.
        self.direction_x, self.direction_y = self.direction 
        self.shoot_timer = 0 #Inicializa el temporizador de disparo del jefe en 0.
        self.shots_fired = 0 #Inicializa el contador de disparos realizados por el jefe en 0.
        self.teleport_timer = 0 #Inicializa el temporizador de teletransporte del jefe en 0.
        self.teleport_interval = 160 #Establece el intervalo de tiempo entre los teletransportes del jefe en 160.

    def update(self, enemy_bullets_group, player): #Actualiza el estado de la instancia del jefe. Recibe dos argumentos: enemy_bullets_group, que representa el grupo de balas enemigas, y player, que representa al jugador.
        """
        El método actualiza el estado del tercer jefe en el juego. El jefe se mueve de forma oscilante en los ejes x e y, 
        persigue al jugador si se han realizado menos de 20 disparos, y se ajusta a los límites de la pantalla.
        """
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 2 # Mueve la posición del jefe de forma oscilante en el eje x utilizando una función sinusoidal.
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 2 #Mueve la posición del jefe de forma oscilante en el eje y utilizando una función sinusoidal.
        if self.shots_fired < 20: #Verifica si el número de disparos realizados por el jefe es menor que 20.
            dx, dy = self.direction 
            if self.direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]: # Comprueba si la dirección de movimiento del jefe corresponde a las diagonales.
                self.speed = 5 / math.sqrt(2) #Establece la velocidad del jefe a 5 dividido por la raíz cuadrada de 2, lo que resulta en un movimiento más lento en las diagonales.
            else: #Si la dirección de movimiento no es diagonal, es decir, horizontal o vertical.
                self.speed = 5 #Establece la velocidad del jefe en 5.
            self.rect.x += dx * self.speed #Mueve la posición del jefe en el eje x según la dirección y velocidad.
            self.rect.y += dy * self.speed #Mueve la posición del jefe en el eje y según la dirección y velocidad.
            #Verifican si el jefe alcanza los límites de la pantalla en los bordes izquierdo, derecho, superior e inferior, y ajustan su posición y dirección de movimiento en consecuencia.
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
        self.image_orig = pygame.image.load('images/bullets/bulletboss3.png').convert_alpha() # carga la imagen de la bala del tercer jefe desde un archivo y la almacena en self.image_orig. convert_alpha() se utiliza para optimizar la imagen para su uso en el juego.
        self.image = self.image_orig #Establece self.image como la imagen original de la bala.
        self.rect = self.image.get_rect() #crea un rectángulo del tamaño de la imagen de la bala y lo asigna a self.rect. El rectángulo se utiliza para controlar la posición y colisiones de la bala.
        self.rect.centerx = x #Establece la coordenada x del centro del rectángulo de la bala.
        self.rect.bottom = y + 10 #Establece la coordenada y del borde inferior del rectángulo de la bala.
        self.speed = 15 #Establece la coordenada y del borde inferior del rectángulo de la bala.
        self.direction = direction #Almacena la dirección en la que se moverá la bala.
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/boss2shoot.mp3') #Carga un sonido de disparo desde un archivo y lo asigna a self.shoot_sound. El sonido se reproduce cuando se crea la bala.
        self.shoot_sound.set_volume(0.4) #Establece el volumen del sonido de disparo a 0.4.
        self.shoot_sound.play() #Reproduce el sonido de disparo.

    def update(self): #Actualiza el estado de la bala en cada fotograma.
        """
        Este método actualiza la posición y rotación de la bala en función de su dirección y velocidad. 
        Además, comprueba si la bala ha salido de la pantalla y la elimina en ese caso.
        """
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)
        #Mueve la posición del rectángulo de la bala en función de su dirección y velocidad. move_ip() actualiza la posición del rectángulo in-place.
        angle = math.atan2(self.direction.y, self.direction.x) #Calcula el ángulo en radianes entre la dirección vertical y horizontal de la bala utilizando la función atan2().
        angle = math.degrees(angle) #Convierte el ángulo de radianes a grados.

        self.image = pygame.transform.rotate(self.image_orig, -angle) #Rota la imagen original de la bala por el ángulo calculado y la asigna a self.image. Esto gira visualmente la imagen de la bala en la dirección correcta.
        self.rect = self.image.get_rect(center=self.rect.center) #Actualiza el rectángulo de la bala para que se ajuste a la nueva imagen rotada. El centro del rectángulo se mantiene en la misma posición.

        if self.rect.top > HEIGHT: #Verifica si la parte superior del rectángulo de la bala ha pasado la altura de la pantalla.
            self.kill() #mElimina la instancia de la bala del grupo de sprites y la elimina del juego.
