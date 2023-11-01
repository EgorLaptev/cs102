"""
    This module receives a list of user views 
    and selects a recommendation based on it
"""

from typing import List, Dict, Set


def read_history(path: str) -> List:
    """ This function return all history of other users from file """
    with open(path, 'r', encoding='UTF-8') as history_file:
        return [ user.split(',') for user in history_file.read().splitlines() ]


def read_movies(path: str) -> Dict:
    """ This function return all movies """
    with open(path, 'r', encoding='UTF-8') as movies_file:
        result = [ movie.split(',') for movie in movies_file.read().splitlines() ]
        result = { movie[0]:movie[1] for movie in result }
    return result


def get_views(movies: Set, users_history: List) -> Dict[str,int]:
    """ This function returns the number of views for each movie """
    views = {}

    for movie in movies:
        views[movie] = sum(user.count(movie) for user in users_history)

    return views


def get_recommendations(views: List, users_history: List) -> Set:
    """ This function returns all recommendations based on user history """
    result = set()

    for user in users_history:
        coincidence = sum( int(movie in views) for movie in user )
        if coincidence > len(user)//2:
            result |= { movie for movie in user if movie not in views }


    return result


if __name__ == '__main__':

    user_history = input().split(',')

    # get the history of others
    all_history = read_history('data/history.txt')

    # get the all movies
    all_movies = read_movies('data/movies.txt')

    # get all recommendations by user history
    recommendations = get_recommendations(user_history, all_history)
    recommendations_views = get_views(recommendations, all_history)

    if len(recommendations) > 0:
        # get the most viewed recommendation
        recommendation_id = max(recommendations_views, key=recommendations_views.get)
        recommendation_name = all_movies[recommendation_id]
        print(recommendation_name)
    else:
        print('No any recommendations')
