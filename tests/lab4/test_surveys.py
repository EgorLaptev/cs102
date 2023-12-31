import unittest
from src.lab4.surveys.main import GroupDistributions

class TestSurveys(unittest.TestCase):
    
    maxDiff = None

    def setUp(self):
        self.groupSystem = GroupDistributions()
        self.distribute = self.groupSystem.distribute
    
    def test_distribute(self):
        self.assertEqual(self.distribute(
            [['Михаил', 18], ['Суворкин', 23], ['Игорь', 24]],
            ['25', '45', '18', '60', '80', '35']
        ), [[], [], [], [], [], [['Суворкин', 23], ['Игорь', 24]], [['Михаил', 18]]])
        
        self.assertEqual(self.distribute(
            [['Гаврилов Максим', 34], ['Иванов Иван', 35], ['Эльдар Джарахов', 29], ['Петросян', 78], ['Орхан Андрей', 18], ['Герасим Георгий', 43]],
            []
        ), [[['Гаврилов Максим', 34], ['Иванов Иван', 35], ['Эльдар Джарахов', 29], ['Петросян', 78], ['Орхан Андрей', 18], ['Герасим Георгий', 43]]])
        
        self.assertEqual(self.distribute(
            [['Гаврилов Максим', 34], ['Иванов Иван', 35], ['Эльдар Джарахов', 29], ['Петросян', 78], ['Орхан Андрей', 18], ['Герасим Георгий', 43]],
            ['18', '25', '35', '45', '60', '80']
        ), [[], [['Петросян', 78]], [], [['Герасим Георгий', 43]], [['Гаврилов Максим', 34], ['Иванов Иван', 35], ['Эльдар Джарахов', 29]], [], [['Орхан Андрей', 18]]])