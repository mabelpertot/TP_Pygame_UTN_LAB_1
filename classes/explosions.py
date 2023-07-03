import pygame
import random

""" 
El constructor de la clase. Toma dos parámetros: center, que representa el centro de la explosión, 
y explosion_images, que es una lista de imágenes de explosión."""
#Estas clases se utilizan para crear efectos de explosión en el juego.
class Explosion(pygame.sprite.Sprite):


    def __init__(self, center, explosion_images):
        super().__init__()
        self.explosion_images = explosion_images #Almacena la lista de imágenes de explosión pasada como argumento.
        self.image = self.explosion_images[0] #Se establece como la primera imagen de explosión en 
        self.rect = self.image.get_rect() #Se crea a partir de la imagen de explosión y 
        self.rect.center = center #se coloca en el centro especificado.
        self.frame = 0 #lleva la cuenta del índice actual de la imagen de explosión.
        self.last_update = pygame.time.get_ticks() #Almacena el tiempo en milisegundos del último cambio de imagen.
        self.frame_rate = 60 # Establece la velocidad de cambio de imagen en 60 fotogramas por segundo.
        self.explosion_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion1.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion2.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        for sound in self.explosion_sounds:
            sound.set_volume(0.3)
        self.explosion_sound = random.choice(self.explosion_sounds)
        self.sound_played = False

    #Es el método de actualización de la explosión. Se llama en cada fotograma para actualizar la animación de la explosión.
    def update(self):
        now = pygame.time.get_ticks() 
        if now - self.last_update > self.frame_rate: # Se comprueba si ha pasado el tiempo suficiente desde el último cambio de imagen
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_images): #Si es así, se actualiza la imagen y se comprueba si se ha alcanzado el final de la animación 
                self.kill() #En ese caso, la explosión se elimina llamando al método kill().
            else:
                center = self.rect.center
                self.image = self.explosion_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                if not self.sound_played:
                    self.explosion_sound.play()
                    self.sound_played = True

    #Esta clase tiene una estructura similar a la clase Explosion, pero se utiliza para otro tipo de explosión.

class Explosion2(pygame.sprite.Sprite):

    def __init__(self, center, explosion2_images):
        super().__init__()
        self.explosion2_images = explosion2_images
        self.image = self.explosion2_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        self.explosion2_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        for sound in self.explosion2_sounds:
            sound.set_volume(0.3)
        self.explosion2_sound = random.choice(self.explosion2_sounds)
        self.sound_played = False

    def update(self):
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

"""
Estas clases se utilizan para animar explosiones en el juego. Cada clase carga imágenes y sonidos de explosión, 
y en cada fotograma actualizan la animación cambiando la imagen y reproduciendo el sonido correspondiente. 
Cuando se alcanza el final de la animación, la explosión se elimina.
"""