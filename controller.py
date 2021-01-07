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

    def __init__(self):
        """TODO: add description here."""
        self.game_controller = GameController()

    def main_loop(self):
        """TODO: add description here."""
        pygame.init()
        pygame.font.init()
        self.game_controller.game_loop()


class GameController:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.window = view.Window(self)
        self.logic = model.Logic()

        self.continue_game = ContinueGame(self)
        self.end_game = EndGame(self)

        self.game_state = self.continue_game

    def game_loop(self):
        """TODO: add description here."""
        self.window.prepare_window()
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def mouse_click(self, click_position):
        """TODO: add description here."""
        self.game_state.mouse_click_handle(click_position)

    def handle_move(self, field):
        """TODO: add description here."""
        is_checker_added = self.logic.add_checker(field)
        if is_checker_added:
            player = self.logic.current_player
            self.window.add_checker(field, player)
            self.evaluate_game()

    def evaluate_game(self):
        """TODO: add description here."""
        evaluation = self.logic.evaluate_board()

        if evaluation != consts.NO_PLAYER:
            self.game_state = self.end_game

        self.game_state.update_window(evaluation)

    def reset_game(self):
        """TODO: add description here."""
        self.window.reset()
        self.logic.reset()

    def position_to_field_number(self, position):
        """TODO: add description here."""
        return self.window.calculate_field_number(position)

    def flip_players(self):
        """TODO: add description here."""
        return self.logic.flip_current_player()

    def update_instruction(self, player):
        """TODO: add description here."""
        self.window.update_instruction(player)

    def draw_end_game_text(self, game_result):
        """TODO: add description here."""
        self.window.end_game_text(game_result)


class GameState(ABC):
    """TODO: add description here."""

    def __init__(self, game_controller: GameController):
        """TODO: add description here."""
        self.game_controller = game_controller

    @abstractmethod
    def mouse_click_handle(self, click_position):
        """TODO: add description here."""

    @abstractmethod
    def update_window(self, evaluation):
        """TODO: add description here."""


class ContinueGame(GameState):
    """TODO: add description here."""

    def mouse_click_handle(self, click_position):
        """TODO: add description here."""
        choosen_field = self.game_controller.position_to_field_number(click_position)
        if choosen_field not in (consts.WRONG, consts.TEXT_AREA):
            self.game_controller.handle_move(choosen_field)

    def update_window(self, evaluation):
        """TODO: add description here."""
        player = self.game_controller.flip_players()
        self.game_controller.update_instruction(player)


class EndGame(GameState):
    """TODO: add description here."""

    def mouse_click_handle(self, click_position):
        """TODO: add description here."""
        if self.game_controller.position_to_field_number(click_position) == consts.TEXT_AREA:
            self.game_controller.reset_game()
            self.game_controller.game_state = self.game_controller.continue_game

    def update_window(self, evaluation):
        """TODO: add description here."""
        self.game_controller.update_instruction(consts.NO_PLAYER)
        self.game_controller.draw_end_game_text(evaluation)


if __name__ == "__main__":
    main = MainController()
    main.main_loop()
