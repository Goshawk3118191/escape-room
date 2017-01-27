#! /usr/bin/env python

import pygame
from Tkinter import *
import time
import os
import sys
from pygame.locals import *
pygame.init()
pygame.mixer.init()

def maketext(root, caption, width=20):
    text = Text(root, cursor = "none", bg = "black", fg = "Lime", font = "Helvetica 30", insertontime = 600, insertofftime = 300, insertbackground = "Lime")
    text.pack(side=BOTTOM, padx=10)
    return text
      
def enter(event):
    global A
    pygame.mixer.music.load("/home/pi/Downloads/M3- Message Alert.mp3")
    pygame.mixer.music.play()
    if textbox.get("1.0", 'end-1c') == "goodbye":
        os._exit(0)
    if textbox.get("1.0", 'end-1c') == "powerdown":
         os._shutdown(0)
    else:
        A += 1
    
def keystroke1(event):
    pygame.mixer.music.load("/home/pi/Downloads/M3 ambiant.mp3")
    pygame.mixer.music.play()
    
def keystroke2(event):
    pygame.mixer.music.load("/home/pi/Downloads/M3- Type 1.mp3")
    pygame.mixer.music.play()
    
def keystroke3(event):
    pygame.mixer.music.load("/home/pi/Downloads/M3- Type2.mp3")
    pygame.mixer.music.play()
    
def keystroke4(event):
    pygame.mixer.music.load("/home/pi/Downloads/M3- Type3.mp3")
    pygame.mixer.music.play()
    
def keystroke5(event):
    pygame.mixer.music.load("/home/pi/Downloads/M3- Typebeep.mp3")
    pygame.mixer.music.play()

def quitout(event):
    os._exit(0)
    
#def enter(event):

A = 1
root = Tk()
root.title('Ninja Escape Cluegiving')
parent = Frame(root,cursor = "none", padx=10, pady= 20, bg = '#000000')
parent.pack(fill=BOTH, expand=True, side = BOTTOM)

#textbox.bind('<Return>', enter)


root.config(cursor="none")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))


textbox = maketext(parent, "Input code, then press enter")
textbox.focus_set()
textbox.bind('<Return>', enter)
textbox.bind('<a>', keystroke2)
textbox.bind('<b>', keystroke2)
textbox.bind('<c>', keystroke3)
textbox.bind('<d>', keystroke4)
textbox.bind('<e>', keystroke5)
textbox.bind('<f>', keystroke3)
textbox.bind('<g>', keystroke2)
textbox.bind('<h>', keystroke3)
textbox.bind('<i>', keystroke4)
textbox.bind('<j>', keystroke4)
textbox.bind('<k>', keystroke2)
textbox.bind('<l>', keystroke2)
textbox.bind('<m>', keystroke3)
textbox.bind('<n>', keystroke4)
textbox.bind('<o>', keystroke3)
textbox.bind('<p>', keystroke4)
textbox.bind('<q>', keystroke2)
textbox.bind('<r>', keystroke3)
textbox.bind('<s>', keystroke4)
textbox.bind('<t>', keystroke2)
textbox.bind('<u>', keystroke3)
textbox.bind('<v>', keystroke2)
textbox.bind('<w>', keystroke3)
textbox.bind('<x>', keystroke4)
textbox.bind('<y>', keystroke4)
textbox.bind('<z>', keystroke2)
textbox.bind('<A>', keystroke2)
textbox.bind('<B>', keystroke3)
textbox.bind('<C>', keystroke4)
textbox.bind('<D>', keystroke3)
textbox.bind('<E>', keystroke4)
textbox.bind('<F>', keystroke2)
textbox.bind('<G>', keystroke3)
textbox.bind('<H>', keystroke4)
textbox.bind('<I>', keystroke2)
textbox.bind('<J>', keystroke3)
textbox.bind('<K>', keystroke2)
textbox.bind('<L>', keystroke3)
textbox.bind('<M>', keystroke4)
textbox.bind('<N>', keystroke4)
textbox.bind('<O>', keystroke2)
textbox.bind('<P>', keystroke2)
textbox.bind('<Q>', keystroke3)
textbox.bind('<R>', keystroke4)
textbox.bind('<S>', keystroke3)
textbox.bind('<T>', keystroke4)
textbox.bind('<U>', keystroke2)
textbox.bind('<V>', keystroke3)
textbox.bind('<W>', keystroke4)
textbox.bind('<X>', keystroke2)
textbox.bind('<Y>', keystroke3)
textbox.bind('<Z>', keystroke2)
textbox.bind('<space>', keystroke3)
for i in xrange(10):
    textbox.bind(str(i), keystroke4)


parent.mainloop()