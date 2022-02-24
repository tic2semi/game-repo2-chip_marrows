import pygame
pygame.init()
dimensiones= (800, 600)
screen=pygame.display.set_mode(dimensiones)
VERDE= (0, 255, 0)
NEGRO= (0, 0,0)
screen.fill(NEGRO)
punto1=(100,50)
punto2=(200,50)
punto3=(500,50)
punto4=(200,50)

pygame.draw.rect(screen,VERDE, (punto1,punto2))
pygame.draw.rect(screen,VERDE, (punto3,punto4))
pygame.display.flip()

