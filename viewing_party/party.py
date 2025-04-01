def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    
    return user_data

def get_watched_avg_rating(user_data):
    # gets the list of movies that have been watched. If empty, return 0.
    watched = user_data["watched"]
    if not watched:
        return 0.0
    # sums the ratings of all the movies that have been watched. returns average rating.
    total = 0
    for movie in watched:
        total += movie["rating"]

    return total / len(watched)

def get_most_watched_genre(user_data):
    # If the user hasn't watched any movies, return None
    if not user_data["watched"]:
        return None

    genre_count = {}

    # Loop through watched movies and get genre of current movie
    for movie in user_data["watched"]:
        genre = movie["genre"] 
        
        if genre in genre_count:
            genre_count[genre] += 1

        else:
            genre_count[genre] = 1

    # return genre with highest count of movies
    most_watched = None
    highest_count = 0

    for genre in genre_count:
        if genre_count[genre] > highest_count:
            most_watched = genre
            highest_count = genre_count[genre]

    return most_watched

    
# get list of movies user has watched, but friends haven't.
def get_friends_movies(user_data):
    titles = set()

    for friend in user_data['friends']:
        for movie in friend['watched']:
            titles.add(movie['title'])

    return titles


def get_unique_watched(user_data):
    unique_movies = []
    friends_watched = get_friends_movies(user_data)

    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    friends_movie_for_user = []

    user_watched = set()
    for movie in user_data["watched"]:
        user_watched.add(movie["title"])

    friends_watched = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie["title"] not in friends_watched:
                friends_movie_for_user.append(movie)
                friends_watched.add(movie["title"])

    return friends_movie_for_user
        
        
def get_available_recs(user_data):
    subscriptions = set(user_data.get("subscriptions", []))
    recommendations = []

    friends_unique_movies = get_friends_unique_watched(user_data)
    
    for movie in friends_unique_movies:
        if movie["host"] in subscriptions:
            recommendations.append(movie)

    return recommendations

def get_new_rec_by_genre(user_data):
    recommendations = []

    if not user_data or not user_data["watched"]:
        return []

    most_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in friends_unique_movies:
        if movie["genre"] == most_genre:
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):
    unique_user_movies = get_unique_watched(user_data)
    favorites = user_data.get("favorites", [])
    recommendations = []

    for movie in favorites:
        if movie in unique_user_movies:
            recommendations.append(movie)

    return recommendations