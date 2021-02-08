import requests
import pprint
import tkinter as tk
import random



# Luodaan sanakirja Genrejen ID:Tä varten
moviedict = {
    "Action": 28,
    "Adventure": 12,
    "Animated": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37
}



#Haetaan rajapinnasta elokuvat
def get_genre(genre):
    api_key = "979fa814995200f21b7468fc2f5f23f6"
    genre_id = moviedict.get(genre)
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}/discover/movie"
    endpoint = f"{api_base_url}?api_key={api_key}&with_genres={genre_id}"
    r1 = requests.get(endpoint)
    movies = r1.json()

#Arvotaan miltä sivulta leffa suositus tulee
    page = random.randint(1, movies['total_pages'])
    randmovies_endpoint = f"{api_base_url}?api_key={api_key}&with_genres={genre_id}&page={page}"
    r2 = requests.get(randmovies_endpoint)
    randmovies = r2.json()
    label['text'] = response(randmovies)

#Haetaan satunnaiselta sivulta satunnainen elokuvasuositus ja tulostetaan GUI:ssa nimi, julkaisuvuosi ja juonen tiivistelmä
def response(randmovies):
    rand = random.randint(1, 19)
    mname = randmovies['results'][rand]['original_title']
    rd = randmovies['results'][rand]['release_date']
    ow = randmovies['results'][rand]['overview']

    movie_sug = 'Movie title: %s \nRealease date: %s \nOverview: %s' % (mname, rd, ow)
    return movie_sug



# Luodaan GUI tkintterillä
HEIGHT = 500
WIDTH = 1200

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='logo.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

options = tk.StringVar()
options.set("Choose genre from the dropdown menu")

#Lista kaikille genreille
genres = [
    "Action",
    "Adventure",
    "Animated",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Music",
    "Mystery",
    "Romance",
    "Science Fiction",
    "TV Movie",
    "Thriller",
    "War",
    "Western"
]

#Pudotusvalikko, jotta ei käyttäjälle ei tule kirjoitusvirheitä
menu = tk.OptionMenu(root, options, *genres)
menu.place(relx=0.15, rely=0.11, relheight=0.07, relwidth=0.5)
#Painike, jolla haetaan suositukset
button = tk.Button(frame, text="Get movie suggestion!", font=30, command=lambda: get_genre(options.get()))
button.place(relx=0.7, relheight=0.9, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
