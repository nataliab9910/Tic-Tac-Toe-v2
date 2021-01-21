"""Application tests."""

import unittest

import consts
import model


class LogicTest(unittest.TestCase):

    def setUp(self):
        self.logic = model.Logic()

    def test_flip_current_player(self):
        self.logic.current_player = consts.PLAYER_O
        self.assertEqual(self.logic.flip_current_player(), consts.PLAYER_X)
        self.assertEqual(self.logic.flip_current_player(), consts.PLAYER_O)

    def test_add_checker(self):
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X,
                            consts.PLAYER_O, consts.NO_PLAYER, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.NO_PLAYER]
        # field with O checker
        self.assertFalse(self.logic.add_checker(0))
        # empty field
        self.assertTrue(self.logic.add_checker(1))
        # field with X checker
        self.assertFalse(self.logic.add_checker(6))

    def test_evaluate_board(self):
        # player O wins in column
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_X, consts.NO_PLAYER,
                            consts.PLAYER_O, consts.PLAYER_O, consts.PLAYER_X,
                            consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X]
        self.assertEqual(self.logic.evaluate_board(), consts.PLAYER_O)

        # player X wins in row
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.PLAYER_X, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_O, consts.NO_PLAYER]
        self.assertEqual(self.logic.evaluate_board(), consts.PLAYER_X)

        # player X wins in diagonal
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_X, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.PLAYER_O, consts.NO_PLAYER]
        self.assertEqual(self.logic.evaluate_board(), consts.PLAYER_X)

        # draw
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_X]
        self.assertEqual(self.logic.evaluate_board(), consts.DRAW)

        # no win or draw
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X,
                            consts.PLAYER_O, consts.NO_PLAYER, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.NO_PLAYER]
        self.assertEqual(self.logic.evaluate_board(), consts.NO_PLAYER)

    def test_check_columns(self):
        # player O wins in first column
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_X, consts.NO_PLAYER,
                            consts.PLAYER_O, consts.NO_PLAYER, consts.NO_PLAYER]
        self.assertEqual(self.logic.check_columns(), consts.PLAYER_O)

        # player X wins in second column
        self.logic.board = [consts.NO_PLAYER, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.NO_PLAYER, consts.PLAYER_X, consts.NO_PLAYER]
        self.assertEqual(self.logic.check_columns(), consts.PLAYER_X)

        # player O wins in third column

        # win in row
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_X]
        self.assertEqual(self.logic.check_columns(), consts.NO_PLAYER)

        # no win
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_O, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_X]
        self.assertEqual(self.logic.check_columns(), consts.NO_PLAYER)

    def test_check_rows(self):
        # player O wins in first row
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_X]
        self.assertEqual(self.logic.check_rows(), consts.PLAYER_O)

        # player X wins in second row
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_X, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_O, consts.NO_PLAYER]
        self.assertEqual(self.logic.check_rows(), consts.PLAYER_X)

        # player X wins in third row
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_O, consts.NO_PLAYER,
                            consts.PLAYER_X, consts.PLAYER_X, consts.PLAYER_X]
        self.assertEqual(self.logic.check_rows(), consts.PLAYER_X)

        # no win in rows
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_X, consts.NO_PLAYER]
        self.assertEqual(self.logic.check_rows(), consts.NO_PLAYER)

    def test_check_diagonals(self):
        # player X wins in left diagonal
        self.logic.board = [consts.PLAYER_X, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_X]
        self.assertEqual(self.logic.check_diagonals(), consts.PLAYER_X)

        # player O wins in right diagonal
        self.logic.board = [consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.NO_PLAYER]
        self.assertEqual(self.logic.check_diagonals(), consts.PLAYER_O)

        # draw
        self.logic.board = [consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O]
        self.assertEqual(self.logic.check_diagonals(), consts.NO_PLAYER)

        # no win in diagonals
        self.logic.board = [consts.PLAYER_O, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_X,
                            consts.NO_PLAYER, consts.PLAYER_X, consts.PLAYER_O]
        self.assertEqual(self.logic.check_diagonals(), consts.NO_PLAYER)

    def test_check_if_draw(self):
        # draw
        self.logic.board = [consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_X,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_O]
        self.assertTrue(self.logic.check_if_draw())

        # draw
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_X,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_O, consts.PLAYER_X]
        self.assertTrue(self.logic.check_if_draw())

        # no draw
        self.logic.board = [consts.PLAYER_O, consts.PLAYER_X, consts.PLAYER_X,
                            consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_O, consts.PLAYER_X]
        self.assertFalse(self.logic.check_if_draw())

    def test_reset(self):
        self.logic.board = [consts.PLAYER_X, consts.NO_PLAYER, consts.PLAYER_O,
                            consts.PLAYER_X, consts.PLAYER_O, consts.PLAYER_O,
                            consts.PLAYER_O, consts.PLAYER_X, consts.NO_PLAYER]
        self.logic.current_player = consts.PLAYER_X
        self.logic.reset()
        self.assertEqual(self.logic.board, consts.BOARD)
        self.assertEqual(self.logic.current_player, consts.PLAYER_O)


if __name__ == '__main__':
    unittest.main()
