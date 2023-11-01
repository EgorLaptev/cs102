import unittest

from src.lab4.cinema.recommend import *

class TestCinema(unittest.TestCase):
    
    def setUp(self):
        self.get_views = get_views
        self.get_recommendations = get_recommendations
        self.read_history = read_history
        self.read_movies = read_movies

    def test_get_views(self):
        history = read_history('src/lab4/cinema/data/history.txt')

        self.assertEqual(get_views({'3'}, history), {'3': 4})
        self.assertEqual(get_views({'4', '6'}, history), {'4': 2, '6': 3})
        self.assertEqual(get_views({'1', '5', '8', '9'}, history), {'5': 3, '1': 2, '9': 3, '8': 2})
        self.assertEqual(get_views({}, history), {})

    def test_get_recommendations(self):
        history = read_history('src/lab4/cinema/data/history.txt')

        self.assertEqual(get_recommendations(['2', '4'], history), {'3'})
        self.assertEqual(get_recommendations(['4', '7', '8'], history), set())
        self.assertEqual(get_recommendations(['9'], history), set())
        self.assertEqual(get_recommendations([], history), set())