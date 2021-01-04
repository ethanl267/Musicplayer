from tkinter import *
import os
import pygame

window = Tk()
window.title("My playlist")
window.geometry("400x400")
os.chdir("/home//user//Desktop/songs")
mysongs = os.listdir()


playlist = Listbox(window, bg="red", selectmode=SINGLE)

for song in mysongs:
    position = 0
    playlist.insert(position, song)
    position = position + 1


def play():
    pygame.mixer.init()
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pass


def stop():
    pass


button1 = Button(window, text="PLAY", height=1, width=8, command=play)
button1.pack()

button2 = Button(window, text="PAUSE", height=1, width=8, command=pause)
button2.pack()
button3 = Button(window, text="UNPAUSE", height=1, width=8, command=unpause)
button3.pack()

button4 = Button(window, text="STOP", height=1, width=8, command=stop)
button4.pack()

label5 = LabelFrame(window, text="name of song")
var = StringVar()
songnames = Label(window, textvariable=var)
songnames.pack()
playlist.pack(fill="both", expand="yes")

window.mainloop()
