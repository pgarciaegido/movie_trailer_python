import requests
import json

# Gets movie information from OMDB API.
# Further information regarding the API: http://www.omdbapi.com/
def get_movie_json(movie):

    # Sends this JSON in case of error.
    default_json_error = {"Plot": "Description not available at the moment."
                                  " Sorry :(",
                          "imdbRating": "N/A"}

    # Sends this message in case of error.
    error_message = ("It looks that the movie --> " + movie.title +
                    " is not being recognized by the API or the server is "
                    "not responding.\nPlease double check if the name "
                    "introduced is correctly spelled.\nIf the title is not "
                    "english, it might be recorded under the english name \n"
                    "Check http://www.omdbapi.com/ for further information.")

    # Formats movie title so it can be read properly by the API.
    title = movie.title.replace(' ', '+').lower()
    try:
        # Tries to make a GET HTTP request. If success, return JSON.
        r = requests.get('http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json')  # NOQA
        movie = r.json()

        # If the response is false, returns error JSON
        if movie["Response"] == "False":
            print(error_message)
            return default_json_error
        else:
            return movie

    except:
        # If request fails, prints an error alert in console and
        #returns error JSON
        print(error_message)
        return default_json_error
