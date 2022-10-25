from pytube import YouTube
import os

from tkinter import *
import tkinter.font as tkFont

def Download (yt_url) :

    url = yt_url

    youtube_video = YouTube(url)

    youtube_video = youtube_video.streams.filter(only_audio=True)[1]

    print(youtube_video)

    output_file = youtube_video.download()

    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)

    print("Successfully downloaded !")

def Submit () :

    global yt_url_input
    yt_url = yt_url_input.get()
    yt_url_input.delete(0,END)

    Download (yt_url)

root = Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

input_label = Label(root, text="Enter Youtube URL :", font=fontStyle)
yt_url_input = Entry(root, font=fontStyle)

submit_button = Button(root, text="Submit", command=Submit, font=fontStyle)

input_label.grid(row=0, column=0)
yt_url_input.grid(row=1, column=0)
submit_button.grid(row=2, column=0)

root.mainloop()