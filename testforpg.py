import testforpg

import os
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

testforpg.init()


size = (1200, 700)
screen = testforpg.display.set_mode(size)

testforpg.display.set_caption("My Game")

done = False

clock = testforpg.time.Clock()

bckG = testforpg.image.load

while not done:
    for event in testforpg.event.get():
        if event.type == testforpg.QUIT:
            done = True


    screen.blit(bckG, (0,0))
    # rect0 = pygame.draw.rect(screen, RED, (200,200,400,150))
    testforpg.display.flip()

    clock.tick(60)

testforpg.quit()