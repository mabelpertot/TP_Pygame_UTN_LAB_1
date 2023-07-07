import pygame
import random

class Explosion(pygame.sprite.Sprite): #Representa una animación de explosión en el juego.
    """
    Representa una explosión en el juego y contiene atributos para almacenar imágenes de explosión, 
    gestionar el cambio de imagen, reproducir sonidos de explosión y controlar su posición en la pantalla del juego.
    """
    def __init__(self, center, explosion_images): #Recibe dos parámetros: center es un parámetro que representa las coordenadas del centro de la explosión, y explosion_images es una lista que contiene las imágenes de la explosión.
        super().__init__()
        self.explosion_images = explosion_images #Se almacena la lista de imágenes de explosión pasada como argumento en el atributo explosion_images
        self.image = self.explosion_images[0] #La primera imagen de explosión se establece como la imagen actual en el atributo image.
        self.rect = self.image.get_rect() #Se crea un rectángulo a partir de la imagen de explosión y se asigna al atributo rect.
        self.rect.center = center #Se establece la posición del rectángulo en el centro especificado mediante el parámetro center
        self.frame = 0 #Se inicializa el atributo frame con el valor 0, que lleva la cuenta del índice actual de la imagen de explosión.
        self.last_update = pygame.time.get_ticks() #Se guarda el tiempo actual en milisegundos en el atributo last_update, que se utiliza para controlar la velocidad de cambio de imagen.
        self.frame_rate = 60 #La velocidad de cambio de imagen se establece en 60 fotogramas por segundo en el atributo frame_rate.
        self.explosion_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion1.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion2.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        for sound in self.explosion_sounds: #Se selecciona aleatoriamente un sonido de explosión de la lista explosion_sounds y se guarda en el atributo explosion_sound
            sound.set_volume(0.3) #Se establece el volumen de los sonidos de explosión 
        self.explosion_sound = random.choice(self.explosion_sounds)
        self.sound_played = False #Indica que el sonido aún no se ha reproducido.

    def update(self): #Actualiza la animación de la explosión en el juego
        """
        Se encarga de avanzar la animación de la explosión, cambiar la imagen mostrada, actualizar la posición y 
        reproducir el sonido de explosión correspondiente. También se encarga de eliminar la explosión cuando se 
        ha completado la animación.
        """
        now = pygame.time.get_ticks() #Se obtiene el tiempo actual en milisegundos y se guarda en la variable now.
        if now - self.last_update > self.frame_rate: # Se comprueba si ha pasado el tiempo suficiente desde el último cambio de imagen
            self.last_update = now #Se verifica si ha pasado suficiente tiempo desde el último cambio de imagen(now)
            self.frame += 1 #Si ha pasado suficiente tiempo, se actualiza el tiempo del último cambio de imagen y se incrementa en 1 para pasar a la siguiente imagen de explosión.
            if self.frame == len(self.explosion_images): #Se verifica si se ha alcanzado el final de la animación si ambas avriables contienen la misma longitud.
                self.kill() #En ese caso, la explosión se elimina.
            else: #Si no se ha alcanzado el final de la animación
                center = self.rect.center #En el centro original de la explosión se establece la posición del rectángulo.
                self.image = self.explosion_images[self.frame] #Se actualiza la imagen de explosión
                self.rect = self.image.get_rect() #Se crea un nuevo rectángulo a partir de la imagen de explosión actualizada
                self.rect.center = center #Se establece la posición del rectángulo en el centro original de la explosión
                if not self.sound_played: #Se verifica si el sonido de explosión aún no se ha reproducido 
                    self.explosion_sound.play() #se reproduce el sonido y se actualiza.
                    self.sound_played = True #Indica que el sonido ya se ha reproducido.

class Explosion2(pygame.sprite.Sprite): #Representa una segunda animación de explosión en el juego.

    def __init__(self, center, explosion2_images): #Recibe dos parámetros: center representa las coordenadas del centro de la explosión, y explosion2_images es una lista que contiene las imágenes de la segunda animación de explosión. 
        super().__init__()
        self.explosion2_images = explosion2_images #Se almacena la lista de imágenes de la segunda animación de explosión. 
        self.image = self.explosion2_images[0] #La primera imagen de la segunda animación se establece como la imagen actual.
        self.rect = self.image.get_rect() #Se crea un rectángulo a partir de la imagen y se asigna a self.rect.
        self.rect.center = center #La posición del rectángulo se establece en el centro especificado.
        self.frame = 0 #Se inicializa en 0, lleva la cuenta del índice actual de la imagen de la segunda animación.
        self.last_update = pygame.time.get_ticks() #Se guarda el tiempo actual en milisegundos, para controlar la velocidad de cambio de imagen.
        self.frame_rate = 60 #La velocidad de cambio de imagen se establece en 60 fotogramas por segundo.
        self.explosion2_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ] #Se crea una instancia para el sonido de la segunda explosión y se almacena en la lista 
        for sound in self.explosion2_sounds:
            sound.set_volume(0.3) #Se establece el volumen del sonido de la segunda explosión.
        self.explosion2_sound = random.choice(self.explosion2_sounds) #Se selecciona aleatoriamente el sonido de la segunda explosión de la lista y se guarda
        self.sound_played = False #Indica que el sonido aún no se ha reproducido.

    def update(self): #Actualiza la animación de la segunda explosión en el juego.
        """
        Este método se encarga de actualizar la animación de la segunda explosión. 
        Realiza tareas similares al método update() de la clase Explosion
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion2_images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion2_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                if not self.sound_played:
                    self.explosion2_sound.play()
                    self.sound_played = True