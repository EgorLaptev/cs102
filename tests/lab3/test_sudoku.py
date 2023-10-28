import unittest

from src.lab3.sudoku import group, get_row, get_col, get_block

class TestSudoku(unittest.TestCase):
    
    def setUp(self):
        self.group = group
        self.get_row = get_row
        self.get_col = get_col
        self.get_block = get_block

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([9,4,5,2,1,7,4,2,6,0,1,5,3,6,5,4], 4), [[9, 4, 5, 2], [1, 7, 4, 2], [6, 0, 1, 5], [3, 6, 5, 4]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])

        self.assertEqual(get_row([['1', '2', '.', '2'], ['4', '5', '6', '.'], ['7', '8', '9', '0'], ['1', '2', '3', '1']], (2, 0)), ['7', '8', '9', '0'])
        self.assertEqual(get_row([['1', '2'], ['4', '.']], (1, 0)), ['4', '.'])
        self.assertEqual(get_row([['1']], (0, 0)), ['1'])