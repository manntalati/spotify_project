from tkinter import *
from tkinter.simpledialog import askinteger
#import spotify_project
import helper

screen = Tk()

def clear():
    for widget in screen.winfo_children():
        widget.destroy()

def genre():
    clear()

    main_label = Label(screen, text="Genre Selector", height=5, width=50)
    main_label.place(x=35, y=0)
    blank = Label(screen, text='')
    blank.grid(row=0, column=1)
    rap_button = Button(screen, text="Rap", width=25, height=3)
    hip_hop_button = Button(screen, text="Hip Hop", width=25, height=3)
    rock_button = Button(screen, text="Rock", width=25, height=3)
    pop_button = Button(screen, text="Pop", width=25, height=3)
    sleep_button = Button(screen, text="Sleep", width=25, height=3)
    modern_bollywood_button = Button(screen, text="Modern Bollywood", width=25, height=3)
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
    happy_button = Button(screen, text="Happy", width=25, height=3)
    sad_button = Button(screen, text="Sad", width=25, height=3)
    anger_button = Button(screen, text="Anger", width=25, height=3)
    energetic_button = Button(screen, text="Energetic", width=25, height=3)
    relaxation_button = Button(screen, text="Relaxation", width=25, height=3)
    triumph_button = Button(screen, text="Triumph", width=25, height=3)
    happy_button.grid(row=0, column=0, padx=10, pady=(70, 20), sticky = "nsew")
    sad_button.grid(row=0, column=2, padx=10, pady=(70, 20), sticky = "nsew")
    anger_button.grid(row=1, column=0, padx=10, pady=20, sticky = "nsew")
    energetic_button.grid(row=1, column=2, padx=10, pady=20, sticky = "nsew")
    relaxation_button.grid(row=2, column=0, padx=10, pady=20, sticky = "nsew")
    triumph_button.grid(row=2, column=2, padx=10, pady=20, sticky = "nsew")


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