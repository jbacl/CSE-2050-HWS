from hw5 import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above
                k_idx = valid_moves((7, 0))
                expected_valid_moves = {(5,1), (6,2)}
                self.assertEqual(k_idx, expected_valid_moves)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx2 = (0, 0)
                expected_valid_moves2 = {(2,1), (1,2)}
                self.assertEqual(valid_moves(k_idx2), expected_valid_moves2)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx3 = (0, 7)
                expected_valid_moves3 = {(2,6), (1,5)}
                self.assertEqual(valid_moves(k_idx3), expected_valid_moves3)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                k_idx4 = (7, 7)
                expected_valid_moves4 = {(5,6), (6,5)}
                self.assertEqual(valid_moves(k_idx4), expected_valid_moves4)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx5 = (3, 3)
                expected_valid_moves5 = {(1,4), (2,5), (4,5), (5,4), (5,2), (4,1), (2,1), (1,2)}
                self.assertEqual(valid_moves(k_idx5), expected_valid_moves5)

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                """Test a few unsolveable puzzles"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x x x - - -
                #2 - - - - - - - -
                #3 - x - k - - - -
                #4 - - - - - - - -
                #5 - - x x x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                p_idxs = {(1,2), (1,3), (1,4), (3,1), (5,2), (5,3), (5,4)}
                k_idx = (3,3)
                self.assertFalse(solveable(p_idxs, k_idx))

        def testSolveableSimple(self):
                """Test a simple solveable puzzle"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - x - -
                #3 - - x - - - - -
                #4 - - - - k - - -
                #5 - - x - - - x -
                #6 - - - x - - - -
                #7 - - - - - - - -

                p_idxs2 = {(2,5), (3,2), (5,2), (6,3), (5,6)}
                k_idx2 = (4,4)
                self.assertTrue(solveable(p_idxs2, k_idx2))
                

        def testSolveableHard(self):
                """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any mistakes"""
                #  0 1 2 3 4 5 6 7
                #0 - - x - x - - -
                #1 - x - - - x - -
                #2 - - - k - - - -
                #3 - x - - - x - -
                #4 - - x - x - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -

                p_idxs3 = {(0,2), (0,4), (1,1), (1,5), (3,1), (4,2), (4,4), (3,5)}
                k_idx3 = (2,3)
                self.assertTrue(solveable(p_idxs3, k_idx3))
                

unittest.main()
