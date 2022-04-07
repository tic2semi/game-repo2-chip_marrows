#Chip Marrows
import pygame, sys, os
from pygame.locals import *
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.init()
# Color
black=(0, 0, 0)
white=(255, 255, 255)
blue=(0, 0, 255)
green=(0, 255, 0)
def BackgroundGameplay():
    screen.fill(black)
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth)
    screen.blit(imagen1, punto1)
    
def UI(screen,green): 
    punto1=(100,50)
    punto2=(200,50)
    punto3=(500,50)
    punto4=(200,50)
    pygame.draw.rect(screen,green, (punto1,punto2))
    pygame.draw.rect(screen,green, (punto3,punto4))
def Fightrs():
    imagen1 = pygame.image.load('game-repo2-chip_marrows/assets/personajes/Luchador1/neutro1.png')
    luch_1 = (100,250)
    screen.blit(imagen1, luch_1)
    imagen2 = pygame.image.load('game-repo2-chip_marrows/assets/personajes/Luchador 2/neutro2.png')
    luch_2 = (400,250)
    screen.blit(imagen2, luch_2)    
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
pygame.display.set_caption("Chip Marrows")
pygame.display.flip()

imagen1 = pygame.image.load('game-repo2-chip_marrows/assets/img fondo.png')
punto1 = (0,0)
screen.blit(imagen1, punto1)
pygame.display.flip()




# Initial Variables
lineWidth=3


 
#######################################################
#EJECUCION DE FUNCIONES 
BackgroundGameplay()
UI(screen,green)
Fightrs()
pygame.display.flip()
pygame.mouse.set_visible(3)

continuar=True
while continuar:
                     
    for event in pygame.event.get():
       if event.type==QUIT:
            continuar=False
       
#Movimiento de puño a la "J" (solo sonido)
    sonido = pygame.mixer.Sound("game-repo2-chip_marrows/assets/Feedback_sonidos codigo/sonidos/desplazamiento puño1.wav")
    keystate = pygame.key.get_pressed() 
    if keystate[pygame.K_j]:
        sonido.play()
        print("sonido")         

clock.tick(60)
    
pygame.quit()
sys.exit();


