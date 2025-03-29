import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        test_bool_1 = m1._cells[0][0].has_top_wall and m1._cells[0][0].has_left_wall
        test_bool_2 = m1._cells[11][9].has_bottom_wall and m1._cells[11][9].has_right_wall
        self.assertEqual(False, test_bool_1)
        self.assertEqual(False, test_bool_2)

    def test_reset_cell_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        Checker = True
        for celllist in m1._cells:
            for cell in celllist:
                if cell.visited:
                    Checker = False
        self.assertEqual(Checker, True)


if __name__ == "__main__":
    unittest.main()

