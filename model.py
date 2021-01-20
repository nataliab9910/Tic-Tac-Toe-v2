"""Game logic."""

import consts


class Logic:
    """Defines game rules."""

    def __init__(self):
        """Initializes Logic."""
        self.board = consts.BOARD[:]
        self.current_player = consts.PLAYER_O

    # def print_board(self):
    #     """Prints game board on terminal.
    #
    #     Used to find bugs.
    #     """
    #     for i in range(3):
    #         print(f' {self.board[3 * i]} | '
    #               f'{self.board[1 + 3 * i]} | '
    #               f'{self.board[2 + 3 * i]}')
    #         if i < 2:
    #             print('---+---+---')

    def flip_current_player(self):
        """Changes current player to opposite."""
        self.current_player = {consts.PLAYER_O: consts.PLAYER_X,
                               consts.PLAYER_X: consts.PLAYER_O}[self.current_player]
        return self.current_player

    def add_checker(self, field_number):
        """Puts checker on empty field."""
        if self.board[field_number] == consts.NO_PLAYER:
            self.board[field_number] = self.current_player
            return True
        return False

    def evaluate_board(self):
        """Checks if game is ended (win or draw)."""
        result = self.check_columns()
        if result == consts.NO_PLAYER:
            result = self.check_rows()
            if result == consts.NO_PLAYER:
                result = self.check_diagonals()
                if result == consts.NO_PLAYER:
                    result = self.check_if_draw()

        return result

    def check_columns(self):
        """Looks for winning position in columns."""
        for i in range(consts.FIELDS_IN_COLUMN):
            column_number = consts.FIELDS_IN_COLUMN
            if self.board[i] == self.board[column_number + i] == self.board[2 * column_number + i] != consts.NO_PLAYER:
                return self.board[i]
        return consts.NO_PLAYER

    def check_rows(self):
        """Looks for winning position in rows."""
        for i in range(consts.FIELDS_IN_ROW):
            row_number = consts.FIELDS_IN_ROW * i
            if self.board[row_number] == self.board[row_number + 1] == self.board[row_number + 2] != consts.NO_PLAYER:
                return self.board[row_number]
        return consts.NO_PLAYER

    def check_diagonals(self):
        """Looks for winning position in diagonals."""
        if self.board[0] == self.board[4] == self.board[8] != consts.NO_PLAYER:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != consts.NO_PLAYER:
            return self.board[2]
        return consts.NO_PLAYER

    def check_if_draw(self):
        """Checks if there is any empty field on game board."""
        for field in self.board:
            if field == consts.NO_PLAYER:
                return consts.NO_PLAYER
        return consts.DRAW

    def reset(self):
        """Sets default settings."""
        self.board = consts.BOARD[:]
        self.current_player = consts.PLAYER_O
