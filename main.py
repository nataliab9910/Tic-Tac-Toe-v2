"""TODO: add description here."""

import pygame
import controller


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

class Main:
    """TODO: add description here."""
    def __init__(self):
        self.controller = controller.Controller()

    def main(self):
        """TODO: add description here."""
        pygame.init()  # move to view?

        self.controller.run()

        # main_window = view.Window()
        # main_window.run()


if __name__ == "__main__":
    main_method = Main()
    main_method.main()
