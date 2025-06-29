import unittest

from game_tic_tac_toe import TicTacToe


class TestGameLogic(unittest.TestCase):
    def test_check_winner(self):
        #chk x wins the first row
        board = [['X', 'X', 'X'],
                 ['', '', ''],
                 ['', '', '']]
        self.assertTrue(TicTacToe.check_winner(None, 'X', board))
        self.assertFalse(TicTacToe.check_winner(None, 'O', board))


    def test_winner_column(self):
        #chk O wins the column
        board = [['O', 'X', 'X'],
                 ['', 'O', ''],
                 ['', '', 'O']]
        self.assertTrue(TicTacToe.check_winner(None, 'O', board))
        self.assertFalse(TicTacToe.check_winner(None, 'X', board))

    def test_is_draw_true(self):
        board = [['X', 'O', 'X'],
                 ['X', 'O', 'O'],
                 ['O', 'X', 'X']]
        self.assertTrue(TicTacToe.is_draw(None, board))

    def test_is_draw_false(self):
        board = [['X', 'O', ''],
                 ['X', 'O', 'O'],
                 ['O', 'X', 'X']]
        self.assertFalse(TicTacToe.is_draw(None, board))

    def test_minimax_and_best_move_block(self):
        # CPU is X and should block O from winning
        ttt = object.__new__(TicTacToe)
        ttt.computer_symbol = 'X'
        ttt.player_symbol = 'O'
        # Board where O can win on (0,2) so CPU must place at (0,2)
        ttt.board = [['O', 'O', ''],
                     ['X', 'X', ''],
                     ['', '', '']]
        move = ttt.best_move()
        self.assertEqual(move, (0, 2))

    def test_minimax_and_best_move_win(self):
        # CPU is X and can win immediately
        ttt = object.__new__(TicTacToe)
        ttt.computer_symbol = 'X'
        ttt.player_symbol = 'O'
        ttt.board = [['X', 'X', ''],
                     ['O', 'O', ''],
                     ['', '', '']]
        move = ttt.best_move()
        self.assertEqual(move, (0, 2))

if __name__ == '__main__':
    unittest.main()