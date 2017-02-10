import requests
import json

# Gets movie information from OMDB API.
def get_movie_json(movie):

    # Sends this JSON in case of error.
    default_json_error = {"Plot": "Description not available at the moment. Sorry :(",
                          "Poster": "https://image.ibb.co/iUi5va/error.jpg",
                          "imdbRating": "N/A"}

    # Formats movie title so it can be read properly by the API.
    title = movie.title.replace(' ', '+').lower()
    try:
        # Tries to make a GET HTTP request. If success, return JSON.
        r = requests.get('http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json')
        movie = r.json()

        # If the response is false, return error JSON
        if movie["Response"] == "False":
            return default_json_error
        else:
            return movie

    except:
        # If request fails, prints an error alert in console and returns default fail info
        print('There is been an error')
        return default_json_error
