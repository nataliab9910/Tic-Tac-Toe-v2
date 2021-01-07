"""TODO: add description here."""

# pylint: disable=W0511
# pylint: disable=E1101
# TODO: delete this line

import consts


class Field:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.value = consts.NO_PLAYER

    def put_checker(self, player):
        """TODO: add description here."""
        self.value = player

    def is_empty(self):
        """TODO: add description here."""
        return self.value == consts.NO_PLAYER

    def reset(self):
        """TODO: add description here."""
        self.value = consts.NO_PLAYER


class Logic:
    """TODO: add description here."""

    def __init__(self):
        """TODO: add description here."""
        self.board = [Field(), Field(), Field(),
                      Field(), Field(), Field(),
                      Field(), Field(), Field()]
        self.current_player = consts.PLAYER_1

    def print_board(self):
        """TODO: add description here."""
        # TODO: delete this function
        for i in range(3):
            print(f' {self.board[3 * i].value} | '
                  f'{self.board[1 + 3 * i].value} | '
                  f'{self.board[2 + 3 * i].value}')
            if i < 2:
                print('---+---+---')

    def flip_current_player(self):
        """TODO: add description here."""
        self.current_player = {consts.PLAYER_1: consts.PLAYER_2,
                               consts.PLAYER_2: consts.PLAYER_1}[self.current_player]
        return self.current_player

    def add_checker(self, field):
        """TODO: add description here."""
        if self.board[field].value == consts.NO_PLAYER:
            self.board[field].value = self.current_player
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
                    result = self.check_draw()

        return result

    def check_columns(self):
        """TODO: add description here."""
        for i in range(consts.FIELDS_IN_COLUMN):
            column_number = consts.FIELDS_IN_COLUMN
            if self.board[i].value == self.board[column_number + i].value == \
                    self.board[2 * column_number + i].value != consts.NO_PLAYER:
                return self.board[i].value
        return consts.NO_PLAYER

    def check_rows(self):
        """TODO: add description here."""
        for i in range(consts.FIELDS_IN_ROW):
            row_number = consts.FIELDS_IN_ROW * i
            if self.board[row_number].value == self.board[row_number + 1].value == \
                    self.board[row_number + 2].value != consts.NO_PLAYER:
                return self.board[row_number].value
        return consts.NO_PLAYER

    def check_diagonals(self):
        """TODO: add description here."""
        if self.board[0].value == self.board[4].value == self.board[8].value != consts.NO_PLAYER:
            return self.board[0].value
        if self.board[2].value == self.board[4].value == self.board[6].value != consts.NO_PLAYER:
            return self.board[2].value
        return consts.NO_PLAYER

    def check_draw(self):
        """TODO: add description here."""
        for field in self.board:
            if field.is_empty():
                return consts.NO_PLAYER
        return consts.DRAW

    def unset_current_player(self):
        """TODO: add description here."""
        self.current_player = consts.NO_PLAYER
        return self.current_player

    def reset(self):
        """TODO: add description here."""
        for field in self.board:
            field.reset()
        self.current_player = consts.PLAYER_1
