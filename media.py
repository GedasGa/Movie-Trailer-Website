#!/usr/bin/env python
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_year, movie_storyline, movie_rating,
                 movie_lenght, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.lenght = movie_lenght
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) #Open browser and play trailer


#def show_info():
    #Print movie information
