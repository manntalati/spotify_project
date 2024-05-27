from tkinter import *
from tkinter.simpledialog import askinteger
#import spotify_project
import helper

#* GUI TASKS
#TODO: loop through the songs recieved from recommendations and display them through the recommendations function below

screen = Tk()
counter = 0

def clear():
    for widget in screen.winfo_children():
        widget.destroy()

def mood_to_use(mood):
    global user_mood, counter
    counter += 1
    user_mood = mood
    clear()
    if counter > 1:
        recommendations()
    else:
        genre()

def genre_to_use(genre):
    global user_genre, counter
    counter += 1
    user_genre = genre
    clear()
    if counter > 1:
        recommendations()
    else:
        mood()


def genre():
    clear()

    main_label = Label(screen, text="Genre Selector", height=5, width=50)
    main_label.place(x=35, y=0)
    blank = Label(screen, text='')
    blank.grid(row=0, column=1)
    rap_button = Button(screen, text="Rap", command=lambda click="rap": genre_to_use(click), width=25, height=3)
    hip_hop_button = Button(screen, text="Hip Hop", command=lambda click="hip hop": genre_to_use(click), width=25, height=3)
    rock_button = Button(screen, text="Rock", command=lambda click="rock": genre_to_use(click), width=25, height=3)
    pop_button = Button(screen, text="Pop", command=lambda click="pop": genre_to_use(click), width=25, height=3)
    sleep_button = Button(screen, text="Sleep", command=lambda click="sleep": genre_to_use(click), width=25, height=3)
    modern_bollywood_button = Button(screen, text="Modern Bollywood", command=lambda click="modern bollywood": genre_to_use(click), width=25, height=3)
    rap_button.grid(row=0, column=0, padx=10, pady=(70, 20), sticky = "nsew")
    hip_hop_button.grid(row=0, column=2, padx=10, pady=(70, 20), sticky = "nsew")
    rock_button.grid(row=1, column=0, padx=10, pady=20, sticky = "nsew")
    pop_button.grid(row=1, column=2, padx=10, pady=20, sticky = "nsew")
    sleep_button.grid(row=2, column=0, padx=10, pady=20, sticky = "nsew")
    modern_bollywood_button.grid(row=2, column=2, padx=10, pady=20, sticky = "nsew")

def mood():
    clear()

    main_label = Label(screen, text="Mood Selector", height=5, width=50)
    main_label.place(x=35, y=0)
    blank = Label(screen, text='')
    blank.grid(row=0, column=1)
    happy_button = Button(screen, text="Happy", command=lambda click="happy": mood_to_use(click), width=25, height=3)
    sad_button = Button(screen, text="Sad", command=lambda click="sad": mood_to_use(click), width=25, height=3)
    anger_button = Button(screen, text="Anger", command=lambda click="anger": mood_to_use(click), width=25, height=3)
    energetic_button = Button(screen, text="Energetic", command=lambda click="energetic": mood_to_use(click), width=25, height=3)
    relaxation_button = Button(screen, text="Relaxation", command=lambda click="relaxation": mood_to_use(click), width=25, height=3)
    triumph_button = Button(screen, text="Triumph", command=lambda click="triumph": mood_to_use(click), width=25, height=3)
    happy_button.grid(row=0, column=0, padx=10, pady=(70, 20), sticky = "nsew")
    sad_button.grid(row=0, column=2, padx=10, pady=(70, 20), sticky = "nsew")
    anger_button.grid(row=1, column=0, padx=10, pady=20, sticky = "nsew")
    energetic_button.grid(row=1, column=2, padx=10, pady=20, sticky = "nsew")
    relaxation_button.grid(row=2, column=0, padx=10, pady=20, sticky = "nsew")
    triumph_button.grid(row=2, column=2, padx=10, pady=20, sticky = "nsew")

def recommendations():
    count = 1
    #take in the valence, energy, and danceability from spotify_project and spit back out the recommendations
    main_label = Label(screen, text="Top 5 Recommended Songs Based on Genre and Mood", height=5, width=50)
    main_label.place(x=35, y=0)
    blank = Label(screen, text='')
    album_label = Label(screen, text='Album: ')
    artist_label = Label(screen, text='Artist: ')
    song_label = Label(screen, text='Song: ')
    #for loop going through the 5 songs
    label = Label(screen, text=f"Recommendation #{count}", height=5, width=50)
    label.place(x=35, y=50)
    album = Label(screen, text='UTOPIA')
    artist = Label(screen, text='Travis Scott')
    song = Label(screen, text='HYAENA')
    blank.grid(row=0, column=1)
    album_label.grid(row=1, column=0, padx=(100, 10), pady=(110, 20))
    artist_label.grid(row=2, column=0, padx=(100, 10), pady=20)
    song_label.grid(row=3, column=0, padx=(100, 10), pady=20)
    album.grid(row=1, column=2, padx=(100, 10), pady=(110, 20))
    artist.grid(row=2, column=2, padx=(100, 10), pady=20)
    song.grid(row=3, column=2, padx=(100, 10), pady=20)

def main():
    screen.title("Spotify Song Recommender")
    screen.geometry("420x420")
    main_label = Label(screen, text="Welcome to the Spotify Song Recommender!", height=5, width=50)
    main_label.place(x=35, y=0)
    genre_button = Button(screen, text="Genre", command=genre, width=25, height=3)
    mood_button = Button(screen, text="Mood", command=mood, width=25, height=3)
    genre_button.grid(row=1, column=0, padx=10, pady=50, sticky = "nsew")
    mood_button.grid(row=1, column=2, padx=10, pady=50, sticky = "nsew")
    blank = Label(screen, text='')
    blank.grid(row=0, column=1)

    screen.mainloop()


main()
print(user_genre)
print(user_mood)