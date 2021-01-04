"""TODO: add description here."""

import pygame

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line


class Images:
    """TODO: add description here."""
    BACKGROUND = None
    O_CHECKER = None
    X_CHECKER = None

    @staticmethod
    def load():
        """TODO: add description here."""
        Images.BACKGROUND = pygame.image.load('assets/background.png')
        Images.O_CHECKER = pygame.image.load('assets/O.png')
        Images.X_CHECKER = pygame.image.load('assets/X.png')
