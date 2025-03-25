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
    if watched == []:
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
    most_watched = max(genre_count, key=genre_count.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3--------------------
# -----------------------------------------
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


