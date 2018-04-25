import media
import fresh_tomatoes


def main():
    """ main function for creating the website """

    # create the instances of movies
    
   
    The_BFG  = media.Movie("The BFG",
                            "Then you can imagine",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/The_BFG_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=GZ0Bey4YUGI")  # NOQA

    Taare_Zameen_Par= media.Movie("Taare Zameen Par",
                                   "Every child is special",
                                   "https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",  # NOQA
                                   "https://www.youtube.com/watch?v=tn_2Ie_jtX8")  # NOQA

    Dirty_Politics = media.Movie("Dirty Politics",
                                 "And the game begins",
                                 "https://upload.wikimedia.org/wikipedia/en/f/f1/Dirty_Politics.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=V5v72YRsKqc")  # NOQA

    Jumbo = media.Movie("Jumbo",
                        "Everything gonna be Alrite",
                        "https://upload.wikimedia.org/wikipedia/en/7/7c/Jumbo_hindi.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=m3yaQ-IAPxs")  # NOQA
    
    Baahubali = media.Movie("Baahubali",
                            "The Beginning",
                            "https://upload.wikimedia.org/wikipedia/commons/c/c8/Baahubali.jpg", # NOQA
                            "https://www.youtube.com/watch?v=3NQRhE772b0")  # NOQA
    
    Hichki = media.Movie("Hichki",
                            "A story of women coming dreams",
                            "https://upload.wikimedia.org/wikipedia/commons/8/85/Hichki.jpg", # NOQA
                            "https://www.youtube.com/watch?v=nLSaCFlXn-g")  # NOQA
    
    Pari= media.Movie("Pari",
                            "Not a fairy tale",
                            "https://upload.wikimedia.org/wikipedia/commons/3/32/Pari_2018.jpg", # NOQA
                            "https://www.youtube.com/watch?v=6i2QK6Jd02s")  # NOQA
    
    
   # create a list contains all the movies
    movies = [
    The_BFG,
    Taare_Zameen_Par,
    Dirty_Politics,
    Jumbo,Baahubali,Hichki,Pari]
     

    # pass the list the fresh_tomatoes to create the website
    fresh_tomatoes.open_movies_page(movies)

if __name__== '__main__':
    main()
