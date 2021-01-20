"""Game controllers."""

from abc import ABC, abstractmethod
import sys

import pygame

import consts
import model
import view


class MainController:
    """Defines main program loop."""

    @staticmethod
    def main_loop():
        """Main program loop."""
        pygame.init()
        pygame.font.init()
        view.Assets.load_images()
        game_controller = GameController()
        game_controller.game_loop()


class GameController:
    """Controls all game."""

    def __init__(self):
        """Initializes GameController."""
        self.window = view.Window(self)
        self.logic = model.Logic()
        self.game_state = GameInProgress(self)

    def game_loop(self):
        """Main game loop."""
        self.window.prepare_window()
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def set_game_state(self, new_state):
        """Sets new game state."""
        self.game_state = new_state

    def handle_mouse_click(self, field_number):
        """Handles mouse click respectively to actual game state."""
        self.game_state.mouse_click_reaction(field_number)

    def handle_move(self, field_number):
        """Handles click on given field."""
        is_checker_added = self.logic.add_checker(field_number)
        if is_checker_added:
            player = self.logic.current_player
            self.window.add_checker(field_number, player)
            self.update_game()

    def update_game(self):
        """Updates game state and refreshes window."""
        evaluation = self.logic.evaluate_board()

        if evaluation != consts.NO_PLAYER:
            self.set_game_state(GameEnded(self))

        self.game_state.window_update(evaluation)

    def reset_game(self):
        """Sets default settings."""
        self.window.reset()
        self.logic.reset()

    def flip_players(self):
        """Changes current player to opposite."""
        return self.logic.flip_current_player()

    def update_instruction(self, current_player):
        """Updates instruction in text ares."""
        self.window.update_instruction(current_player)

    def draw_end_game_text(self, game_result):
        """Draws end game text in the middle of the board."""
        self.window.end_game_text(game_result)


class GameState(ABC):
    """Abstraction of game states."""

    def __init__(self, game_controller: GameController):
        """Initializes GameState."""
        self.game_controller = game_controller

    @abstractmethod
    def mouse_click_reaction(self, field_number):
        """Defines mouse click reaction."""

    @abstractmethod
    def window_update(self, game_evaluation):
        """Defines window update steps."""


class GameInProgress(GameState):
    """Concrete game state - game is in progress (no win, no draw)."""

    def mouse_click_reaction(self, field_number):
        """Tries to put checker on choosen field."""
        if field_number not in (consts.WRONG, consts.TEXT_AREA):
            self.game_controller.handle_move(field_number)

    def window_update(self, game_evaluation):
        """Changes instruction in text area."""
        player = self.game_controller.flip_players()
        self.game_controller.update_instruction(player)


class GameEnded(GameState):
    """Concrete game state - game is ended (win or draw)."""

    def mouse_click_reaction(self, field_number):
        """Restarts game if ext area is choosen."""
        if field_number == consts.TEXT_AREA:
            self.game_controller.reset_game()
            self.game_controller.set_game_state(GameInProgress(self.game_controller))
            # self.game_controller.game_state = self.game_controller.continue_game_state

    def window_update(self, game_evaluation):
        """Changes instruction in text area and shows end game instruction in the middle of the board."""
        self.game_controller.update_instruction(consts.NO_PLAYER)
        self.game_controller.draw_end_game_text(game_evaluation)


if __name__ == "__main__":
    # Runs whole program.
    main = MainController()
    main.main_loop()
