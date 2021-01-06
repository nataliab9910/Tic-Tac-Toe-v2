"""TODO: add description here."""

import pygame
import constants


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line


class Assets:
    """TODO: add description here."""
    BACKGROUND = None
    O_CHECKER = None
    X_CHECKER = None

    @staticmethod
    def load():
        """TODO: add description here."""
        Assets.BACKGROUND = pygame.image.load('assets/background.png')
        Assets.O_CHECKER = pygame.image.load('assets/O.png')
        Assets.X_CHECKER = pygame.image.load('assets/X.png')


class Window:
    """TODO: add description here."""

    def __init__(self, controller):
        """TODO: add description here."""
        Assets.load()
        pygame.display.set_caption(constants.GAME_TITLE)
        self.surface = pygame.display.set_mode((constants.SURFACE_WIDTH,
                                                constants.BOARD_HEIGHT + constants.TEXT_AREA_HEIGHT))
        self.surface.blit(Assets.BACKGROUND, (0, 0))
        self.clock = pygame.time.Clock()
        self.controller = controller

    def run(self):
        """TODO: add description here."""
        running = True

        print(constants.FIELDS_COORDINATES)
        print(constants.FIELDS_RANGES)

        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    if event.key == pygame.K_r:
                        pass

            self.clock.tick(60)

    def add_checker(self):
        pass
        # check logic return
        # if true put checker and change instruction // should get checker name?
        # evaluate board
        # if false do nothing
