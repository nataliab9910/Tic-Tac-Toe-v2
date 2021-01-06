import constants


class Field:
    def __init__(self):
        self.value = constants.NO_PLAYER

    def put_checker(self, player):
        self.value = player

    def is_empty(self):
        return not self.value == constants.NO_PLAYER

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
        pass


if __name__ == "__main__":
    # TODO: delete this statement
    logic = Logic()
    logic.print_board()
