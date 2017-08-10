import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Trailers!</title>

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        .movie-description-layer {
          position: absolute;
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          background: rgba(100, 100, 120, 0.7); /* color of the backgroud with 70% opacity */
          color: #fff;  /* text color */
          visibility: hidden;
          opacity: 0;
          display: flex;
          align-items: center;
          justify-content: center;

          /* transition effect. not necessary */
          transition: opacity .2s, visibility .2s;
        }
        .img-wrap:hover .movie-description-layer {
          visibility: visible;   /* when mouse is over an img - make text visible */
          opacity: 1;
        }
        .movie-description {
          transition: .2s;
          transform: translateY(1em);
        }
        .img-wrap:hover .movie-description {
          transform: translateY(0);
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // When mouse is over a movie img - write a Storyline to movietext elem
        function myOverFunction(movieId, movieStoryline) {
            movietext = movieId + " Storyline";
            document.getElementById(movietext).innerHTML = movieStoryline;
        }
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <span class="fa fa-times-circle-o fa-inverse fa-2x"></span>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span><link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">
            <span class="fa fa-youtube-play fa-lg" style="color:red;"></span> Movie Trailers
          </a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li class="nav-item">
                <a class="btn btn-block btn-social btn-github" href="https://github.com/GedasGa" target="_blank">
                    <span class="fa fa-github fa-lg"></span> GedasGa
                </a>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container -->
    </nav>
    <div class="container">
      {movie_tiles}
    </div>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}"  data-toggle="modal" data-target="#trailer">
    <div class="img-wrap" id="{movie_title}" onmouseover="myOverFunction(id, '{movie_storyline}')">
        <img src="{poster_image_url}" width="220" height="342">
        <div class="movie-description-layer">
            <p class="movie-description" id="{movie_storyline_p}"></p>
        </div>
    </div>
    <h2>{movie_title}</h2>
    <h4>({movie_year})</h4>
    <h4><span class="label label-default">{movie_rating} | {movie_lenght} min</span></h4>
</div>
'''

# The page's footer
movie_tile_footer = '''
    <div class="container">
        <footer>
            <p class="pull-right"><a href="#">Back to top</a></p>
            <p><span class="fa fa-copyright"> 2017 GedasGa &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
        </footer>
    </div>
  </body>
</html>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            movie_year = movie.year,
            movie_storyline = movie.storyline,
            movie_rating = movie.rating,
            movie_lenght = movie.lenght,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            movie_storyline_p = movie.title + " Storyline"
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + movie_tile_footer)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
