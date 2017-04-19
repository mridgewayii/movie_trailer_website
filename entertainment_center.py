import media
import fresh_tomatoes
#Define data for each movie trailer to be shown on the website.
#(title, narrative, link to artwork, link to video)
#The Star Trek 2009 Movie
star_trek_2009 = media.Movie("Star Trek (2009)", "The prequel to the original "
							 "Star Treck Motion Picture that outlines a young "
							 "James T. Kirk's journey to become the captain of"
							 " the U.S.S. Enterprise", 
							 "https://upload.wikimedia.org/wikipedia/en/9/9f/Star_Trek_movie_logo_2009.jpg",
							 "https://www.youtube.com/watch?v=FTzIaSQwxCU")
#Terminator Genisys
terminator_genisys = media.Movie("Terminator Genisys","Arnold said he would be"
								 " back and this time to protect a young Sarah"
								 " Conner and Kyle Reese",
                     			 "https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG"
                     			 ,"https://www.youtube.com/watch?v=62E4FJTwSuc")
#The Maze Runner
the_maze_runner = media.Movie("The Maze Runner","He doesn't remember where he "
							  "came from.  He only knows he wants out.",
                     		  "https://upload.wikimedia.org/wikipedia/en/d/db/The_Maze_Runner_cover.png"
                     		  ,"https://www.youtube.com/watch?v=AwwbhhjQ9Xk")
#2001 - A Space Odyssey
a_space_odyssey = media.Movie("2001: A Space Odyssey","As man ventures into "
							  "the expanse of space, HAL creates unforeseen "
							  "challenges for the crew",
                     		  "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg"
                     		  ,"https://www.youtube.com/watch?v=XHjIqQBsPjk&t=40s")
#2010 - The Year We Make Contact
the_year_contact = media.Movie("2010: The Year We Make Contact","The search "
							   "for Discovery One and the self-aware HAL",
                     		   "https://upload.wikimedia.org/wikipedia/en/4/4a/2010-poster01.jpg"
                     		   ,"https://www.youtube.com/watch?v=Gyf8QWoL7T0")
#2012
film_2012 = media.Movie("2012","No one was expecting Mother Nature to take "
						"back her land.",
                     	"https://upload.wikimedia.org/wikipedia/en/d/dd/2012_Poster.jpg"
                     	,"https://www.youtube.com/watch?v=sFXGrTng0gQ")
#Set the movies that will be passed to the media file
movies = [star_trek_2009, terminator_genisys, the_maze_runner, a_space_odyssey,
		  the_year_contact, film_2012]
#Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)

