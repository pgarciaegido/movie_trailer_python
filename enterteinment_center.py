import media
import fresh_tomatoes

toy_story = media.Movie("Casablanca",
                        "Love history during WW2",
                        "http://pics.filmaffinity.com/casablanca-565828825-large.jpg",
                        "https://www.youtube.com/watch?v=BkL9l7qovsE")

avatar = media.Movie("The great beauty",
                     "Life in decadent modern Rome",
                     "http://pics.filmaffinity.com/la_grande_bellezza-366210175-large.jpg",
                     "https://www.youtube.com/watch?v=uxh3or6zLvE")

lalaland = media.Movie("La La Land",
                       "An idealistic piano player and a frustrated actress fell in love...",
                       "http://www.indiewire.com/wp-content/uploads/2016/08/crhirsww8aad6ty.jpg",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A dreamy writer travels in time in Paris",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

relatos_salvajes = media.Movie("Wild Tales",
                               "Five different stories with only one thing in common: violence",
                               "http://pics.filmaffinity.com/relatos_salvajes-102488639-large.jpg",
                               "https://www.youtube.com/watch?v=3BxE9osMt5U")

la_vaquilla = media.Movie("The heifer",
                          "The adventures of a republican regiment during the spanish civil war",
                          "http://pics.filmaffinity.com/la_vaquilla-561240437-large.jpg",
                          "https://www.youtube.com/watch?v=CWJXYC2tBLc")

# Array holds all the instances of the Movie class.
movies = [toy_story, avatar, lalaland, midnight_in_paris, relatos_salvajes, la_vaquilla]

# The open_movies_page method opens a new tab with the 
fresh_tomatoes.open_movies_page(movies)
