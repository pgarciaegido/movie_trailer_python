import requests
import json

# Gets movie information from OMDB API.
# Further information regarding the API: http://www.omdbapi.com/
def get_movie_json(movie):

    # Sends this JSON in case of error.
    default_json_error = {"Plot": "Description not available at the moment."
                                  " Sorry :(",
                          "imdbRating": "N/A"}

    # Sends this message in case of ValueError.
    value_error_message = ("It looks that the movie --> " + movie.title +
                    " is not being recognized by the API.\nPlease double "
                    "check if the name introduced is correctly spelled.\n"
                    "If the title is not english, it might be recorded under "
                    "the english name \nCheck http://www.omdbapi.com/ "
                    "for further information.")

    # Formats movie title so it can be read properly by the API.
    title = movie.title.replace(' ', '+').lower()
    try:
        # Tries to make a GET HTTP request. If success, return JSON.
        r = requests.get('http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json')  # NOQA
        movie = r.json()

        # If the response is false, raises an exception
        if movie["Response"] == "False":
            raise ValueError(value_error_message)
        else:
            return movie

    except requests.exceptions.ConnectionError as e:
        # If request fails because there is a Connection Error
        print(e, '\nThere is been a problem with your connection.\n')
        return default_json_error

    except ValueError as e:
        # If movie title not recognized by the API.
        raise
        return default_json_error
