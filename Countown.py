#! /usr/bin/env python

#imports first
import pygame
from Tkinter import *
import time
import sys
import os
from pygame.locals import *
import RPi.GPIO as GPIO
from gpiozero import LED, Button
from time import sleep
GPIO.setmode(GPIO.BCM)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/home/pi/Downloads/5 Minute final for machine.mp3')



#first timer method to start the game
def start ():
        pygame.mixer.music.play()
        global minute
        global second
        global resetflag
        global pausegame
        global fontsize
        while pausegame == False:
                if resetflag == False:
                    minute = 5
                    second = 0
                    resetflag = True
                if second >= 10 and minute >=10:
                    var.set("%s" % minute + ":%s" % second)
                if second >= 0 and second < 10 and minute >= 10:
                    var.set("%s" % minute + ":0%s" % second)
                if second >= 10 and minute < 10:
                    var.set("%s" % minute + ":%s" % second)
                if second >= 0 and second < 10 and minute < 10:
                    var.set("%s" % minute + ":0%s" % second)
                if minute == 1 and second == 30:
                    GPIO.output(17, False)
                if minute == 0 and second == 0:
                    GPIO.output(17, True)
                if minute == 0 and second <= -1:
                    if X  == 11:
                        var.set("GAME OVER")
                        break
                    else:
                        static()
                if second == 0 and minute >= 1:
                    minute -= 1
                    second = 60
                second -= 1
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.1)
                root.update()
                time.sleep(.091)
                root.update()

#basic definitions that help the program function.        
       
def reset():
    global X
    if X < 11:
        global resetflag
        resetflag = False
        X += 1
        GPIO.output(17, True)
        GPIO.output(18, False)
        time.sleep(.1)
        GPIO.output(18, True)
        if X == 1:
            flicker1()
        if X == 2:
             flicker2()
        if X == 3:
             flicker3()
        if X == 4:
             flicker4()
        if X == 5:
             flicker5()
        if X == 6:
             flicker6()
        if X == 7:
             flicker7()
        if X == 8:
             flicker8()
        if X == 9:
             flicker9()
        if X == 10:
             flicker10()
        if X == 11:
             flicker11()

def static():
    global pausegame
    while True:
        if pausegame == True:
            if gamestart == False:
                var.set("%s" % minute + ":0%s" % second)
                break
            if gamestart == True:
                var.set("You win!")
                break
        var.set ("1:32")
        time.sleep(.03)
        root.update()
        var.set ("4:17")
        time.sleep(.03)
        root.update()
        var.set ("1:41")
        time.sleep(.03)
        root.update()
        var.set ("4:18")
        time.sleep(.03)
        root.update()
        var.set ("2:52")
        time.sleep(.03)
        root.update()
        var.set ("1:98")
        time.sleep(.03)
        root.update()
        var.set ("3:21")
        time.sleep(.03)
        root.update()
        var.set ("5:68")
        time.sleep(.03)
        root.update()
        var.set ("6:52")
        time.sleep(.03)
        root.update()
        var.set ("2:38")
        time.sleep(.03)
        root.update()
        var.set ("3:54")
        time.sleep(.03)
        root.update()
        var.set ("7:85")
        time.sleep(.03)
        root.update()
        var.set ("3:99")
        time.sleep(.03)
        root.update()
        var.set ("0:70")
        time.sleep(.03)
        root.update()
        var.set ("9:94")
        time.sleep(.03)
        root.update()
        var.set ("5:35")
        time.sleep(.03)
        root.update()
        var.set ("0:22")
        time.sleep(.03)
        root.update()
        var.set ("4:33")
        time.sleep(.03)
        root.update()
        var.set ("8:85")
        time.sleep(.03)
        root.update()
        var.set ("8:43")
        time.sleep(.03)
        root.update()
        var.set ("0:66")
        time.sleep(.03)
        root.update()
        var.set ("1:20")
        time.sleep(.03)
        root.update()
        var.set ("6:62")
        time.sleep(.03)
        root.update()
        var.set ("8:48")
        time.sleep(.03)
        root.update()
        var.set ("8:37")
        time.sleep(.03)
        root.update()
        var.set ("7:34")
        time.sleep(.03)
        root.update()
        var.set ("2:87")
        time.sleep(.03)
        root.update()
        var.set ("4:31")
        time.sleep(.03)
        root.update()
        var.set ("2:23")
        time.sleep(.03)
        root.update()
        var.set ("0:75")
        time.sleep(.03)
        root.update()
        var.set ("9:92")
        root.update()
    
def wingame():
    global pausegame
    pausegame = True
    var.set("You win!")
    pygame.mixer.music.load("/home/pi/python_games/tetrisc.mid")
    pygame.mixer.music.play()
    GPIO.output(27, False)
    #start()

def newgame():
    global X
    global minute
    global second
    global gamestart
    global pausegame
    GPIO.output(chan_list, True)
    pygame.mixer.music.load("/home/pi/python_games/beep1.ogg")
    pygame.mixer.music.play()
    X = 0
    minute = 5
    second = 0
    var.set("%s" % minute + ":0%s" % second)
    gamestart = False
    pausegame = True

    

def makeentry(root, caption, width=20):
    entry = Entry(root)
    entry.pack(side=BOTTOM, padx=10)
    return entry

def enter(event):
    check_password()   

def check_password():
    global gamestart
    global pausegame
    if (passcode.get() == '481632'and gamestart == False):
        passcode.delete(0, 'end')
        gamestart = True
        pausegame = False
        start()
        return
    if (passcode.get() == '481632'and gamestart == True):
        passcode.delete(0, 'end')
        reset()
    if (passcode.get() == 'missionsupportgoodbye'):
        quitout()
    if (passcode.get() == 'misionsupportpoweroff'):
        power()
    if (passcode.get() == '81614123'):
        wingame()
        passcode.delete(0, 'end')
    if (passcode.get() == 'missionsupportnewgame'):
        passcode.delete(0, 'end')
        newgame()
    else:
        passcode.delete(0, 'end')

#def button_start():
 #   global gamestart
  #  for event in pygame.event.get.pressed():
   #     if gamestart == False:
    #        if event.type == pygame.KEYDOWN:
     #           if event.key == pygame.KEY_LEFT:
      #              gamestart = True
       #             start()

#while presently unused, the progam has the ability to pause the timer
#and to add more time if prompted.
def addtime():
    global minute
    minute += 1
    
def pause():
    global pausegame
    if pausegame == False:
        pausegame = True
    else:
        pausegame = False
        start()
        
def power():
    GPIO.cleanup()
    os._shutdown(0)
    
def quitout():
    GPIO.cleanup()
    os._exit(0)

#these are the eleven phases of the game as the players continually reset.
#named for the flickering of the GPIO lights connected to the pi.
def flicker1():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            sleep(.04)
            root.update()
            twentysix()
            sleep(.06)
            root.update()
            twentysix()
            sleep(.05)
            root.update()
            sleep(.09)
            root.update()
            sleep(.05)
            twentysix()
            sleep(.03)
            root.update()
            sleep(.04)
            root.update()
            sleep(.18)
            root.update()
            sleep(.18)
        
def flicker2():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            twenty()
            sleep(.04)
            root.update()
            twentysix()
            root.update()
            sleep(.06)
            root.update()
            twentysix()
            root.update()
            sleep(.05)
            root.update()
            sleep(.09)
            root.update()
            twenty()
            root.update()
            sleep(.05)
            root.update()
            twenty()
            root.update()
            sleep(.03)
            root.update()
            sleep(.04)
            root.update()
            sleep(.18)
            root.update()
        
def flicker3():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            twenty()
            root.update()
            sleep(.04)
            root.update()
            twentysix()
            root.update()
            sleep(.06)
            root.update()
            twentysix()
            root.update()
            sleep(.05)
            root.update()
            nine()
            root.update()
            twenty()
            root.update()
            sleep(.05)
            root.update()
            twenty()
            root.update()
            sleep(.03)
            root.update()
            nine()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker4():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            twenty()
            root.update()
            sleep(.04)
            root.update()
            twentysix()
            root.update()
            sleep(.06)
            root.update()
            twentysix()
            root.update()
            sleep(.05)
            root.update()
            nine()
            root.update()
            twenty()
            root.update()
            sleep(.05)
            root.update()
            twenty()
            root.update()
            sleep(.03)
            root.update()
            nine()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker5():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            twenty()
            root.update()
            sleep(.02)
            root.update()
            twentysix()
            root.update()
            sixteen()
            root.update()
            sleep(.05)
            root.update()
            twentysix()
            root.update()
            sleep(.03)
            root.update()
            nine()
            root.update()
            twenty()
            root.update()
            sleep(.03)
            root.update()
            twenty()
            root.update()
            sleep(.01)
            root.update()
            sixteen()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker6():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            twenty()
            root.update()
            sleep(.02)
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            sleep(.05)
            root.update()
            twentysix()
            root.update()
            sleep(.03)
            root.update()
            nine()
            root.update()
            twelve()
            root.update()
            sleep(.03)
            root.update()
            twenty()
            root.update()
            sleep(.01)
            root.update()
            sixteen()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker7():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            thirteen()
            root.update()
            twenty()
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            sleep(.05)
            root.update()
            thirteen()
            root.update()
            twentysix()
            root.update()
            nine()
            root.update()
            twelve()
            root.update()
            twenty()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker8():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            thirteen()
            root.update()
            twentyfive()
            root.update()
            twenty()
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            sleep(.05)
            root.update()
            thirteen()
            root.update()
            twentysix()
            root.update()
            nine()
            root.update()
            twelve()
            root.update()
            nine()
            root.update()
            sleep(.04)
            root.update()
        
def flicker9():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            thirteen()
            root.update()
            twentyfive()
            root.update()
            twenty()
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            thirteen()
            root.update()
            twentysix()
            root.update()
            nine()
            root.update()
            twelve()
            root.update()
            nine()
            root.update()
            nineteen()
            root.update()
        
def flicker10():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            thirteen()
            root.update()
            twentyfive()
            root.update()
            twenty()
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            thirteen()
            root.update()
            twentysix()
            root.update()
            eleven()
            root.update()
            twelve()
            root.update()
            nine()
            root.update()
            nineteen()
            root.update()
        
def flicker11():
    pygame.mixer.music.play()
    global minute
    global second
    global resetflag
    global pausegame
    global fontsize
    while pausegame == False:
            if resetflag == False:
                minute = 5
                second = 0
                resetflag = True
            if second >= 10 and minute >=10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute >= 10:
                var.set("%s" % minute + ":0%s" % second)
            if second >= 10 and minute < 10:
                var.set("%s" % minute + ":%s" % second)
            if second >= 0 and second < 10 and minute < 10:
                var.set("%s" % minute + ":0%s" % second)
            if minute == 1 and second == 30:
                GPIO.output(17, False)
            if minute == 0 and second == 0:
                GPIO.output(17, True)
            if minute == 0 and second == -1:
                if X  == 11:
                    var.set("GAME OVER")
                    break
                else:
                    static()
            if second == 0 and minute >= 1:
                minute -= 1
                second = 60
            second -= 1
            thirteen()
            root.update()
            twentyfive()
            root.update()
            twenty()
            root.update()
            twelve()
            root.update()
            sixteen()
            root.update()
            twentyone()
            root.update()
            twentysix()
            root.update()
            eleven()
            root.update()
            twelve()
            root.update()
            nine()
            root.update()
            nineteen()
            root.update()

#these control the individual flicker patterns of each light.
#easy to change and customize, but each one must add up to .09 seconds.
def twentyone():
    GPIO.output(21, False)
    sleep(.03)
    GPIO.output(21, True)
    sleep(.03)
    GPIO.output(21, False)
    sleep(.03)
    GPIO.output(21, True)
    root.update()
    
def eleven():
    GPIO.output(16, True)
    GPIO.output(11, False)
    sleep(.015)
    GPIO.output(11, True)
    sleep(.02)
    GPIO.output(11, False)
    sleep(.015)
    GPIO.output(11, True)
    sleep(.02)
    GPIO.output(11, False)
    sleep(.02)
    GPIO.output(11, True)
    root.update()

def nineteen():
    GPIO.output(19, False)
    sleep(.01)
    GPIO.output(19, True)
    sleep(.01)
    GPIO.output(19, False)
    sleep(.01)
    GPIO.output(19, True)
    sleep(.01)
    GPIO.output(19, False)
    sleep(.01)
    GPIO.output(19, True)
    sleep(.01)
    GPIO.output(19, False)
    sleep(.01)
    GPIO.output(19, True)
    sleep(.01)
    GPIO.output(19, False)
    sleep(.01)
    GPIO.output(19, True)
    root.update()
    
def twentyfive():
    GPIO.output(25, False)
    GPIO.output(16, True)
    sleep(.04)
    GPIO.output(25, True)
    sleep(.05)
    GPIO.output(16, False)
    root.update()
    
def thirteen():
    GPIO.output(13, False)
    sleep(.09)
    GPIO.output(13, True)
    root.update()
    
def twelve():
    GPIO.output(12, False)
    sleep(.045)
    GPIO.output(12, True)
    sleep(.045)
    root.update()

def sixteen():
    GPIO.output(16, False)
    sleep(.03)
    GPIO.output(16, True)
    sleep(.03)
    GPIO.output(16, False)
    sleep(.03)
    root.update()

def nine():
    GPIO.output(9, False)
    sleep(.05)
    GPIO.output(9, True)
    sleep(.04)
    root.update()

def twenty():
    GPIO.output(20, False)
    sleep(.02)
    GPIO.output(20, True)
    sleep(.06)
    GPIO.output(20, False)
    sleep(.01)
    GPIO.output(20, True)
    root.update()

def twentysix():
    GPIO.output(26, False)
    sleep(.025)
    GPIO.output(26, True)
    sleep(.025)
    GPIO.output(26, False)
    sleep(.04)
    GPIO.output(26, True)
    root.update()

#global variables
    
resetflag = True
X = 0
gamestart = False
minute = 5
second = 0
pausegame = False

#The GUI
root = Tk()
var = StringVar()
root.geometry('1000x800')
parent = Frame(root, padx=10, pady= 20, bg = '#000000')
parent.pack(fill=BOTH, expand=True, side = BOTTOM)

passcode = makeentry(parent, "Input code, then press enter")

passcode.bind('<Return>', enter)
passcode.focus_set()

label = Label(root, padx=800, pady=200, textvariable = var, bg = "#000000", font=("DS-Digital", 150), fg ="red")
var.set("%s" % minute + ":0%s" % second)
label.pack(side =TOP)

root.config(cursor="none")

#comment or uncomment these three to toggle fullscreen.
#Highly recommended that fullscreen is disabled while tampering with program.
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))

#GPIO setup. This is the reason the program lags for a second before
#the user interface opens when started.
chan_list = [21,11,19,25,13,12,16,9,20,26,27,18,17]
GPIO.setup(chan_list, GPIO.OUT)
sleep(1)
GPIO.output(chan_list, True)


parent.mainloop()