"""TODO: add description here."""

import pygame
import controller


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

class Main:
    """TODO: add description here."""

    @staticmethod
    def main():
        """TODO: add description here."""
        pygame.init()  # move to view?

        main_controller = controller.Controller()
        main_controller.run()

        # main_window = view.Window()
        # main_window.run()


if __name__ == "__main__":
    Main.main()
