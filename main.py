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
#Iniciación de variables
key_luch1 = "neutral"
key_luch2 = "neutral"
t_atack = -5
t_atack2 = -5
imagen1 = pygame.image.load('assets/img fondo.png')
punto1 = (0,0)
#Definimos un diccionario para los estados del luchador(por ahora ataque y neutro)
img_luch1 = {"neutral" : pygame.image.load('assets/personajes/Luchador1/neutro1.png'),
                
                "atack" : pygame.image.load("assets/personajes/Luchador1/variante_puño_opt-2.jpeg")}


img_luch2 = {"neutral" : pygame.image.load('assets/personajes/Luchador 2/neutro2.png'),
                "atack": pygame.image.load("assets/personajes/Luchador 2/variante puño_opt.jpeg")}
def BackgroundGameplay():
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth)
    screen.blit(imagen1, punto1)
    
def UI(screen,green): 
    punto1=(100,50)
    punto2=(200,50)
    punto3=(500,50)
    punto4=(200,50)
    pygame.draw.rect(screen,green, (punto1,punto2))
    pygame.draw.rect(screen,green, (punto3,punto4))
pos_1 = (100,250)
pos_2 = (400,250)
def Fightrs(sprt_luch1, sprt_luch2, pos_1 ,pos_2):
    
    screen.blit(sprt_luch1 , pos_1)
    screen.blit(sprt_luch2, pos_2)  
    

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
def back (imagen1, punto1):
    screen.blit(imagen1, punto1)
    




lineWidth=3


 
#######################################################
#EJECUCION DE FUNCIONES 
BackgroundGameplay()
pygame.mouse.set_visible(3)
hitbox_luch1= img_luch1[key_luch1].get_rect()
hitbox_luch2= img_luch2[key_luch2].get_rect()
continuar=True
while continuar:
                     
    for event in pygame.event.get():
       if event.type==QUIT:
            continuar=False
       
    #Movimiento de puño ambos jugadores
    luch1_swing = pygame.mixer.Sound("assets/Feedback_sonidos codigo/sonidos/desplazamiento puño1.wav")
    luch2_swing = pygame.mixer.Sound("assets/Feedback_sonidos codigo/sonidos/desplazamiento puño 2 .wav")
    luch_hit = pygame.mixer.Sound("assets/Feedback_sonidos codigo/sonidos/Hit1.wav")
    keystate = pygame.key.get_pressed()
    hitbox_luch1.topleft = pos_1
    hitbox_luch2.topleft = pos_2
    if keystate [pygame.K_p]: 
        pos_1 = (200, 250)
    if key_luch1 == "neutral":
        if keystate[pygame.K_j]:
            t_atack = 3
            luch1_swing.play()
            key_luch1 = "atack"
            img_luch1[key_luch1]
    elif key_luch1 == "atack":
        t_atack -= 1
        if hitbox_luch1.colliderect(hitbox_luch2):
                luch_hit.play()
        if t_atack <= 0:
            key_luch1 = "neutral"
            

            pygame.display.flip()
    if key_luch2 == "neutral":
        if keystate[pygame.K_k]:
            t_atack2 = 5
            luch2_swing.play()
            key_luch2 = "atack"
            img_luch2[key_luch2]
    elif key_luch2 == "atack":
        t_atack2 -= 1
        if hitbox_luch2.colliderect(hitbox_luch1):
                luch_hit.play()
        if t_atack2 <= 0:
            key_luch2 ="neutral"
            pygame.display.flip()

           
    screen.fill(black)
    back (imagen1, punto1)
    UI(screen,green)
    Fightrs(img_luch1[key_luch1] , img_luch2[key_luch2], pos_1 , pos_2)  
   #Atualizando fotogramas
     
    pygame.display.flip()

              
    #Control de estados (para que el puño no sea infinito)
    
    
   
    

clock.tick(60)
    
pygame.quit()
sys.exit();


