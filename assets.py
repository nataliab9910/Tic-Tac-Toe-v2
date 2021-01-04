import pygame


class Assets:

    BACKGROUND_IMAGE = None
    O_IMAGE = None
    X_IMAGE = None

    @staticmethod
    def load():
        Assets.BACKGROUND_IMAGE = pygame.image.load('assets/background.png')
        Assets.O_IMAGE = pygame.image.load('assets/O.png')
        Assets.X_IMAGE = pygame.image.load('assets/X.png')
