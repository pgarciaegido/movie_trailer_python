import media
import fresh_tomatoes

toy_story = media.Movie("Casablanca",
                        "https://www.youtube.com/watch?v=BkL9l7qovsE")

avatar = media.Movie("The great beauty",
                     "https://www.youtube.com/watch?v=uxh3or6zLvE")

lalaland = media.Movie("La La Land",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")

the_man_from_earth = media.Movie("The man from earth",
                                "https://www.youtube.com/watch?v=9mOIxyRTY5I")

relatos_salvajes = media.Movie("Wild Tales",
                               "https://www.youtube.com/watch?v=3BxE9osMt5U")

volver = media.Movie("Volver",
                     "https://www.youtube.com/watch?v=hp4u67AV8VI")

# Array holds all the instances of the Movie class.
movies = [toy_story, avatar, lalaland, the_man_from_earth, relatos_salvajes, volver]

# The open_movies_page method opens a new tab with the 
fresh_tomatoes.open_movies_page(movies)
