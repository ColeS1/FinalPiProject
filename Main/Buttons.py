import RPi.GPIO as GPIO
from time import sleep
import pygame

from pygame.locals import ( #Used for any of the instances where buttons are used and we may want to close the window
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def buttons():

    """Returns a list of the buttons pressed from the keypad"""

    button_vals = {         #Dictionary that holds the pin number as a key and the value is what that pin number stands for
                17: "1",
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
                19: "Dist"
                }

    pins = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19] #List of pin numbers

    argument_list = [] #List to eventually return the buttons pressed

    RUNNING = True

    #This while loop will continuously run until the "Lock" button is pressed (therefore making a return statement)

    while RUNNING:

        for event in pygame.event.get(): #Used for any of the instances where buttons are used and we may want to close the window

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                exit()
            elif (event.type == QUIT):
                exit()
        
        for i in pins: #Loops through all of the pins and checks if any are high
            
            if GPIO.input(i) == True:
                
                # print(button_vals[i]) This is for testing buttons pushed

                if i == 12: #If pin 12 (Lock) is pressed, then the list of button pressed will be returned to be dealt within the GUI

                    RUNNING = False

                    # print(argument_list) Used for testing what the entire argument list was

                    sleep(0.3) #Delay used to let program rest for a second
                    return argument_list

                
                else:

                    argument_list.append(button_vals[i]) #Appends whatever button was pressed to the list of arguments
                    sleep(0.3) #Waits so that we don't get like 50 "Forward"s in the list when it's pressed once