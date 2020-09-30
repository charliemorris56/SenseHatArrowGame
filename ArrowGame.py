from sense_hat import SenseHat
import os
import time
import pygame
from pygame.locals import *
import random

sense = SenseHat()
pygame.init()
pygame.display.set_mode((10, 10))
sense.clear()

def main(): #the main is run first, i didn't need a main i could have just left the code open but this is more tidy
    score = 0
    high_score = 0
    different = True
    game_time = 1 #initializing variables
    playing = True
    
    random_number_text_red = random.randint(0,255)
    random_number_text_green = random.randint(0,255)
    random_number_text_blue = random.randint(0,255)
    random_number_background_red = random.randint(0,255)
    random_number_background_green = random.randint(0,255)
    random_number_background_blue = random.randint(0,255)

    while different:
        for r in range(-150, 150): #I don't want the text and background colours to be too the same or it may confuse the user, this code her is very redundant as I could have just done the text colour minus the background colour and look to see if that number was in the range
            for g in range(-150, 150): #although this is not perfect as the colour displayed is determined in part by proportions
                  for b in range(-150, 150):
                    if random_number_text_red + r == random_number_background_red and random_number_text_green + g == random_number_background_green and random_number_text_blue + b == random_number_background_blue:
                        random_number_text_red = random.randint(0,255)
                        random_number_text_green = random.randint(0,255)
                        random_number_text_blue = random.randint(0,255)
                        different = True
                    else:
                        different = False

    while playing: #this is a big loop in which the game runs
sense.show_message("Choose your game timer", scroll_speed = 0.075, text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue]) 

        if game_time <=9:
            sense.show_letter(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        else:
            sense.show_message(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])

        running = True
        
        while running: #there is some event handling here, which you can use the joystick on the sense hat or just the arrow keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False
                    elif event.key == pygame.K_DOWN and game_time !=1: #i don't want to game timer being less than 0 or it will just run for ever
                        game_time -= 1
                        if game_time <=9: #you can't have multiple letters displayed in show_letter so it changes to a message after 9
                             sense.show_letter(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
                        else:
                            sense.show_message(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
                    elif event.key == pygame.K_UP:
                        game_time += 1
                        if game_time <=9:
                             sense.show_letter(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
                        else:
                            sense.show_message(str(game_time), text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
                    
        sense.show_message("Are you ready?", scroll_speed = 0.075, text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        time.sleep(1)
        sense.show_letter("3", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        time.sleep(1)
        sense.show_letter("2", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        time.sleep(1)
        sense.show_letter("1", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        
        score = game(game_time) #the game function runs here, i get game to return the value of the score
        
        if score > high_score: #for if you want to play the game multiple times on a sitting you can get a high score
            high_score = score
    
        sense.set_rotation(0) #just puts the sense hat back to default layout
        running = True
        
        sense.show_message("Your score was: " + str(score), scroll_speed = 0.075, text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        sense.show_message("Do you want to play again? Y/N", scroll_speed = 0.075, text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
        sense.show_letter("Y", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])

        while running: #some more event handling for if the user wants to play again
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        playing = True
                        sense.show_letter("Y", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])
                    elif event.key == pygame.K_RIGHT:
                        playing = False
                        sense.show_letter("N", text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])      

    sense.show_message("Your high score was: " + str(high_score), scroll_speed = 0.075, text_colour = [random_number_text_red, random_number_text_green, random_number_text_blue], back_colour= [random_number_background_red, random_number_background_green, random_number_background_blue])   

    sense.clear()
    
def game(game_time):
    score = 0
    correct = True
    rotation = [0, 90, 180, 270] #initializing variables
    angle = 0
    angle_check = 0
    pause = 3
    game_time /= 0.95
    red = 0
    
    abc = [225, 100, 0] #arrow background colour, arror_backgronud_colour was a mouth full to put into the 2D array
    acw = [255, 255, 255] #white
    acg = [0, 255, 0] #green
    acr = [255, 0, 0] #red

    arrow_image_white = [ #default white image
    abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
    abc, abc, abc, acw, acw, abc, abc, abc,   #y=1
    abc, abc, acw, acw, acw, acw, abc, abc,   #y=2
    abc, acw, acw, acw, acw, acw, acw, abc,   #y=3
    abc, abc, abc, acw, acw, abc, abc, abc,   #y=4
    abc, abc, abc, acw, acw, abc, abc, abc,   #y=5
    abc, abc, abc, acw, acw, abc, abc, abc,   #y=6
    abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
    ]

    arrow_image_green = [ #the green one
    abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
    abc, abc, abc, acg, acg, abc, abc, abc,   #y=1
    abc, abc, acg, acg, acg, acg, abc, abc,   #y=2
    abc, acg, acg, acg, acg, acg, acg, abc,   #y=3
    abc, abc, abc, acg, acg, abc, abc, abc,   #y=4
    abc, abc, abc, acg, acg, abc, abc, abc,   #y=5
    abc, abc, abc, acg, acg, abc, abc, abc,   #y=6
    abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
    ]

    arrow_image_red = [ #the red one
    abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=1
    abc, abc, acr, acr, acr, acr, abc, abc,   #y=2
    abc, acr, acr, acr, acr, acr, acr, abc,   #y=3
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=4
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=5
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=6
    abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
    ]
    
    while correct:
        if score != 0: #this is a countdown timer so the user knows when the next round is going to start, you could change the value of the pause and the colour gradient would still be great
            for a in range(1, pause):
                time.sleep(pause / 3)
                acg = [255 * a / pause, 255, 255 * a / pause]
                arrow_image_green = [ #the green one
                abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
                abc, abc, abc, acg, acg, abc, abc, abc,   #y=1
                abc, abc, acg, acg, acg, acg, abc, abc,   #y=2
                abc, acg, acg, acg, acg, acg, acg, abc,   #y=3
                abc, abc, abc, acg, acg, abc, abc, abc,   #y=4
                abc, abc, abc, acg, acg, abc, abc, abc,   #y=5
                abc, abc, abc, acg, acg, abc, abc, abc,   #y=6
                abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
                ]
                sense.set_pixels(arrow_image_green)
                
        time.sleep(1)        

        acg = [0, 255, 0]
        arrow_image_green = [ #the green one
        abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
        abc, abc, abc, acg, acg, abc, abc, abc,   #y=1
        abc, abc, acg, acg, acg, acg, abc, abc,   #y=2
        abc, acg, acg, acg, acg, acg, acg, abc,   #y=3
        abc, abc, abc, acg, acg, abc, abc, abc,   #y=4
        abc, abc, abc, acg, acg, abc, abc, abc,   #y=5
        abc, abc, abc, acg, acg, abc, abc, abc,   #y=6
        abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
        ]
        
        angle = random.choice(rotation)
        
        while angle == angle_check: #to make sure that it is not the same rotation twice
            angle_check = angle
            angle = random.choice(rotation)

        angle_check = angle    
        sense.set_rotation(angle)
        sense.set_pixels(arrow_image_white)
        
        correct = False
        game_time *=0.95 #making it so that game runs faster over time, by 5%

        start_time = end_time = time.time()
          
        while end_time - start_time <= game_time and correct == False: #check to see if the objective is complete and the timer is also here
            end_time = time.time()

            red = int(255 - (((end_time - start_time) / game_time) ** 2) * 255)
            if red < 0:
                red = 0
            acr = [255, red, red]
            arrow_image_red = [ #the red one
            abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
            abc, abc, abc, acr, acr, abc, abc, abc,   #y=1
            abc, abc, acr, acr, acr, acr, abc, abc,   #y=2
            abc, acr, acr, acr, acr, acr, acr, abc,   #y=3
            abc, abc, abc, acr, acr, abc, abc, abc,   #y=4
            abc, abc, abc, acr, acr, abc, abc, abc,   #y=5
            abc, abc, abc, acr, acr, abc, abc, abc,   #y=6
            abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
            ]
            sense.set_pixels(arrow_image_red)
              
            x, y, z = sense.get_accelerometer_raw().values()
            x = round(x, 0)
            y = round(y, 0)
            
            if x == -1:
                if angle == 180: #this is where the program know the rotation of the PI
                    score += 1
                    correct = True
                    sense.set_pixels(arrow_image_green)
                    
            elif y == -1:
                if angle == 90:
                    score += 1
                    correct = True
                    sense.set_pixels(arrow_image_green)
                
            elif y == 1:
                if angle == 270:
                    score += 1
                    correct = True
                    sense.set_pixels(arrow_image_green)
                    
            elif x == 1:
                if angle == 0:
                    score += 1
                    correct = True
                    sense.set_pixels(arrow_image_green)
            else:
                correct = False

    acr = [255, 0, 0]
    arrow_image_red = [ #the red one
    abc, abc, abc, abc, abc, abc, abc, abc,   #y=0
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=1
    abc, abc, acr, acr, acr, acr, abc, abc,   #y=2
    abc, acr, acr, acr, acr, acr, acr, abc,   #y=3
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=4
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=5
    abc, abc, abc, acr, acr, abc, abc, abc,   #y=6
    abc, abc, abc, abc, abc, abc, abc, abc    #y=7        
    ]
    sense.set_pixels(arrow_image_red)
    
    time.sleep(3)
    
    return score

main()
