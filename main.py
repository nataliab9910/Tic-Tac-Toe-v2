"""TODO: add description here."""

import pygame
import controller


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

class Main:
    """TODO: add description here."""
    # pylint: disable=R0903
    # TODO: delete this line
    def __init__(self):
        self.controller = controller.GameController()

    def main_loop(self):
        """TODO: add description here."""
        pygame.init()
        pygame.font.init()
        self.controller.game_loop()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
