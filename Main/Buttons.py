import RPi.GPIO as GPIO
from time import sleep
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def buttons():

    button_vals = {17: "1",
                16: "2",
                13: "3",
                6: "4",
                5:"5",
                4: "6",
                26: "7",
                25: "8",
                24: "9",
                22: "<",
                21: "0",
                20: ">",
                27: "Run",
                12: "Lock",
                23: "Read",
                19: "Dist"}

    pins = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19]

    argument_list = []

    RUNNING = True

    while RUNNING:

        for event in pygame.event.get():

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                exit()
            elif (event.type == QUIT):
                exit()
        
        for i in pins:
            
            if GPIO.input(i) == True:
                
                print(button_vals[i])

                if i == 12:

                    RUNNING = False
                    print(argument_list)
                    sleep(0.3)
                    return argument_list

                
                else:

                    argument_list.append(button_vals[i])
                    sleep(0.3)
