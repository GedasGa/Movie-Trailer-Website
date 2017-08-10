#!/usr/bin/env python
import fresh_tomatoes
import media

# Creating Movie class instances/objects
toy_story = media.Movie("Inception",
                        "2010",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "PG-13",
                        "146",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

avatar = media.Movie("Avatar",
                     "2009",
                     "A marine on an alien planet.",
                     "PG-13",
                     "162",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

prestige = media.Movie("The Prestige",
                       "2006",
                       "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
                       "PG-13",
                       "130",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=o4gHCmTQDVI")

hunger_games = media.Movie("The Hunger Games",
                           "2012",
                           "A really real reality show.",
                           "PG-13",
                           "142",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

fight_club = media.Movie("Fight Club",
                         "1999",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club.",
                         "R",
                         "139",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1._SX600_SY600_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

pulp_fiction = media.Movie("Pulp Fiction",
                           "1994",
                           "The lives of two mob hit men, a boxer, a wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "R",
                           "154",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")


movies = [toy_story, avatar, prestige, hunger_games, fight_club, pulp_fiction] # Creating a list/array
fresh_tomatoes.open_movies_page(movies)     # Generating a movie trailer webpage with movies[]
