import webbrowser

class Movie():
    """ This class provides a way to store information about movies """

    """ Constructor takes information of the movie. A title, a brief description,
    a poster image and the trailer url from Youtube. """

    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
