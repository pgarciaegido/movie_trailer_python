# :movie_camera: Pablo's Movie Trailer Python Site :movie_camera:
Python written website where you can show the trailers of your favourite movies. This is part of a project for Udacity.

![Demo](https://image.ibb.co/er2Xaa/sample.jpg)

### Features
* List of your favoutire movies
* On click, it shows the trailer
* On hover, it shows a short description of the movie
* It displays the average rate on IMDB

### Usage
If you would like to make your own list of favourite movies, you can create your owns on the **enterteinment_center.py** file.
```python
star_wars = media.Movie("Star Wars",  # Movie title
                        "http://pics.filmaffinity.com/starwars.jpg",  # URL to poster pic
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")  # URL to Youtube trailer
```
The description of the movie and the IMDB rating is brought by OMDB API, so is important that the title is correctly spelled. When it comes to those with a non english title, you will probably have to check under what name is it recorded on the db. Do it [here](http://www.omdbapi.com/#examples).

There will be an array / list at the bottom of the file where you have to include all your movies:
```python
movies = [casablanca, the_great_beauty, lalaland] # Include all the instances you have created
```
In order to create the website, you have to run that file.
```sh
$ python enterteinment_center.py
```
### Contributing
If you fancy, you can make a pull request and improve the functionality or even the UI of the site.
Any possible issues, you can report them [here](https://github.com/pgarciaegido/movie_trailer_python/issues).

### Contact
You can contact me on pgarciaegido@gmail.com
