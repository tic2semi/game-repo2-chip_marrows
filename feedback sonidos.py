import pygame 
pygame.init
while True:
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_j]:
        sonido.play("Feedback sonidos codigo/sonidos/desplazamiento puño1.wav")

