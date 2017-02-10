import media
import fresh_tomatoes

# Instances of Movie class, brought from media file

casablanca = media.Movie("Casablanca",
                         "http://pics.filmaffinity.com/casablanca-565828825-large.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=BkL9l7qovsE")

the_great_beauty = media.Movie("The great beauty",
                               "http://pics.filmaffinity.com/la_grande_bellezza-366210175-large.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=uxh3or6zLvE")

lalaland = media.Movie("La La Land",
                       "http://pics.filmaffinity.com/la_la_land-262021831-large.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")

the_man_from_earth = media.Movie("The man from earth",
                                 "http://pics.filmaffinity.com/jerome_bixby_s_the_man_from_earth-512181758-large.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=9mOIxyRTY5I")

relatos_salvajes = media.Movie("Wild Tales",
                               "http://pics.filmaffinity.com/relatos_salvajes-102488639-large.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=3BxE9osMt5U")

volver = media.Movie("Volver",
                     "http://pics.filmaffinity.com/volver-432380780-large.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=hp4u67AV8VI")

# Array holds all the instances of the Movie class.
movies = [casablanca, the_great_beauty, lalaland, the_man_from_earth,
          relatos_salvajes, volver]

# The open_movies_page method opens a new tab with the
fresh_tomatoes.open_movies_page(movies)
