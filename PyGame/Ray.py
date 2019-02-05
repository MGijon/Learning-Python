import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Ray(object):

    def __init__(self, arg):
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
