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

    def wait_for_events(self):
        """TODO: add description here."""

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                choosen_field = self.calculate_field_number(click_position)
                if choosen_field != constants.WRONG:
                    self.controller.add_checker(choosen_field)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    pass

        self.clock.tick(60)
        return True

    def add_checker(self, field, player):
        self.surface.blit({constants.PLAYER_1: Assets.O_CHECKER, constants.PLAYER_2: Assets.X_CHECKER}[player],
                          constants.FIELDS_COORDINATES[field])

    @staticmethod
    def calculate_field_number(position):
        for field in range(constants.NUMBER_OF_FIELDS):
            field_range = constants.FIELDS_RANGES[field]
            if position[0] in range(*field_range["x_axis"]) and position[1] in range(*field_range["y_axis"]):
                return field
        return constants.WRONG


class Instruction:
    def __init__(self, position):
        self.text = "Ruch Kółka!"
        self.position = position
