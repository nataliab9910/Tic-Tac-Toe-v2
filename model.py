import constants


class Field:
    def __init__(self):
        self.value = constants.NO_PLAYER

    # put checker
    # check if empty


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


if __name__ == "__main__":
    # TODO: delete this statement
    logic = Logic()
    logic.print_board()
