#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pygame Tutorial - Tanks

import pygame
import time
import random

# Setup the game screen
pygame.init()

# Define RGB colors
white       = (255,255,255)
black       = (0,0,0)
red         = (255,0,0)
yellow      = (200,200,0)
green       = (34,177,76)
light_green = (0,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')  # Window title

# icon = pygame.image.load("snakeapple.png")
# pygame.display.set_icon(icon)

# img = pygame.image.load('snakehead.png')
# appleimg = pygame.image.load('snakeapple.png')

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

        text_to_button("Play", black, 150, 500, 100, 50)
        text_to_button("Controls", black, 350, 500, 100, 50)
        text_to_button("Quit", black, 550, 500, 100, 50)


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
        pygame.display.update()
        clock.tick(FPS)

    # Close pygame and python
    pygame.quit()
    quit()

game_intro()
gameLoop()
