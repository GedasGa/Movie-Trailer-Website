# Movie Trailer Website

**by Gedas Gardauskas**

The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery and movie trailer website. The data is served as a web page allowing visitors to review the movies and watch the trailers:

## What it is and it does

A Python program that produces the HTML for a movie website that displays a number of movies. In this website you can see all the information about the movie. More over, you can click on a movie poster to play its trailer.

#### This project consists for the following files:

- `entertainment_center.py` - main Python script to run the program
- `media.py` - contains the class Movie that stores all information about a movie
- `fresh_tomatoes.py` - creates the HTML file for the website and opens it in  your browser

## Required Libraries and Dependencies

- Python 2.x is required to run this project. The Python executable should be in your default path, which the Python installer should have set.

## Getting started

- Download the project .zip file to you computer and unzip the file or clone this repository to your desktop.
- Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows).
- Navigate to the project directory and type in the following command:
    `python entertainment_center.py`
- Your default browser should launch a new tab displaying the movie trailer website.

    P.S. If you're using Linux or Mac, you might need to set a permission to make this file executable. You can do it using the following command:
    `chmod +x entertainment_center.py`

### Notes from Udacity
- The file `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies.

- Your task is to write a movie class in `media.py`. To do this, think about what the properties of a movie are that need to be encapsulated in a movie object such as movie titles, box art, poster images, and movie trailer URLs. Look at what `open_movies_page()` does with a list of movie objects for hints on how to design your movie class.

- You’ll want to write a constructor for the movie class so that you can create instances of movie. You can now create a list of these movie objects in `entertainment_center.py` by calling the constructor `media.Movie()` to instantiate movie objects. You’ve given movies their own custom data structure by defining the movie class and constructor, and now these objects can be stored in a list data structure. This list of movies is what the `open_movies_page()` function needs as input in order to build the HTML file, so you can display your website.

## Extra features:

- When mouse is hovered over a movie img it displays movie storyline.
- Added the release date to the Movie class, which is also displayed on the website.
- Added the movie rating and lenght to the Movie class, they're also displayed on the website.
- Changed the navigation.
- Added front-awesome CDN.
- Changed Video close img to front-awesome icon.
- Added a sticky footer.
