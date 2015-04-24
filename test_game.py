from game import Puzzle
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        N =5
        puzzle = Puzzle(N)
        self.assertTrue(puzzle.is_finished() == True)
        self.assertTrue(puzzle.get_valid_moves().__len__() == 2)
        self.assertTrue(len(puzzle.state) == N*N)
        

if __name__ == '__main__':
    unittest.main()
