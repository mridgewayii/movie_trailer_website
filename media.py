import webbrowser

#Define Movie Class
class Movie():
	#Set order of strings to be passed to this class
    def __init__(self, movie_title, movie_storyline, poster_image, 
				 trailer_youtube):
	#Initialize variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
		
	#Define show_trailer and open new browser or tab in existing instance
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
