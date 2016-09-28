#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pygame Tutorial - Tanks

import pygame
import time
import random

# Setup the game screen
pygame.init()

# Define RGB colors
white           = (255,255,255)
black           = (0,0,0)
red             = (200,0,0)
light_red       = (255,0,0)

yellow          = (200,200,0)
light_yellow    = (255,255,0)

green           = (34,177,76)
light_green     = (0,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')  # Window title


mainTankX = display_width * 0.9
mainTankY = display_height * 0.9


clock = pygame.time.Clock()

FPS = 15


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True

    message_to_screen("Paused",
                      black,
                      -100,
                      "large")
    message_to_screen("Press C to Continue or Q to Quit.",
                      black,
                      25)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])


def game_intro():
    # Intro Screen
    intro = True

    while intro:

        # Exit the game if the X is clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Close the Intro screen if "C" is pressed.
            # Continues to gameLoop().
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                # Exit is "Q" is pressed.
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective is to shoot and destroy",
                          black,
                          -30)
        message_to_screen("the enemy tanks before they destroy you.",
                          black,
                          10)
        message_to_screen("The more enemies you destroy, the harder they get.",
                          black,
                          50)
        # message_to_screen("Press C to Continue, P to Pause or Q to Quit.",
        #                   black,
        #                   180)


        # Buttons
        cur = pygame.mouse.get_pos()

        if 150+100 > cur[0] > 150 and 500+50 > cur[1] > 500:
            pygame.draw.rect(gameDisplay, light_green, (150,500,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        pygame.draw.rect(gameDisplay, yellow, (350,500,100,50))
        pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        button("Play", 150, 500, 100, 50, green, light_green, action="play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow,
               action="controls")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)




def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight,
                   size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)


def tank(x,y):
    pygame.draw.circle(gameDisplay, black, (int(x),int(y)), 20)


def game_controls():
    # Controls screen
    gcont = True

    while gcont:

        # Exit the game if the X is clicked.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -100,
                          "large")
        message_to_screen("Fire: Spacebar",
                          black,
                          -30)
        message_to_screen("Move Turret: UP and Down arrows",
                          black,
                          10)
        message_to_screen("Move Tank: Left and Right arrows",
                          black,
                          50)
        message_to_screen("Pause: P",
                          black,
                           90)


        # Buttons
        cur = pygame.mouse.get_pos()

        if 150+100 > cur[0] > 150 and 500+50 > cur[1] > 500:
            pygame.draw.rect(gameDisplay, light_green, (150,500,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        pygame.draw.rect(gameDisplay, yellow, (350,500,100,50))
        pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        button("Play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow,
               action="main")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()  # Get mouse position
    click = pygame.mouse.get_pressed()  # Get mouse clicks

    # Define the button boundaries and draw button
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)


def message_to_screen(msg,color,y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():

    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                             size="large")
            message_to_screen("Press C to Continue or Q to Quit",
                              black,
                              y_displace=50,
                             size="medium")

        while gameOver == True:
            # gameDisplay.fill(white)
            pygame.display.update()

            # Exit if the X is clicked
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False

            # Look for C and Q keys
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()  # Pause the game

        gameDisplay.fill(white)
        tank(mainTankX,mainTankY)  # Draw tank
        pygame.display.update()
        clock.tick(FPS)

    # Close pygame and python
    pygame.quit()
    quit()

game_intro()
gameLoop()
