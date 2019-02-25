import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


size = (1200, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

bckG = pygame.image.load

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.blit(bckG, (0,0))
    # rect0 = pygame.draw.rect(screen, RED, (200,200,400,150))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()