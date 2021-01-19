"""TODO: add description here."""

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

import consts


class Logic:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.board = consts.BOARD[:]
        self.current_player = consts.PLAYER_O

    def print_board(self):
        """TODO: add description here."""
        # TODO: delete this function
        for i in range(3):
            print(f' {self.board[3 * i]} | '
                  f'{self.board[1 + 3 * i]} | '
                  f'{self.board[2 + 3 * i]}')
            if i < 2:
                print('---+---+---')

    def flip_current_player(self):
        """TODO: add description here."""
        self.current_player = {consts.PLAYER_O: consts.PLAYER_X,
                               consts.PLAYER_X: consts.PLAYER_O}[self.current_player]
        return self.current_player

    def add_checker(self, field_number):
        """TODO: add description here."""
        if self.board[field_number] == consts.NO_PLAYER:
            self.board[field_number] = self.current_player
            return True
        return False

    def evaluate_board(self):
        """TODO: add description here."""
        result = self.check_columns()
        if result == consts.NO_PLAYER:
            result = self.check_rows()
            if result == consts.NO_PLAYER:
                result = self.check_diagonals()
                if result == consts.NO_PLAYER:
                    result = self.check_if_draw()

        return result

    def check_columns(self):
        """TODO: add description here."""
        for i in range(consts.FIELDS_IN_COLUMN):
            column_number = consts.FIELDS_IN_COLUMN
            if self.board[i] == self.board[column_number + i] == self.board[2 * column_number + i] != consts.NO_PLAYER:
                return self.board[i]
        return consts.NO_PLAYER

    def check_rows(self):
        """TODO: add description here."""
        for i in range(consts.FIELDS_IN_ROW):
            row_number = consts.FIELDS_IN_ROW * i
            if self.board[row_number] == self.board[row_number + 1] == self.board[row_number + 2] != consts.NO_PLAYER:
                return self.board[row_number]
        return consts.NO_PLAYER

    def check_diagonals(self):
        """TODO: add description here."""
        if self.board[0] == self.board[4] == self.board[8] != consts.NO_PLAYER:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != consts.NO_PLAYER:
            return self.board[2]
        return consts.NO_PLAYER

    def check_if_draw(self):
        """TODO: add description here."""
        for field in self.board:
            if field == consts.NO_PLAYER:
                return consts.NO_PLAYER
        return consts.DRAW

    def reset(self):
        """TODO: add description here."""
        self.board = consts.BOARD[:]
        self.current_player = consts.PLAYER_O
