import webbrowser

class Movie():
    """ Constructor takes information of the movie. A title and the trailer url from Youtube. """

    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
