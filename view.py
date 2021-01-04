"""TODO: add description here."""

import pygame
import assets

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line


SURFACE_WIDTH = 454
BOARD_HEIGHT = 454
TEXT_AREA_HEIGHT = 50
GAME_TITLE = 'TIC-TAC-TOE Game!'


class Window:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        pygame.display.set_caption(GAME_TITLE)
        self.surface = pygame.display.set_mode((SURFACE_WIDTH, BOARD_HEIGHT + TEXT_AREA_HEIGHT))
        self.surface.blit(assets.Images.BACKGROUND, (0, 0))
        self.clock = pygame.time.Clock()

    def run(self):
        """TODO: add description here."""
        running = True

        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    if event.key == pygame.K_r:
                        pass

            self.clock.tick(60)
