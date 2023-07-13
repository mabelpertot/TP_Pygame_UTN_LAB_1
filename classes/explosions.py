import pygame
import random

class Explosion(pygame.sprite.Sprite): #Representa una animación de explosión en el juego.
    """
    Representa una explosión en el juego y contiene atributos para almacenar imágenes de explosión, 
    gestionar el cambio de imagen, reproducir sonidos de explosión y controlar su posición en la pantalla del juego.
    """
    def __init__(self, center, explosion_images): #Recibe dos parámetros: center es un parámetro que representa las coordenadas del centro de la explosión, y explosion_images es una lista que contiene las imágenes de la explosión.
        super().__init__()
        self.explosion_images = explosion_images
        self.image = self.explosion_images[0] 
        self.rect = self.image.get_rect()
        self.rect.center = center 
        self.frame = 0 
        self.last_update = pygame.time.get_ticks() 
        self.frame_rate = 60
        self.explosion_sounds = [
            pygame.mixer.Sound('game_sounds/explosions/explosion1.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion2.wav'),
            pygame.mixer.Sound('game_sounds/explosions/explosion3.wav')
        ]
        for sound in self.explosion_sounds:
            sound.set_volume(0.3) 
        self.explosion_sound = random.choice(self.explosion_sounds)
        self.sound_played = False

    def update(self): #Actualiza la animación de la explosión en el juego
        """
        Se encarga de avanzar la animación de la explosión, cambiar la imagen mostrada, actualizar la posición y 
        reproducir el sonido de explosión correspondiente. También se encarga de eliminar la explosión cuando se 
        ha completado la animación.
        """
        now = pygame.time.get_ticks() 
        if now - self.last_update > self.frame_rate: 
            self.last_update = now 
            self.frame += 1 
            if self.frame == len(self.explosion_images):
                self.kill() 
            else: 
                center = self.rect.center 
                self.image = self.explosion_images[self.frame] 
                self.rect = self.image.get_rect() 
                self.rect.center = center
                if not self.sound_played: 
                    self.explosion_sound.play() 
                    self.sound_played = True 

class Explosion2(pygame.sprite.Sprite): #Representa una segunda animación de explosión en el juego.

    def __init__(self, center, explosion2_images): #Recibe dos parámetros: center representa las coordenadas del centro de la explosión, y explosion2_images es una lista que contiene las imágenes de la segunda animación de explosión. 
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

    def __init__(self, center, explosion2_images): #Recibe dos parámetros: center representa las coordenadas del centro de la explosión, y explosion2_images es una lista que contiene las imágenes de la segunda animación de explosión. 
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