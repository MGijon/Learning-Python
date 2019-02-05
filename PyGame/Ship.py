import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Ship(pygame.sprite.Sprite):

    color = GREEN
    width = 10
    height = 10
    position = (0, 0)
    life = 10

    def __init__(self, screen):

        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw a rectangle
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #self.screen = screen

    @property
    def position(self):
        ''' funciona como un getter '''
        return self.position;

    @position.setter
    def position(self, newPosition):
        self.position = newPosition;

    @property
    def life(self):
        ''' funciona como un getter '''
        return self.life;

    @life.setter
    def life(self, newLife):
        self.life = newLife;

#    def draw(self, x, y):
#        pygame.draw.rect(self.screen, self.color, [y + 55, x + 200, x + 100, y + 70],0)


    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels


#El soñador de providence
