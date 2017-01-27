#! /usr/bin/env python

import os
import sys
import pygame
import time
from pygame.locals import *
import RPi.GPIO as GPIO
from gpiozero import LED, Button
GPIO.setmode(GPIO.BCM)
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible(False)
wingame = pygame.image.load('/home/pi/Downloads/execute3').convert()
player = pygame.image.load('/home/pi/Downloads/Ship ImageRed.png').convert()
hyperplayer = pygame.image.load('/home/pi/Downloads/Ship ImageYellow.png').convert()
superplayer = pygame.image.load('/home/pi/Downloads/Ship ImageGreen.png').convert()
reseticon = pygame.image.load('/home/pi/Downloads/RESET.png').convert()
hyperjump = pygame.image.load('/home/pi/Downloads/hyperjump small.png').convert()
hyperjumpup = pygame.image.load('/home/pi/Downloads/hyperjump up').convert()
hyperjumpdown= pygame.image.load('/home/pi/Downloads/hyperhump down').convert()
superjump = pygame.image.load('/home/pi/Downloads/superjump.png').convert()
superjumpup = pygame.image.load('/home/pi/Downloads/superjump up').convert()
superjumpdown = pygame.image.load('/home/pi/Downloads/superjump down').convert()
#background = pygame.image.load('/home/pi/whitecircle').convert()
#screen.blit(background, (0, 0))
position = player.get_rect()
position = position.move(440, 350)      
screen.blit(player, position)      
pygame.display.update()
fivebuttons = USEREVENT + 1
pygame.time.set_timer(fivebuttons, 10000000)
A = 0
B = 0
C = 0
D = 0
jump = 0

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, True)

def quitout():
    GPIO.cleanup()
    os._exit(0)

def reset():
    global position
    global player
    global A
    global B
    global C
    global D
    global jump
    A = 0
    B = 0
    C = 0
    D = 0
    jump = 0
    GPIO.output(2, True)
    time.sleep(.1)
    screen.blit(player, position, position) 
    position = player.get_rect()
    screen.fill((0,0,0))
    position = position.move(440, 350)
    screen.blit(player, position)      
    pygame.display.update()
    main()

def endgame():
    global A
    global B
    global C
    global D
    global wingame
    time.sleep(.1)
    screen.fill((0,0,0))
    time.sleep(.1)
    screen.blit(wingame, (160, 275))
    time.sleep(.1)
    pygame.display.update()
    pygame.mixer.music.load("/home/pi/Downloads/Power down Joystick.mp3")
    pygame.mixer.music.play()
    while True:
                for event in pygame.event.get():
                    if event.type == fivebuttons:
                        pygame.time.set_timer(fivebuttons, 10000000)
                        pygame.mixer.music.load("/home/pi/python_games/beep2.ogg")
                        pygame.mixer.music.play()
                        A = 0
                        B = 0
                    if event.type == KEYDOWN:
                        if event.key == K_4:   #blue
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 3:
                                B += 1
                            elif B == 5:
                                B += 1
                            else:
                                B = 0
                        if event.key == K_1:  #white
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 1:
                                B+= 1
                            if B == 4:
                                B += 1
                            if B == 6:
                                B += 1
                            else:
                                B = 0
                        if event.key == K_3: #green
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 0:
                                B += 1
                            else:
                                B = 0
                        if event.key == K_2:  #orange
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 2:
                                B +=1
                            if B == 7:
                                GPIO.output(2, False)
                                time.sleep(1)
                                GPIO.output(2, True)
                            else:
                                B = 0
                        if event.key == K_5:  #red
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            B = 0
                        if event.key == K_LEFT:
                            if A == 0:
                                    A += 1
                            elif A == 4:
                                    A += 1
                            elif A == 8:
                                    quitout()
                            else:
                                    A = 0
                        if event.key == K_UP:
                            if A == 1:
                                    A += 1
                            elif A == 5:
                                    A += 1
                            else:
                                    A = 0
                        if event.key == K_RIGHT:
                            if A == 2:
                                    A += 1
                            elif A == 6:
                                    A += 1
                            elif A == 8:
                                    A += 1
                            elif A == 9:
                                    #shutdown()
                                reset()
                            else:
                                    A = 0
                        if event.key == K_DOWN:
                            if A == 3:
                                    A += 1
                            elif A == 7:
                                    A += 1
                            else:
                                    A = 0
                        if event.key == K_SPACE:
                            if C < 5:
                                C += 1
                            elif C == 5:
                                quitout()
                        if event.key == K_LSHIFT:
                            if D < 5:
                                D += 1
                            elif D == 5:
                                reset()


def main():
    global A
    global B
    global C
    global jump
    global position
    global player
    while True:
        for event in pygame.event.get():
            if event.type == fivebuttons:
                    pygame.time.set_timer(fivebuttons, 10000000)
                    pygame.mixer.music.load("/home/pi/python_games/beep2.ogg")
                    pygame.mixer.music.play()
                    B = 0
            if event.type == KEYUP:
                if event.key == K_8 or event.key == K_7:
                    jump = 0 
                    screen.blit(player, position)
                    pygame.display.update()
            if event.type == KEYDOWN:
                if event.key == K_9:
                    screen.blit(player, position, position) 
                    position = player.get_rect()
                    screen.fill((0,0,0))
                    screen.blit(reseticon, (275,275))
                    position = position.move(440, 350)
                    pygame.display.update()
                    time.sleep(.6)
                    screen.fill((0,0,0))
                    screen.blit(player, position)      
                    pygame.display.update()
                if event.key == K_8:
                    jump = 1
                    screen.blit(hyperplayer,position)
                    pygame.display.update()
                if event.key == K_7:
                    jump = 2
                    screen.blit(superplayer,position)
                    pygame.display.update()
                if jump == 0:
                    if event.key == K_LEFT:
                        screen.blit(player, position, position) 
                        position = position.move(-25, 0)
                        screen.blit(player, position)
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Joystick Beep.mp3")
                        pygame.mixer.music.play()
                        if A == 8:
                            A += 1
                        elif A == 9:
                            A += 1
                        elif A == 10:
                            A += 1
                        elif A == 16:
                            A += 1
                        elif A == 17:
                            A += 1
                        elif A == 18:
                            A += 1
                        elif A == 19:
                            A += 1
                            #os._exit(0)
                            #os.system("poweroff")
                        else:
                            A = 0
                    elif event.key == K_UP:
                        screen.blit(player, position, position) 
                        position = position.move(25, 0)     
                        screen.blit(player, position)      
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Joystick Beep.mp3")
                        pygame.mixer.music.play()
                        if A == 0:
                            A += 1
                        elif A == 1:
                            A += 1
                        else:
                            A = 0
                    elif event.key == K_RIGHT:
                        screen.blit(player, position, position) 
                        position = position.move(0, -25)     
                        screen.blit(player, position)      
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Joystick Beep.mp3")
                        pygame.mixer.music.play()
                        if A == 2:
                            A += 1
                        elif A == 3:
                            A += 1
                        elif A == 4:
                            A += 1
                        elif A == 5:
                            A += 1
                        elif A == 6:
                            A += 1
                        elif A == 7:
                            A += 1
                        elif A == 11:
                            A += 1
                        elif A == 12:
                            A += 1
                        elif A == 13:
                            A += 1
                        elif A == 14:
                            A += 1
                        elif A == 21:
                            A += 1
                        elif A == 22:
                            A += 1
                        elif A == 23:
                            A += 1
                        elif A == 24:
                            A += 1
                        elif A == 25:
                            A += 1
                        else:
                            A = 0
                    elif event.key == K_DOWN:
                        screen.blit(player, position, position) 
                        position = position.move(0, 25)     
                        screen.blit(player, position)      
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Joystick Beep.mp3")
                        pygame.mixer.music.play()
                        A = 0
                if jump == 1:
                    if event.key == K_LEFT:
                        screen.blit(player, position, position)
                        position = position.move(-83, 0)
                        position = position.move(-211, 0)
                        screen.blit(hyperjump, position)
                        position = position.move(-83, 0)
                        screen.blit(hyperplayer, position)
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Hyperjump Final.mp3")
                        pygame.mixer.music.play()
                        A = 0
                    elif event.key == K_UP:
                        screen.blit(player, position, position)
                        position = position.move(83, 0)
                        screen.blit(hyperjump, position)
                        position = position.move(294,0)
                        screen.blit(hyperplayer, position)     
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Hyperjump Final.mp3")
                        pygame.mixer.music.play()
                        if A == 15:
                            A += 1
                        else:
                            A = 0
                    elif event.key == K_RIGHT:
                        screen.blit(player, position, position) 
                        position = position.move(0, -294)
                        screen.blit(hyperjumpup, position)
                        position = position.move(0, -83)
                        screen.blit(hyperplayer, position)     
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Hyperjump Final.mp3")
                        pygame.mixer.music.play()
                        A = 0
                    elif event.key == K_DOWN:
                        screen.blit(player, position, position)
                        position = position.move(0, 83)
                        screen.blit(hyperjumpdown, position)
                        position = position.move(0, 294)
                        screen.blit(hyperplayer, position)    
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Hyperjump Final.mp3")
                        pygame.mixer.music.play()
                        if A == 20:
                            A += 1
                        else:
                            A = 0
                    if event.key == K_7:
                        jump = 0
                        screen.blit(player, position)
                        pygame.display.update()
                if jump == 2:
                    if event.key == K_LEFT:
                        screen.blit(player, position, position)
                        position = position.move(-83, 0)
                        position = position.move(-566, 0)
                        screen.blit(superjump, position)
                        position = position.move(-83, 0)
                        screen.blit(superplayer, position)
                        pygame.display.update()
                        if A == 26:
                            endgame()
                            break
                        else:
                            A = 0
                            pygame.mixer.music.load("/home/pi/Downloads/Superjump Final.mp3")
                            pygame.mixer.music.play()
                    elif event.key == K_UP:
                        screen.blit(player, position, position)
                        position = position.move(83, 0)
                        screen.blit(superjump, position)
                        position = position.move(649, 0)     
                        screen.blit(superplayer, position)
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Superjump Final.mp3")
                        pygame.mixer.music.play()
                        A = 0
                    elif event.key == K_RIGHT:
                        screen.blit(player, position, position)
                        position = position.move(0, -649)
                        screen.blit(superjumpup, position)
                        position = position.move(0, -83)
                        screen.blit(superplayer, position)
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Superjump Final.mp3")
                        pygame.mixer.music.play()
                        A = 0
                    elif event.key == K_DOWN:
                        screen.blit(player, position, position)
                        position = position.move(0, 83)
                        screen.blit(superjumpdown, position)
                        position = position.move(0, 649)
                        screen.blit(superplayer, position)
                        pygame.display.update()
                        pygame.mixer.music.load("/home/pi/Downloads/Superjump Final.mp3")
                        pygame.mixer.music.play()
                        A = 0
                    if event.key == K_8:
                        jump = 0
                        screen.blit(player, position)
                        pygame.display.update()
                if event.key == K_4:   #blue
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 3:
                                B += 1
                            elif B == 5:
                                B += 1
                            else:
                                B = 0
                if event.key == K_1:  #white
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 1:
                                B+= 1
                            if B == 4:
                                B += 1
                            if B == 6:
                                B += 1
                            else:
                                B = 0
                if event.key == K_3: #green
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 0:
                                B += 1
                            else:
                                B = 0
                if event.key == K_2:  #orange
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            if B == 2:
                                B +=1
                            if B == 7:
                                GPIO.output(2, False)
                                time.sleep(1)
                                GPIO.output(2, True)
                            else:
                                B = 0
                if event.key == K_5:  #red
                            pygame.time.set_timer(fivebuttons, 10000)
                            pygame.mixer.music.load("/home/pi/Downloads/light puzzle beep sound.mp3")
                            pygame.mixer.music.play()
                            B = 0
                if event.key == K_SPACE:
                    if C < 5:
                        C += 1
                    elif C == 5:
                        quitout()
        pygame.display.update()
        pygame.time.delay(100)
        
main()