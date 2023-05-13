import pygame
from SerialMonitor import *
import pyttsx3
from CONSTANTS import *
from Buttons import *
from time import sleep
import RPi.GPIO as GPIO
from SenderRadio import *

class Line():
    HEIGHT = 50     #Set dimensions for the Line block (With Line 1, 2, and so on)
    WIDTH = 300
    LINE_HEIGHTS = {  #Dictionary of Line 1 - Line 12 string (names) that go with a number (Y value)
                    "Line 1": 50,
                    "Line 2": 100,
                    "Line 3": 150,
                    "Line 4": 200,
                    "Line 5": 250,
                    "Line 6": 300,
                    "Line 7": 350,
                    "Line 8": 400,
                    "Line 9": 450,
                    "Line 10": 500,
                    "Line 11": 550,
                    "Line 12": 600
                    }
    
    def __init__(self, number:int): #Takes in number to assign the name of the Line block
        """Takes in a number to instantiate a line"""
        self.name = f"Line {number}"
        self.height = Line.LINE_HEIGHTS[self.name]  #Acesses the dictionary and assigns where the height would be

        self.rect = pygame.Rect((0, self.height, Line.WIDTH, Line.HEIGHT))

        self.font_surface = FONT.render(self.name, True, WHITE_FONT)   #Pygame to render the font

        self.rect_centered = self.font_surface.get_rect(center=self.rect.center)    #Centers the font surface within the rectangle

class Functions():
    HEIGHT = 50     #Set dimensions for the Function block (With While Loop, Forward, and so on...)
    WIDTH = 300
    FUNCTION_HEIGHTS = {      #Dictionary of Function 1 - Function 12 string (locations) that go with a number (Y value)
                    "Function 1": 50,
                    "Function 2": 100,
                    "Function 3": 150,
                    "Function 4": 200,
                    "Function 5": 250,
                    "Function 6": 300,
                    "Function 7": 350,
                    "Function 8": 400,
                    "Function 9": 450,
                    "Function 10": 500,
                    "Function 11": 550,
                    "Function 12": 600
                    }
    

    
    def __init__(self, line_number: int, analog_value: int):

        """Takes in a number to determine which function block is actually being acted on"""

        self.function_location_name:str = f"Function {line_number}" #Assigns a line number to the function
        self.height = Functions.FUNCTION_HEIGHTS[self.function_location_name] #Assigns the height of the block according to which function we are instantiating

        self.rect = pygame.Rect((300, self.height, Functions.WIDTH, Functions.HEIGHT)) #Makes a rectangle with the given specfications of a Function block

        self.analog_value:int = analog_value #Assigns an analog value to the function


        self.function_name = self.function_determiner() #Returns what the name of the function is based the function_determiner function

        self.font_surface = FONT.render(self.function_name, True, WHITE_FONT) #Similar font set up as the line block
        self.rect_centered = self.font_surface.get_rect(center=self.rect.center) #Similar font setup to center within the rectangle

    def function_determiner(self):
        
        """Uses the assigned analog value and returns what function it is along with the radio letter associated with it"""

        if self.analog_value in range(173, 182):

            self.radio_name = "f"
            return "Go Forward"
        
        elif self.analog_value in range(506, 520):

            self.radio_name = "l"
            return "Turn Left"
        
        elif self.analog_value in range(147, 156):

            self.radio_name = "w"
            return "While Loop"
        
        elif self.analog_value in range(833, 844):

            self.radio_name = "r"
            return "Turn Right"
        
        elif self.analog_value in range(335, 343):

            self.radio_name = "s"
            return "If"
        
        elif self.analog_value in range(72, 80):

            self.radio_name = "o"
            return "For Loop"
        
        elif self.analog_value in range(86, 95):

            self.radio_name = "e"
            return "Go Reverse"
        
        else:

            self.radio_name = " "
            return "None"
        
class Arguments():

    HEIGHT = 50 #Dimensions of argument blocks
    WIDTH = 300

    ARGUMENT_HEIGHTS = { #Dictionary of Arguments 1 - Arguments 12 string (locations) that go with a number (Y value)
                    "Argument 1": 50,
                    "Argument 2": 100,
                    "Argument 3": 150,
                    "Argument 4": 200,
                    "Argument 5": 250,
                    "Argument 6": 300,
                    "Argument 7": 350,
                    "Argument 8": 400,
                    "Argument 9": 450,
                    "Argument 10": 500,
                    "Argument 11": 550,
                    "Argument 12": 600
                    }

    def __init__ (self, line_number, function_name):

        """Takes in a line number to determine the argument location and what the function is"""

        self.argument_location_name = f"Argument {line_number}"
        self.line_number = f"Line {line_number}" #Needed for error determining later on. 
        self.function_name = function_name #Takes in the function name to use later on in error determining.

        self.radio_name = " "
        self.string = "No Arguments" #Sets the default arguments to "No arguments" and will stay that way until changed within the string_of_arguments_determiner function

        self.height = Arguments.ARGUMENT_HEIGHTS[self.argument_location_name] #Similar to the other two blocks and sets the height of where the block will be based off of the location
        self.rect = pygame.Rect((600, self.height, Arguments.WIDTH, Arguments.HEIGHT)) #Similar to the other two blocks where it sets the size and location


    
    def string_of_arguments_determiner(self, list_of_arguments):

        """Sets the information of what will be displayed in the arguments column based on the function name, and handles error handling (along with text to speech to say what is happening)"""

        #Checks if the function is any of the movement functions. If it is, then the user should put in an amount of seconds above 0 or below 100. 
        if self.function_name == "Go Forward" or self.function_name == "Turn Left" or self.function_name == "Turn Right" or self.function_name == "Go Reverse" or self.function_name == "For Loop":
            try:

                if int("".join(list_of_arguments)) in range(0, 100): #Checks if the arguments set in (when joined together and typecasted into an integer) are from 0 to 99 seconds

                    if self.function_name == "For Loop": #Checks if the function is specfically a for loop because the movement blocks and for loops have the same types of arguments (0 - 99)
                        
                        self.string = "Repeat " + "".join(list_of_arguments) + " times" 
                        self.radio_name = "".join(list_of_arguments) #Sets the number as the representation of what is sent to the radio
                        return self.string #Returns a different string value to output because it is a for loop

                    else:
                        
                        self.string = "".join(list_of_arguments) + " seconds"
                        self.radio_name = "".join(list_of_arguments) #Sets the number as the representation of what is sent to the radio
                        return self.string #Else it'll return the integer with seconds at the end
                    

                else: 
                    
                    engine = pyttsx3.init() #If the number is not within the range, then it will show an error that the number is not between 0 and 99
                    VALUE_TOO_HIGH = f"Error on {self.line_number}. Numbers cannot exceed must stay between 0 and 99. Erasing all arguments..."
                    engine.say(VALUE_TOO_HIGH)
                    engine.runAndWait()
                    return "Error" #Returns Error to know later on that we need to ask for this again
                    


            except ValueError: #Uses the except handle for a ValueError incase the user attempts to enter anything but an integer

                engine = pyttsx3.init() #Text to speech: says that only numbers can be used and not anything else
                WRONG_ARGUMENT = f"Error on {self.line_number}. Please put in only numbers for {self.function_name} blocks. Erasing all arguments..."
                engine.say(WRONG_ARGUMENT)
                engine.runAndWait()
                return "Error" #Returns Error to know later on that we need to ask for this again
                
        #Checks if the function is a while loop or a if statement, if it is, then it'll check the arguments.
        elif self.function_name == "While Loop" or self.function_name == "If":

            if len(list_of_arguments) not in range(3, 5): #Checks if there are more than 3 or 4 arguments (the only amount that should occur)

                engine = pyttsx3.init() #If there are too many arguments, then the text to speech will say such
                TOO_MANY_ARGUMENTS = f"Error on {self.line_number}. Too little or too many arguments entered for {self.function_name}. Erasing all arguments..."
                engine.say(TOO_MANY_ARGUMENTS)
                engine.runAndWait()
                return "Error" #Returns Error to know later on that we need to ask for this again
                

            elif len(list_of_arguments) in range(3, 5): #Checks if the list of arguments ARE 3 or 4

                if len(list_of_arguments) == 3: #Checks if the amount of arguments are three

                    try:
                        
                        if list_of_arguments[0] == "Dist" and (list_of_arguments[1] == "<" or list_of_arguments[1] == ">") and int(list_of_arguments[2]) in range(0, 10): #Checks if the three arguments are valid, if they are:

                            self.string = list_of_arguments[0] + " " + list_of_arguments[1] + " " + list_of_arguments[2] + "cm" #It'll set the radio to be what is given
                            self.radio_name = "p" + list_of_arguments[1] + list_of_arguments[2] #It'll set the radio to be what is given
                            return self.string

                        else:   #If the arguments aren't valid (eles) then raise an error

                            engine = pyttsx3.init() #Tells text to speech to say that there are invalid arguments
                            INVALID_ARGUMENTS = f"Error on {self.line_number}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            return "Error" #Returns Error to know later on that we need to ask for this again
                            
                            

                    except ValueError: #Uses the except handle for a ValueError incase the user attempts to enter anything but an integer for the distance to use

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line_number}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        return "Error" #Returns Error to know later on that we need to ask for this again
                        

                elif len(list_of_arguments) == 4: #Checks if the amount of arguments given are four

                    try:
                        
                        if list_of_arguments[0] == "Dist" and (list_of_arguments[1] == "<" or list_of_arguments[1] == ">") and int(list_of_arguments[2]) in range(0, 10) and (int(list_of_arguments[3]) in range(0, 10)): ##Checks if the four arguments are valid, if they are:
                            
                            self.string = list_of_arguments[0] + " " + list_of_arguments[1] + " " + list_of_arguments[2] + list_of_arguments[3] + "cm" #It'll set the radio to be what is given
                            self.radio_name = "p" + list_of_arguments[1] + list_of_arguments[2] + list_of_arguments[3] #It'll set the radio to be what is given
                            return self.string

                        else:

                            engine = pyttsx3.init() #Else the arguments are not valid, then an error is raised (text to speech)
                            INVALID_ARGUMENTS = f"Error on {self.line_number}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            return "Error" #Returns Error to know later on that we need to ask for this again
                            

                    except ValueError: #Uses the except handle for a ValueError incase the user attempts to enter anything but an integer for the distance to use

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line_number}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        return "Error" #Returns Error to know later on that we need to ask for this again

        elif self.function_name == "None": #If no functions are presented, then the arguments will stay at a constant "No Arguments". Radio will just be a space sent over.
            self.string = "No Arguments"
            self.radio_name = " "
            return "No Arguments"
            


pygame.init()


# Initialize pygame library and display

screen = pygame.display.set_mode((900, 650)) #Set the display to 900x650 (COULD HAVE BEEN CHANGED TO SOMETHING BIGGER, DIDNT HAVE TIME DUE TO HAVING TO CHANGE SOME OF THE DIMENSIONS WITHIN THE OBJECTS)

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

button: "list[int]" = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19] #GPIO Pins used for the keypad

#Setup for the GPIO pins to be used

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


line_list: "list[Line]" = [] #Empty list to contain all of the Line objects and control them all at once with a for loop

for i in range(1, 13):

    line_list.append(Line(i)) #Appends a Line object with the given number to give the appropriate number

def program_startup():

    """Runs the entire program."""

    #WHILE LOOP THAT CONTROLS DISPLAYING THE INFORMATION ON THE GUI (not much functionality apart from taking in data)

    RUNNING = True

    while (RUNNING):

        # Look through all the events that happened in the last frame to see if the user tries to exit.
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUNNING = False
            elif (event.type == QUIT):
                RUNNING = False

        list_of_analogs = serial_monitor() #Calls the serial monitor function to constantly check for what is on the rack.
        function_list: list[Functions] = [] #List to keep track of the instantiated functions to be easily called upon

        for (line_number, analog_values) in zip((range(1, 13)), (list_of_analogs)): #Iterates through a range of 1-12 and through the list of analogs from the rack at once.

            function_list.append(Functions(line_number, analog_values)) #Going through all of these values (in the zip function) we can instantiate a Function with these values

        header_list = ["Line #:", "Block Type:", "Arguments:"]  #Headers For the Line numbers, Block Types, and Arguments
        header_dict = {"Line #:": 0, "Block Type:": 300, "Arguments:": 600} #Dictionary that says where the headers will be along the X-axis


        for i in header_list: #Renders all of the headers

            font_surface = FONT.render(i, True, WHITE_FONT) #Renders font surface with constant FONT

            rect = pygame.Rect((header_dict[i], 0, 300, 50)) #Creates a rect based on which header it is (dictionary being used and tells where for it to be).
            rect_centered = font_surface.get_rect(center=rect.center) #Centers the font surface within the rectangle

            pygame.draw.rect(screen, GREY, rect) #Draws the rectangles
            screen.blit(font_surface, rect_centered) #Pygame's way of saying to put this on the screen
        
        for lines in line_list:

            pygame.draw.rect(screen, GREY, lines.rect)  #Draws the line blocks on the screen
            screen.blit(lines.font_surface, lines.rect_centered)  #Pygame's way of saying to put this on the screen and puts what line number it is

        for functions in function_list:
        
            pygame.draw.rect(screen, GREY, functions.rect)  #Draws the function blocks on the screen
            screen.blit(functions.font_surface, functions.rect_centered)  #Pygame's way of saying to put this on the screen and puts the text of what the function is

        list_of_arguments: list[Arguments] = [] #List to keep track of all of the instantiated arguments (basically just to put that there are "No Arguments" until the next while loop)

        for (line_number, function) in zip((range(1, 13)), function_list): #Goes through a range of 1-12 and the function list
            
            argument = Arguments(line_number, function.function_name) #Sets line number and finds the function name to create an argument
            list_of_arguments.append(argument)

        for arguments in list_of_arguments:

            pygame.draw.rect(screen, GREY, arguments.rect) #Draws the arguments

            font_surface = FONT.render(arguments.string, True, WHITE_FONT) #Creates the font surface in the for loop (caused issues within the class, so I decided to go this route)
            centered = font_surface.get_rect(center=arguments.rect.center) #Centered the text within the rectangle

            pygame.draw.rect(screen, GREY, arguments.rect)
            screen.blit(font_surface, centered) #Pygame's way of saying to put this on the screen and put the arguments within the block

        if GPIO.input(12) == True: #Checks the state of pin 12 (aka Lock button), this ultimately breaks the while loop and continues the program to another while loop

            engine = pyttsx3.init()
            LOCKED = "The rack is now locked" #The text to speech will say this
            engine.say(LOCKED)
            engine.runAndWait()

            RUNNING = False
            sleep(0.2)

            
        pygame.display.flip()

    #START OF WHILE LOOP THAT GOES THROUGH ALL OF THE ARGUMENTS AND SETTING THEM -- The Functions will no longer be updated here

    argument_counter = 0 #Counter that keeps track of which argument we're on

    while argument_counter != 12: #Ensures the entire list of arguments are accounted for when iterating

        for event in pygame.event.get():

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                exit()
            elif (event.type == QUIT):
                exit()
       
        for arguments in list_of_arguments: #Goes through each of the argument objects

            if list_of_arguments.index(arguments) == argument_counter: #Checks which argument we're currently on

                if arguments.function_name == "None": #If there is no function there when the argument counter gets to it, then that means we don't change the arguments from "No Arguments"
                    continue

                else: #If there is a function then:

                    WRONG = True
                    #This loop allows it to where if you put an invalid argument, then it will continuously keep telling you to put a valid one until a valid one is inputted
                    while WRONG:
                        
                        engine = pyttsx3.init() #Says that we are on whichever line, and we are currently editing the arguments for whichever function
                        engine.say(f"Currently on Line {argument_counter + 1} for putting arguments onto {arguments.function_name} block.")
                        engine.runAndWait()

                        string = arguments.string_of_arguments_determiner(buttons()) #Goes through the argument method that checks all inputs from the button function

                        if string == "Error": #Error means that the function returned an error and the text to speech just says to try again.

                            engine = pyttsx3.init()
                            engine.say(f"Try putting a valid argument on Line {argument_counter + 1} again.")
                            engine.runAndWait()

                        else:   #Otherwise we stop this loop

                            WRONG = False

            else:
                string = arguments.string #Allows it to where the other arguments that are not being affected (because we are doing one at a time) will still be constantly refreshed.

            font_surface = FONT.render(string, True, WHITE_FONT)            #Rest of these things just draw the arguments
            centered = font_surface.get_rect(center=arguments.rect.center)
                        
            pygame.draw.rect(screen, GREY, arguments.rect)
            screen.blit(font_surface, centered) #Pygame's way of saying to put this on the screen and show what the arguments are
        
        argument_counter += 1

        pygame.display.flip()



    RUN_NOT_PRESSED = True

    engine = pyttsx3.init()
    engine.say("Press read, then press a line number if you would like to hear the arguments of the block. Press Run if you are ready for your program to start")
    engine.runAndWait()


    function_argument_string = ""

    #START OF NEW WHILE LOOP, THIS IS WHERE THE READ AND RUN FUNCTIONALITY IS RUN

    while RUN_NOT_PRESSED:

        for event in pygame.event.get():

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                exit()
            elif (event.type == QUIT):
                exit()

        if GPIO.input(23) == True: #Checks if pin 23 is high (or Read), if so:

            engine = pyttsx3.init() #Text to speech says we are in reading mode
            engine.say("Reading lines, please select a line number to read its block and arguments")
            engine.runAndWait()
            sleep(0.2)

            WRONG = True

            #This loop ensures that if there is an invalid input then it wil keep running until there is a valid one put in for reading a line

            while WRONG == True:

                button = buttons() #Returns the list of buttons pressed
                try:

                    if int("".join(button)) in range(0, 100):
                        button_value = "".join(button)
                        WRONG = False

                    else:

                            engine = pyttsx3.init()
                            engine.say("Invalid input, try putting in a number between 1 and 12.")
                            engine.runAndWait()

                except ValueError:

                    engine = pyttsx3.init()
                    engine.say("Invalid input, only use numbers to signify the line number.")
                    engine.runAndWait()


            engine = pyttsx3.init()
            engine.say(f"Line {button_value} has a {function_list[int(button_value) - 1].function_name} block and its arguments are {list_of_arguments[int(button_value) - 1].string}")
            engine.runAndWait()

        elif GPIO.input(27) == True:

            for (function_values, argument_values) in zip(function_list, list_of_arguments):

                string_of_values = function_values.radio_name + argument_values.radio_name 
                function_argument_string += string_of_values
                radio = function_argument_string.strip() + " "

            engine = pyttsx3.init()
            engine.say("Code has begun running. Please wait for the upload process to complete.")
            engine.runAndWait()
            sleep(0.2)

            print(radio)
            radio_code(radio)
            
        elif GPIO.input(19) == True:

            engine = pyttsx3.init()
            engine.say("Are you sure?")
            engine.runAndWait()
            sleep(0.2)

            secret_to_restart = ["1", "2", "3", "4"]

            secret_list = buttons()

            if secret_list == secret_to_restart:

                engine = pyttsx3.init()
                engine.say("Restarting...")
                engine.runAndWait()
                sleep(0.2)
                RUN_NOT_PRESSED = False
                program_startup()



program_startup()