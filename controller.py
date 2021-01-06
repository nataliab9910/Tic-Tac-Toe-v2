import view
import model
import constants
import sys


class Controller:

    def __init__(self):
        self.window = view.Window(self)
        self.logic = model.Logic()
        self.game_result = constants.NO_PLAYER

    def run(self):
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def mouse_click_handle(self, click_position):
        if self.game_result == constants.NO_PLAYER:
            choosen_field = self.window.calculate_field_number(click_position)
            if choosen_field != constants.WRONG:
                self.handle_move(choosen_field)
        else:
            self.reset()

    def handle_move(self, field):
        possible_to_add = self.logic.check_if_can_be_added(field)
        if possible_to_add:
            player = self.logic.current_player
            self.window.add_checker(field, player)
            self.logic.print_board()
            self.game_result = self.logic.evaluate_board()
            self.logic.flip_current_player()

    def reset(self):
        self.game_result = constants.NO_PLAYER
        self.window.reset()
        self.logic.reset()
