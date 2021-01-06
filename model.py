import constants


class Field:
    def __init__(self):
        self.value = constants.NO_PLAYER

    def put_checker(self, player):
        self.value = player

    def is_empty(self):
        return self.value == constants.NO_PLAYER

    def reset(self):
        self.value = constants.NO_PLAYER


class Logic:
    BOARD = [Field(), Field(), Field(),
             Field(), Field(), Field(),
             Field(), Field(), Field()]

    def __init__(self):
        self.board = Logic.BOARD[:]
        self.current_player = constants.PLAYER_1

    def print_board(self):
        # TODO: delete this function
        for i in range(3):
            print(f' {self.board[3 * i].value} | '
                  f'{self.board[1 + 3 * i].value} | '
                  f'{self.board[2 + 3 * i].value}')
            if i < 2:
                print('---+---+---')

    def flip_current_player(self):
        self.current_player = {constants.PLAYER_1: constants.PLAYER_2,
                               constants.PLAYER_2: constants.PLAYER_1}[self.current_player]

    def check_if_can_be_added(self, field):
        if self.board[field].value == constants.NO_PLAYER:
            self.board[field].value = self.current_player
            return True
        return False

    def evaluate_board(self):
        result = self.check_columns()
        if result == constants.NO_PLAYER:
            result = self.check_rows()
            if result == constants.NO_PLAYER:
                result = self.check_diagonals()
                if result == constants.NO_PLAYER:
                    result = self.check_draw()

        return result

    def check_columns(self):
        for i in range(constants.FIELDS_IN_COLUMN):
            column_number = constants.FIELDS_IN_COLUMN
            if self.board[i].value == self.board[column_number + i].value == self.board[2 * column_number + i].value != constants.NO_PLAYER:
                return self.board[i].value
        return constants.NO_PLAYER

    def check_rows(self):
        for i in range(constants.FIELDS_IN_ROW):
            row_number = constants.FIELDS_IN_ROW * i
            if self.board[row_number].value == self.board[row_number + 1].value == self.board[row_number + 2].value != constants.NO_PLAYER:
                return self.board[row_number].value
        return constants.NO_PLAYER

    def check_diagonals(self):
        if self.board[0].value == self.board[4].value == self.board[8].value != constants.NO_PLAYER:
            return self.board[0].value
        elif self.board[2].value == self.board[4].value == self.board[6].value != constants.NO_PLAYER:
            return self.board[2].value
        return constants.NO_PLAYER

    def check_draw(self):
        for field in self.board:
            if field.is_empty():
                return constants.NO_PLAYER
        return constants.DRAW

    def reset(self):
        for field in self.board:
            field.reset()
        self.current_player = constants.PLAYER_1


if __name__ == "__main__":
    # TODO: delete this statement
    logic = Logic()
    logic.print_board()
