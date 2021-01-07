"""TODO: add description here."""

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

# TODO: segregate imports
import sys
import view
import model
import consts
from abc import ABC, abstractmethod


class Controller:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.window = view.Window(self)
        self.logic = model.Logic()
        self.game_result = consts.NO_PLAYER  # Game state

    def run(self):
        """TODO: add description here."""
        self.window.prepare_window()
        # self.window.update_instruction()
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def mouse_click_handle(self, click_position):
        """TODO: add description here."""
        # TODO: add state here
        if self.game_result == consts.NO_PLAYER:
            choosen_field = self.window.calculate_field_number(click_position)
            if choosen_field != consts.WRONG:
                self.handle_move(choosen_field)
        else:
            if self.window.is_text_area_clicked(click_position):
                self.reset_game()

    def handle_move(self, field):
        """TODO: add description here."""
        checker_added = self.logic.add_checker(field)
        if checker_added:
            player = self.logic.current_player
            self.window.add_checker(field, player)
            self.evaluate_game_state()

    def evaluate_game_state(self):
        """TODO: add description here."""
        self.game_result = self.logic.evaluate_board()

        # TODO: add state here
        if self.game_result == consts.NO_PLAYER:
            current_player = self.logic.flip_current_player()
            self.window.update_instruction(current_player)
        else:
            current_player = self.logic.unset_current_player()
            self.window.update_instruction(current_player)
            self.window.end_game_text(self.game_result)

    def reset_game(self):
        """TODO: add description here."""
        self.game_result = consts.NO_PLAYER
        self.window.reset()
        self.logic.reset()


class GameState(ABC):

    @abstractmethod
    def update_game(self):
        pass

    # @abstractmethod
    def mouse_click_handle(self):
        print("hello")


class GameEnd(GameState):
    def update_game(self):
        print("endup")


class GameContinue(GameState):
    def update_game(self):
        print("contup")


cont = GameContinue()
end = GameEnd()
cont.update_game()
cont.mouse_click_handle()
end.mouse_click_handle()
end.update_game()
