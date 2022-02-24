#Chip Marrows
import pygame, sys, os
from pygame.locals import *
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.init()
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED']='1'
clock = pygame.time.Clock()
# Resolucion
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

#FONDO
dimensiones=(800,600)
screen=pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Juego")
pygame.display.flip()

imagen1 = pygame.image.load('img fondo.png')
punto1 = (0,0)
screen.blit(imagen1, punto1)
pygame.display.flip()



# Color
black=(0, 0, 0)
white=(255, 255, 255)
blue=(0, 0, 255)

# Initial Variables
lineWidth=3

def BackgroundGameplay():
    screen.fill(black)
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth)
    screen.blit(imagen1, punto1)
    pygame.display.flip()
#######################################################
BackgroundGameplay()
pygame.mouse.set_visible(3)

continuar=True
while continuar:
                     
    for event in pygame.event.get():
       if event.type==QUIT or event.type==pygame.KEYDOWN:
            continuar=False
            
      

    clock.tick(60)
    
pygame.quit()
sys.exit();


