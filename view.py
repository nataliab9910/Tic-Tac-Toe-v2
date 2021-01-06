"""TODO: add description here."""

import pygame
import consts


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line


class Assets:
    """TODO: add description here."""
    BACKGROUND_IMG = None
    O_CHECKER_IMG = None
    X_CHECKER_IMG = None

    @staticmethod
    def load():
        """TODO: add description here."""
        Assets.BACKGROUND_IMG = pygame.image.load('assets/background.png')
        Assets.O_CHECKER_IMG = pygame.image.load('assets/O.png')
        Assets.X_CHECKER_IMG = pygame.image.load('assets/X.png')


class Text:
    """TODO: add description here."""
    INSTRUCTION = {consts.NO_PLAYER: "Kliknij tutaj, aby zagrać ponownie.", consts.PLAYER_1: "Ruch Kółka!",
                   consts.PLAYER_2: "Ruch Krzyżyka!"}
    END_GAME = {consts.PLAYER_1: " Wygrywa Kółko! ", consts.PLAYER_2: " Wygrywa Krzyżyk! ", consts.DRAW: " Remis! "}

    SIZE_MEDIUM = 25
    SIZE_BIG = 32
    FONT_NAME = 'freesansbold.ttf'
    COLOR = pygame.Color("black")
    BACKGROUND_COLOR = pygame.Color("#888CA2")


class Window:
    """TODO: add description here."""

    def __init__(self, controller):
        """TODO: add description here."""
        Assets.load()
        pygame.display.set_caption(consts.GAME_TITLE)
        self.surface = pygame.display.set_mode((consts.SURFACE_WIDTH,
                                                consts.BOARD_HEIGHT + consts.TEXT_AREA_HEIGHT))
        self.surface.blit(Assets.BACKGROUND_IMG, (0, 0))
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
                self.controller.mouse_click_handle(click_position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    self.controller.reset_game()

        self.clock.tick(60)
        return True

    def add_checker(self, field, player):
        """TODO: add description here."""
        self.surface.blit({consts.PLAYER_1: Assets.O_CHECKER_IMG,
                           consts.PLAYER_2: Assets.X_CHECKER_IMG}[player],
                          consts.FIELDS_COORDINATES[field])
        pygame.display.flip()

    @staticmethod
    def calculate_field_number(position):
        """TODO: add description here."""
        for field in range(consts.NUMBER_OF_FIELDS):
            field_range = consts.FIELDS_RANGES[field]
            if position[0] in range(*field_range["x_axis"]) and position[1] in range(*field_range["y_axis"]):
                return field
        return consts.WRONG

    @staticmethod
    def is_text_area_clicked(position):
        if position[1] in range(consts.BOARD_HEIGHT, consts.BOARD_HEIGHT + consts.TEXT_AREA_HEIGHT):
            return True
        return False

    def reset(self):
        """TODO: add description here."""
        self.surface.blit(Assets.BACKGROUND_IMG, (0, 0))

    def update_instruction(self, current_player=consts.PLAYER_1):
        pygame.draw.rect(self.surface, Text.BACKGROUND_COLOR,
                         (0, consts.SURFACE_WIDTH, consts.BOARD_HEIGHT, consts.BOARD_HEIGHT + consts.TEXT_AREA_HEIGHT))
        text = Text.INSTRUCTION[current_player]
        self.draw_text(text, Text.SIZE_MEDIUM, consts.TEXT_AREA_CENTER)
        pygame.display.flip()

    def end_game_text(self, result):
        text = Text.END_GAME[result]
        self.draw_text(text, Text.SIZE_BIG, consts.BOARD_CENTER)
        pygame.display.flip()

    def draw_text(self, text, size, position_center):
        font = pygame.font.Font(Text.FONT_NAME, size)
        text = font.render(text, False, Text.COLOR, Text.BACKGROUND_COLOR)
        text_rect = text.get_rect(center=position_center)
        self.surface.blit(text, text_rect)
