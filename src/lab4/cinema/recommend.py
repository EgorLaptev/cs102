"""
    This module receives a list of user views 
    and selects a recommendation based on it
"""

from typing import List, Dict, Set

user_history = input().split(',')


# get the history of others
with open('data/history.txt', 'r', encoding='UTF-8') as history_file:
    history = [ user.split(',') for user in history_file.read().splitlines() ]


# get the movies
with open('data/movies.txt', 'r', encoding='UTF-8') as movies_file:
    all_movies = [ movie.split(',') for movie in movies_file.read().splitlines() ]
    all_movies = { movie[0]:movie[1] for movie in all_movies }


def get_views(movies: Set) -> Dict[str,int]:
    """ This function returns the number of views for each movie """
    views = {}

    for movie in movies:
        views[movie] = sum(user.count(movie) for user in history)

    return views


def get_recommendations(views: List, users_history: List) -> Dict[str, int]:
    """ This function returns all recommendations based on user history """
    result = set()

    for user in users_history:
        coincidence = sum( int(movie in views) for movie in user )
        if coincidence > len(user)//2:
            result |= { movie for movie in user if movie not in views }

    return get_views(result)


# get all recommendations by user history
recommendations = get_recommendations(user_history, history)

# get the most viewed recommendation
recommendation_id = max(recommendations, key=recommendations.get)
recommendation_name = all_movies[recommendation_id]

print(recommendation_name)
