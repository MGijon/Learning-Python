import pygame
from Ship import Ship

pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

SCREENWIDTH=400
SCREENHEIGHT=500


size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Spaca Invaders")

carryOn = True
clock = pygame.time.Clock()

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

ship = Ship(screen)

ship.rect.x = 200
ship.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(ship)


while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                 carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        ship.moveRight(5)

     # --- Game logic should go here

     # --- Drawing code should go here
     # First, clear the screen to white
#    screen.fill(WHITE)

    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)
    #Refresh Screen
    pygame.display.flip()

#    i = 1
#    ship.draw(x = i, y = 1)

     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

     # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()






# https://www.101computing.net/creating-sprites-using-pygame/
