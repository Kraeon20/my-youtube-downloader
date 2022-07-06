from gc import callbacks
from importlib.resources import path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube
import shutil
import webbrowser




#FUNCTIONS
def select_path():
    #allows user to select the path from file manager
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #moves downloaded file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("DOWNLOAD COMPLETE! DOWNLOAD ANOTHER FILE")


    

#screen design
screen =Tk()
title = screen.title("YOUTUBE DOWNLOADER   |   [by: KRAEON]")
canvas = Canvas(screen, width=500, height=500)
canvas.config(background="#980900")
screen.resizable(False, False)
canvas.pack()

#youtube logo
logo_img = PhotoImage(file='great.png')
canvas.create_image(240, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="PASTE THE DOWNLOAD LINK HERE: ", background="#980900", font=("Bauhus 93", 11, BOLD))

#select path for saving the file
path_label = Label(screen, text="SELECT PATH FOR DOWNLOAD HERE: ",background="#980900", font=("Bauhus 93", 11, BOLD))
browse_btn = Button(screen, text="BROWSE", font=("Bauhus 93", 11, BOLD), command=select_path)

#add to window
canvas.create_window(250, 220, window=path_label)
canvas.create_window(250, 260, window=browse_btn)

#adding widgets to window
canvas.create_window(250, 150, window=link_label)
canvas.create_window(250, 180, window=link_field)


#download buttons
download_btn = Button(screen, text="[DOWNLOAD]", background="green", font=BOLD, command=download_file)
#add download button to canvas
canvas.create_window(250, 320, window=download_btn)

#owner
creator = Label(screen, text="MADE BY: [KRAEON] ", background="#980900", font=("Bauhus 93", 11, BOLD))
canvas.create_window(250, 400, window=creator)





#contact

#instagram button
def callback():
    webbrowser.open_new("https://www.instagram.com/kraeo.n/")

#small instagram butoon and "CONTACT ME ON INSTAGRAM" label
instagram = Button(text="CONTACT ME ON INSTAGRAM", command=callback)
canvas.create_window(400, 480, window=instagram)

#small instram logo and postion
insta_img = PhotoImage(file='gram.png')
insta_img = insta_img.subsample(33, 33)
canvas.create_image(295, 480, image=insta_img)



#discord button
def callback():
    webbrowser.open_new("https://www.discordapp.com/users/kraeon#4199")

#small discord butoon and "CONTACT ME ON discord" label
discord = Button(text="CONTACT ME ON DISCORD", command=callback)
canvas.create_window(120, 480, window=discord)


#small discord logo and postion
discord_img = PhotoImage(file='discord.png')
discord_img = discord_img.subsample(25, 25)
canvas.create_image(20, 480, image=discord_img)

screen.mainloop()