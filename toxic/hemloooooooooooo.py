import pygame
pygame.init()
screen = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()
sq = pygame.Rect(150,25,5,5)
cpos = pygame.Vector2(150,150)
cspd = pygame.Vector2()
crad = 3
cacc = 0.001 
cspdmul = 0.99
bounce = 1.0
while True:
    if pygame.event.get(pygame.QUIT): break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        sq.move_ip(0,-5)
    if keys[pygame.K_DOWN]:
        sq.move_ip(0,5)
    if keys[pygame.K_LEFT]:
        sq.move_ip(-5,0)
    if keys[pygame.K_RIGHT]:
        sq.move_ip(5,0)
    cspd *=cspdmul
    if cpos[0]<crad:
        cpos.update(crad,cpos[1])
        cspd.update(-cspd[0]*bounce,cspd[1])
    cpos = cpos +cspd
    pygame.draw.circle(screen , "blue" , cpos ,crad)
    pygame.draw.rect(screen,"red", sq)
    pygame.display.flip()
    clock.tick(60)
pygame.quit
