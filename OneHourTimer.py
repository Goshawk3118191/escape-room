#! /usr/bin/env python

#imports
import pygame
from Tkinter import *
import time
import os
import sys
pygame.mixer.init()

#Definition functions
def start ():
    global minute
    global second
    global pausegame
    pausegame = False
    while pausegame == False:
        root.update()
        if second >= 10 and minute >=10:
            var.set("%s" % minute + ":%s" % second)
        if second >= 0 and second < 10 and minute >= 10:
            var.set("%s" % minute + ":0%s" % second)
        if second >= 10 and minute < 10:
            var.set("0%s" % minute + ":%s" % second)
        if second >= 0 and second < 10 and minute < 10:
            var.set("0%s" % minute + ":0%s" % second)
        if minute == 60 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/Game on final.mp3")
            pygame.mixer.music.play() 
        if minute == 55 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/5minuteshavepassedDS.mp3")
            pygame.mixer.music.play()
        if minute == 50 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/10minutesDS.mp3")
            pygame.mixer.music.play()
        if minute == 40 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/20 minutes passed.mp3")
            pygame.mixer.music.play()
        if minute == 30 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/30 minutes left.mp3")
            pygame.mixer.music.play()
        if minute == 15 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/15 minutes left.mp3")
            pygame.mixer.music.play()
        if minute == 5 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/5 minutes left.mp3")
            pygame.mixer.music.play()
        if minute == 3 and second == 0:
            pygame.mixer.music.load("/home/pi/Downloads/3 minutes left.mp3")
            pygame.mixer.music.play()
        if minute == 1 and second == 30:
            pygame.mixer.music.load("/home/pi/Downloads/90 seconds left.mp3")
            pygame.mixer.music.play()
        if minute == 0 and second == 52:
            pygame.mixer.music.load("/home/pi/Downloads/final countdown-gameover.mp3")
            pygame.mixer.music.play()
        if minute == 0 and second == 0:
            var.set("GAME OVER")
            break
        if second == 0:
            minute -= 1
            second = 60
        second -= 1
        time.sleep(.991)
    
def pause():
    global pausegame
    if pausegame == False:
        pausegame = True
    else:
        pausegame = False
        start()
        
def reset():
    global minute
    global second
    minute = 60
    second = 0
    var.set("%s" % minute + ":0%s" % second)

def quitout():
    os._exit(0)
        
#global variables
    
minute = 60
second = 0
pausegame = False

#Graphical interface
root = Tk()
root.title('Ninja Escape Countdown')
var = StringVar()
parent = Frame(root, padx=10, pady= 20, bg = '#000000')
parent.pack(fill=BOTH, expand=True, side = BOTTOM)

label = Label(root, padx=800, pady=200, textvariable = var, bg = "#000000", font=("DS-Digital", 180), fg ="red")
var.set("%s" % minute + ":0%s" % second)
label.pack(side =TOP)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

#Command buttons
gamestartbutton = Button(parent, borderwidth=4, text="Start the game",font=("Arial", 20), width = 10, height=5,  pady=8, command=start)
gamestartbutton.pack(side=LEFT)

pausebutton = Button(parent, borderwidth=4, text="Pause game", font=("Arial", 20), width = 10, height=5,  pady=8, command=pause)
pausebutton.pack(side=LEFT)

exitbutton = Button(parent, borderwidth=4, text="exit", font=("Arial", 20), width = 10, height=5, pady=8, command=quitout)
exitbutton.pack(side=RIGHT)

resetbutton = Button(parent, borderwidth=4, text="Reset timer", font=("Arial", 20), width = 10, height=5,  pady=8, command=reset)
resetbutton.pack(side=RIGHT)


parent.mainloop()