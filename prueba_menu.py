import pygame
pygame.init()

SIZE = (800,600)

position=(0,0)

screen = pygame.display.set_mode(SIZE)

punto1=(0,0)

imagen1 = pygame.image.load('menu.png')
screen.blit(imagen1, punto1)
pygame.display.flip()

clock = pygame.time.Clock()

continuar=True
while continuar:

    for event in pygame.event.get():
       if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuar=False
      

    clock.tick(60)
    
pygame.quit()
