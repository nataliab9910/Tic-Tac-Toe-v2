"""TODO: add description here."""

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

# TODO: segregate imports
from abc import ABC, abstractmethod
import sys

import pygame

import consts
import model
import view


class MainController:
    # pylint: disable=R0903
    """TODO: add description here."""

    @staticmethod
    def main_loop():
        """TODO: add description here."""
        pygame.init()
        pygame.font.init()
        view.Assets.load_images()
        game_controller = GameController()
        game_controller.game_loop()


class GameController:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.window = view.Window(self)
        self.logic = model.Logic()

        # self.continue_game_state = GameInProgress(self)
        # self.end_game_state = GameEnded(self)

        self.game_state = GameInProgress(self)

    def game_loop(self):
        """TODO: add description here."""
        self.window.prepare_window()
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def set_game_state(self, new_state):
        self.game_state = new_state

    def handle_mouse_click(self, field_number):
        """TODO: add description here."""
        self.game_state.mouse_click_reaction(field_number)

    def handle_move(self, field_number):
        """TODO: add description here."""
        is_checker_added = self.logic.add_checker(field_number)
        if is_checker_added:
            player = self.logic.current_player
            self.window.add_checker(field_number, player)
            self.update_game()

    def update_game(self):
        """TODO: add description here."""
        evaluation = self.logic.evaluate_board()

        if evaluation != consts.NO_PLAYER:
            self.set_game_state(GameEnded(self))
            # self.game_state = self.end_game_state

        self.game_state.window_update(evaluation)

    def reset_game(self):
        """TODO: add description here."""
        self.window.reset()
        self.logic.reset()

    def flip_players(self):
        """TODO: add description here."""
        return self.logic.flip_current_player()

    def update_instruction(self, current_player):
        """TODO: add description here."""
        self.window.update_instruction(current_player)

    def draw_end_game_text(self, game_result):
        """TODO: add description here."""
        self.window.end_game_text(game_result)


class GameState(ABC):
    """TODO: add description here."""

    def __init__(self, game_controller: GameController):
        """TODO: add description here."""
        self.game_controller = game_controller

    @abstractmethod
    def mouse_click_reaction(self, field_number):
        """TODO: add description here."""

    @abstractmethod
    def window_update(self, game_evaluation):
        """TODO: add description here."""


class GameInProgress(GameState):
    """TODO: add description here."""

    def mouse_click_reaction(self, field_number):
        """TODO: add description here."""
        # choosen_field_number = self.game_controller.position_to_field_number(field_number)
        if field_number not in (consts.WRONG, consts.TEXT_AREA):
            self.game_controller.handle_move(field_number)

    def window_update(self, game_evaluation):
        """TODO: add description here."""
        player = self.game_controller.flip_players()
        self.game_controller.update_instruction(player)


class GameEnded(GameState):
    """TODO: add description here."""

    def mouse_click_reaction(self, field_number):
        """TODO: add description here."""
        if field_number == consts.TEXT_AREA:
            self.game_controller.reset_game()
            self.game_controller.set_game_state(GameInProgress(self.game_controller))
            # self.game_controller.game_state = self.game_controller.continue_game_state

    def window_update(self, game_evaluation):
        """TODO: add description here."""
        self.game_controller.update_instruction(consts.NO_PLAYER)
        self.game_controller.draw_end_game_text(game_evaluation)


if __name__ == "__main__":
    main = MainController()
    main.main_loop()
