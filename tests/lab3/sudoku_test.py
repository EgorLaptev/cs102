import unittest

from src.lab3.sudoku import group

class TestCaesar(unittest.TestCase):
    
    def setUp(self):
        self.group = group

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([9,4,5,2,1,7,4,2,6,0,1,5,3,6,5,4], 4), [[9, 4, 5, 2], [1, 7, 4, 2], [6, 0, 1, 5], [3, 6, 5, 4]])