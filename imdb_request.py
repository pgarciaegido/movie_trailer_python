import requests
import json

def get_movie_json(movie):
    title = movie.title.replace(' ', '+').lower()
    try:
        r = requests.get('http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json')
        movie = r.json()
        return movie
    except:
        print('There is been an error')
        return {"imdbID":"", "imdbRating": "N/A"}
