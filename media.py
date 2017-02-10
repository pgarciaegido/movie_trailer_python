import webbrowser

class Movie():
    """ The class Movie takes information of your favourite movies in order
        to show them on a generated HTML. It requires three arguments:

        movie_title (str): The title of the movie. Being accurate is important
                    since we are making a request to an API to get further
                    info. Lenguage matters. If you have any doubt, visit
                    http://www.omdbapi.com/ and check if your movie is in
                    the database and under what name.

        movie_poster (str): Input an URL to your favourite poster of the
                     movie. Example: http://awesomemovie.com/poster.jpg

        trailer_youtube (str): Introduce and YouTube URL to the movie
                        trailer_youtube Example:
                        https://www.youtube.com/watch?v=VJBS1ogEVHE """

    def __init__(self, movie_title, movie_poster, trailer_youtube):
        self.title = movie_title
        self.poster = movie_poster
        self.trailer_youtube_url = trailer_youtube
