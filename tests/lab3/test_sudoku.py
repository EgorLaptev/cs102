import unittest

from src.lab3.sudoku import *

class TestSudoku(unittest.TestCase):
    
    def setUp(self):
        self.group = group
        self.get_row = get_row
        self.get_col = get_col
        self.get_block = get_block
        self.read_sudoku = read_sudoku
        self.check_solution = check_solution

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([9,4,5,2,1,7,4,2,6,0,1,5,3,6,5,4], 4), [[9, 4, 5, 2], [1, 7, 4, 2], [6, 0, 1, 5], [3, 6, 5, 4]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])
        self.assertEqual(get_row([['1']], (0, 0)), ['1'])
        self.assertEqual(get_row([['1', '2'], ['4', '.']], (1, 0)), ['4', '.'])
        self.assertEqual(get_row([['1', '2', '.', '2'], ['4', '5', '6', '.'], ['7', '8', '9', '0'], ['1', '2', '3', '1']], (2, 0)), ['7', '8', '9', '0'])

    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])
        self.assertEqual(get_col([['1']], (0, 0)), ['1'])
        self.assertEqual(get_col([['1', '2'], ['4', '.']], (0, 1)), ['2', '.'])
        self.assertEqual(get_col([['1', '2', '.', '2'], ['4', '5', '6', '.'], ['7', '8', '9', '0'], ['1', '2', '3', '1']], (0, 3)), ['2', '.', '0', '1'])

    def test_get_block(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))
        self.assertEqual(find_empty_positions([['1', '.', '3'], ['4', '5', '.'], ['.', '8', '9']]), (0, 1))

    def test_find_possible_values(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (0,2)), {'1', '2', '4'})
        self.assertEqual(find_possible_values(grid, (4,7)), {'2', '5', '9'})

    def test_check_solution(self):
        self.assertEqual(check_solution([
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']]), True)
        self.assertEqual(check_solution([
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
            ['1', '9', '8', '2', '4', '2', '5', '6', '7'], 
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']]), False)
        
    def test_generate_sudoku(self):
        self.assertEqual(sum(1 for row in generate_sudoku(40) for e in row if e == '.'), 41)
        self.assertEqual(sum(1 for row in generate_sudoku(1000) for e in row if e == '.'), 0)
        self.assertEqual(sum(1 for row in generate_sudoku(0) for e in row if e == '.'), 81)