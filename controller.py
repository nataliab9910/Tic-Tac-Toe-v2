import view
import model
import sys


class Controller:

    def __init__(self):
        self.window = view.Window(self)
        self.logic = model.Logic()

    def run(self):
        running = True
        while running:
            running = self.window.wait_for_events()
        sys.exit(0)

    def add_checker(self, field):
        possible_to_add = self.logic.check_if_can_be_added(field)
        if possible_to_add:
            self.window.add_checker(field, self.logic.current_player)
            self.logic.print_board()
            #evaluate board
            self.logic.flip_current_player()
