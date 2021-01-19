"""TODO: add description here."""

# TODO: segregate imports
import pygame
import consts


# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line


class Assets:
    """TODO: add description here."""
    # pylint: disable=R0903
    # TODO: delete this line
    BACKGROUND_IMG = None
    O_CHECKER_IMG = None
    X_CHECKER_IMG = None

    @staticmethod
    def load_images():
        """TODO: add description here."""
        Assets.BACKGROUND_IMG = pygame.image.load('assets/background.png')
        Assets.O_CHECKER_IMG = pygame.image.load('assets/O.png')
        Assets.X_CHECKER_IMG = pygame.image.load('assets/X.png')


class Text:
    """TODO: add description here."""
    # pylint: disable=R0903
    # TODO: delete this line
    INSTRUCTIONS = {consts.NO_PLAYER: "Kliknij tutaj, aby zagrać ponownie.",
                    consts.PLAYER_O: "Ruch Kółka!",
                    consts.PLAYER_X: "Ruch Krzyżyka!"}
    END_GAME = {consts.PLAYER_O: " Wygrywa Kółko! ",
                consts.PLAYER_X: " Wygrywa Krzyżyk! ",
                consts.DRAW: " Remis! "}

    SIZE_MEDIUM = 25
    SIZE_BIG = 32
    FONT_NAME = 'freesansbold.ttf'
    COLOR = pygame.Color("black")
    BACKGROUND_COLOR = pygame.Color("#888CA2")


class Window:
    """TODO: add description here."""

    def __init__(self, controller):
        """TODO: add description here."""
        self.surface = pygame.display.set_mode((consts.SURFACE_WIDTH, consts.SURFACE_HEIGHT))
        self.controller = controller

    def prepare_window(self):
        pygame.display.set_caption(consts.GAME_TITLE)
        self.surface.blit(Assets.BACKGROUND_IMG, (0, 0))
        self.update_instruction()

    def wait_for_events(self):
        """TODO: add description here."""

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                field_number = self.calculate_field_number(click_position)
                self.controller.handle_mouse_click(field_number)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    self.controller.reset_game()

        return True

    def add_checker(self, field_number, player):
        """TODO: add description here."""
        self.surface.blit({consts.PLAYER_O: Assets.O_CHECKER_IMG,
                           consts.PLAYER_X: Assets.X_CHECKER_IMG}[player],
                          consts.FIELDS_COORDINATES[field_number])
        pygame.display.flip()

    @staticmethod
    def calculate_field_number(position):
        """TODO: add description here."""
        if position[1] in range(consts.BOARD_HEIGHT, consts.SURFACE_HEIGHT):
            return consts.TEXT_AREA
        for field in range(consts.NUMBER_OF_FIELDS):
            field_range = consts.FIELDS_RANGES[field]
            if position[0] in range(*field_range["x_axis"]) and position[1] in range(*field_range["y_axis"]):
                return field
        return consts.WRONG

    # @staticmethod
    # def is_text_area_clicked(position):
    #     """TODO: add description here."""
    #     if position[1] in range(consts.BOARD_HEIGHT, consts.SURFACE_HEIGHT):
    #         return True
    #     return False

    def reset(self):
        """TODO: add description here."""
        self.surface.blit(Assets.BACKGROUND_IMG, (0, 0))
        self.update_instruction()

    def update_instruction(self, current_player=consts.PLAYER_O):
        """TODO: add description here."""
        pygame.draw.rect(self.surface, Text.BACKGROUND_COLOR,
                         (0, consts.SURFACE_WIDTH, consts.BOARD_HEIGHT, consts.SURFACE_HEIGHT))
        text = Text.INSTRUCTIONS[current_player]
        self.draw_text(text, Text.SIZE_MEDIUM, consts.TEXT_AREA_CENTER)
        pygame.display.flip()

    def end_game_text(self, game_result):
        """TODO: add description here."""
        text = Text.END_GAME[game_result]
        self.draw_text(text, Text.SIZE_BIG, consts.BOARD_CENTER)
        pygame.display.flip()

    def draw_text(self, text, size, position_center):
        """TODO: add description here."""
        font = pygame.font.Font(Text.FONT_NAME, size)
        text = font.render(text, False, Text.COLOR, Text.BACKGROUND_COLOR)
        text_rect = text.get_rect(center=position_center)
        self.surface.blit(text, text_rect)
