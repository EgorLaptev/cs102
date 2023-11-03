from typing import List, Dict, Set

class Recommendations:
    def __init__(self, history_path: str, movies_path: str):
        self.history = self.read_history(history_path)
        self.movies = self.read_movies(movies_path)

    def read_history(self, path: str) -> List:
        """ This function return all history of other users from file """
        with open(path, 'r', encoding='UTF-8') as history_file:
            return [ user.split(',') for user in history_file.read().splitlines() ]

    def read_movies(self, path: str) -> Dict:
        """ This function return all movies """
        with open(path, 'r', encoding='UTF-8') as movies_file:
            result = [ movie.split(',') for movie in movies_file.read().splitlines() ]
            result = { movie[0]:movie[1] for movie in result }
        return result

    def get_views(self, movies: Set) -> Dict[str,int]:
        """ This function returns the number of views for each movie """
        views = {}

        for movie in movies:
            views[movie] = sum(user.count(movie) for user in self.history)

        return views

    def get_recommendations(self, user_history: List) -> str:
        """ This function returns the most viewed recommendation based on user history """
        recommendations = self.get_recommendation_set(user_history)
        recommendations_views = self.get_views(recommendations)

        if len(recommendations) > 0:
            # get the most viewed recommendation
            recommendation_id = max(recommendations_views, key=recommendations_views.get)
            recommendation_name = self.movies[recommendation_id]
            return recommendation_name
        else:
            return 'No any recommendations'

    def get_recommendation_set(self, user_history: List) -> Set:
        """ This function returns all recommendations based on user history """
        result = set()

        for user in self.history:
            coincidence = sum( int(movie in user_history) for movie in user )
            if coincidence > len(user)//2:
                result |= { movie for movie in user if movie not in user_history }

        return result


if __name__ == '__main__':
    user_input = input().split()

    recSystem = Recommendations('data/history.txt', 'data/movies.txt')
    recs = recSystem.get_recommendations(user_input)

    print(recs)