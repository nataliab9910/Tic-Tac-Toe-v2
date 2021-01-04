"""TODO: add description here."""

import pygame
import assets
import view


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

class Main:
    """TODO: add description here."""

    @staticmethod
    def main():
        """TODO: add description here."""
        pygame.init()
        assets.Images.load()

        main_window = view.Window()
        main_window.run()


if __name__ == "__main__":
    Main.main()
