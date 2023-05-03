import pygame
from testingserial import serial_monitor
import pyttsx3
from CONSTANTS import *
from Buttons import *
from time import sleep
import RPi.GPIO as GPIO

class Line():
    HEIGHT = 50
    WIDTH = 300
    LINE_HEIGHTS = {
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
    
    def __init__(self, number:int): #Takes in number to assign the name of it
        
        self.name = f"Line {number}"
        self.height = Line.LINE_HEIGHTS[self.name]
        self.rect = pygame.Rect((0, self.height, Line.WIDTH, Line.HEIGHT))
        self.font = FONT
        self.font_surface = self.font.render(self.name, True, WHITE_FONT)
        self.rect_centered = self.font_surface.get_rect(center=self.rect.center)

class Functions():
    HEIGHT = 50
    WIDTH = 300
    FUNCTION_HEIGHTS = {
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

        self.function_location_name:str = f"Function {line_number}"
        self.height = Functions.FUNCTION_HEIGHTS[self.function_location_name]
        self.rect = pygame.Rect((300, self.height, Functions.WIDTH, Functions.HEIGHT))
        self.font = FONT

        self.analog_value:int = analog_value

        self.function_name = self.function_determiner()
        self.font_surface = self.font.render(self.function_name, True, WHITE_FONT)
        self.rect_centered = self.font_surface.get_rect(center=self.rect.center)

    def function_determiner(self):

        if self.analog_value in range(173, 182):

            return "Go Forward"
        
        elif self.analog_value in range(506, 520):

            return "Turn Left"
        
        elif self.analog_value in range(147, 156):

            return "While Loop"
        
        elif self.analog_value in range(833, 844):

            return "Turn Right"
        
        elif self.analog_value in range(335, 343):

            return "If"
        
        elif self.analog_value in range(72, 80):

            return "For Loop"
        
        elif self.analog_value in range(86, 95):

            return "Go Reverse"
        
        else:

            return "None"
        
class Arguments():

    HEIGHT = 50
    WIDTH = 300
    ARGUMENT_HEIGHTS = {
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

        self.argument_location_name = f"Argument {line_number}"
        self.line_number = f"Line {line_number}"
        self.function_name = function_name

        self.string = "No Arguments"
        self.height = Arguments.ARGUMENT_HEIGHTS[self.argument_location_name]
        self.rect = pygame.Rect((600, self.height, Arguments.WIDTH, Arguments.HEIGHT))


    
    def string_of_arguments_determiner(self, list_of_arguments):

        if self.function_name == "Go Forward" or self.function_name == "Turn Left" or self.function_name == "Turn Right" or self.function_name == "Go Reverse" or self.function_name == "For Loop":
            try:

                if int("".join(list_of_arguments)) in range(0, 100):

                    if self.function_name == "For Loop":
                        
                        self.string = "Repeat" + "".join(list_of_arguments) + "times"
                        return "Repeat" + "".join(list_of_arguments) + "times"

                    else:
                        
                        self.string = "".join(list_of_arguments) + " seconds"
                        return "".join(list_of_arguments) + " seconds"
                    

                else: 
                    
                    engine = pyttsx3.init()
                    VALUE_TOO_HIGH = f"Error on {self.line_number}. Numbers cannot exceed must stay between 0 and 99. Erasing all arguments..."
                    engine.say(VALUE_TOO_HIGH)
                    engine.runAndWait()
                    return "Error"
                    


            except ValueError:

                engine = pyttsx3.init()
                WRONG_ARGUMENT = f"Error on {self.line_number}. Please put in only numbers for {self.function_name} blocks. Erasing all arguments..."
                engine.say(WRONG_ARGUMENT)
                engine.runAndWait()
                return "Error"
                

        elif self.function_name == "While Loop" or self.function_name == "If":

            if len(list_of_arguments) not in range(3, 5):

                engine = pyttsx3.init()
                TOO_MANY_ARGUMENTS = f"Error on {self.line_number}. Too many arguments entered for {self.function_name}. Erasing all arguments..."
                engine.say(TOO_MANY_ARGUMENTS)
                engine.runAndWait()
                return "Error"
                

            elif len(list_of_arguments) in range(3, 5):

                if len(list_of_arguments) == 3:

                    try:
                        
                        if list_of_arguments[0] == "Dist" and (list_of_arguments[1] == "<" or list_of_arguments[1] == ">") and int(list_of_arguments[2]) in range(0, 10):
                            self.string = " ".join(list_of_arguments) + "cm"
                            return " ".join(list_of_arguments) + "cm"

                        else:
                            engine = pyttsx3.init()
                            INVALID_ARGUMENTS = f"Error on {self.line_number}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            return "Error"
                            
                            

                    except ValueError:

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line_number}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        return "Error"
                        

                elif len(list_of_arguments) == 4:

                    try:
                        
                        if list_of_arguments[0] == "Dist" and (list_of_arguments[1] == "<" or list_of_arguments[1] == ">") and int(list_of_arguments[2]) in range(0, 10) and int(list_of_arguments[3] in range(0, 10)):
                            
                            self.string = list_of_arguments[0] + " " + list_of_arguments[1] + " " + (list_of_arguments[2] + list_of_arguments[3])
                            return list_of_arguments[0] + " " + list_of_arguments[1] + " " + (list_of_arguments[2] + list_of_arguments[3])

                        else:

                            engine = pyttsx3.init()
                            INVALID_ARGUMENTS = f"Error on {self.line_number}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            return "Error"
                            

                    except ValueError:

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line_number}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        return "Error"

        elif self.function_name == "None": 
            self.string = "No Arguments"
            return "No Arguments"
            


pygame.init()
line_list = []
for i in range(1, 13):

    line_list.append(Line(i))

# Initialize pygame library and display

screen = pygame.display.set_mode((900, 650))

# Create a person object

RUNNING = True 

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)

button = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19]

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



def program_startup():

    RUNNING = True

    while (RUNNING):
        # Look through all the events that happened in the last frame to see
        # if the user tried to exit.
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUNNING = False
            elif (event.type == QUIT):
                RUNNING = False

        list_of_analogs = serial_monitor()
        function_list = []

        for (line_number, analog_values) in zip((range(1, 13)), (list_of_analogs)):

            function_list.append(Functions(line_number, analog_values))

        header_list = ["Line #:", "Block Type:", "Arguments:"]
        header_dict = {"Line #:": 0, "Block Type:": 300, "Arguments:": 600}


        for i in header_list:

            font_surface = FONT.render(i, True, WHITE_FONT)

            rect = pygame.Rect((header_dict[i], 0, Line.WIDTH, Line.HEIGHT))
            rect_centered = font_surface.get_rect(center=rect.center)

            pygame.draw.rect(screen, GREY, rect)
            screen.blit(font_surface, rect_centered)
        
        for lines in line_list:

            pygame.draw.rect(screen, GREY, lines.rect)
            screen.blit(lines.font_surface, lines.rect_centered)  # blit the text surface onto the rectangle

        for functions in function_list:
        
            pygame.draw.rect(screen, GREY, functions.rect)
            screen.blit(functions.font_surface, functions.rect_centered)  # blit the text surface onto the rectangle

        list_of_arguments = []

        for (line_number, function) in zip((range(1, 13)), function_list):
            
            argument = Arguments(line_number, function.function_name)
            list_of_arguments.append(argument)

        for arguments in list_of_arguments:

            pygame.draw.rect(screen, GREY, arguments.rect)

            what_to_show = arguments.string

            font_surface = FONT.render(what_to_show, True, WHITE_FONT)
            centered = font_surface.get_rect(center=arguments.rect.center)

            pygame.draw.rect(screen, GREY, arguments.rect)
            screen.blit(font_surface, centered)

        if GPIO.input(12) == True:

            engine = pyttsx3.init()
            LOCKED = "The rack is now locked"
            engine.say(LOCKED)
            engine.runAndWait()

            RUNNING = False
            sleep(0.2)

            
        pygame.display.flip()


    argument_counter = 0
    memory_of_args = []

    while argument_counter != 12:

        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUNNING = False
            elif (event.type == QUIT):
                RUNNING = False

        for i in header_list:

            font_surface = FONT.render(i, True, WHITE_FONT)

            rect = pygame.Rect((header_dict[i], 0, Line.WIDTH, Line.HEIGHT))
            rect_centered = font_surface.get_rect(center=rect.center)

            pygame.draw.rect(screen, GREY, rect)
            screen.blit(font_surface, rect_centered)

        for lines in line_list:

            pygame.draw.rect(screen, GREY, lines.rect)
            screen.blit(lines.font_surface, lines.rect_centered)

        for functions in function_list:
        
            pygame.draw.rect(screen, GREY, functions.rect)
            screen.blit(functions.font_surface, functions.rect_centered)

        for arguments in list_of_arguments:

            pygame.draw.rect(screen, GREY, arguments.rect)

            what_to_show = arguments.string

            font_surface = FONT.render(what_to_show, True, WHITE_FONT)
            centered = font_surface.get_rect(center=arguments.rect.center)

            pygame.draw.rect(screen, GREY, arguments.rect)
            screen.blit(font_surface, centered)

        memory_of_args.append(list_of_arguments[argument_counter])

        f = 0

        while f < len(memory_of_args):

            list_of_arguments[f] = memory_of_args[f]
            f += 1
       
        for arguments in list_of_arguments:

            if list_of_arguments.index(arguments) == argument_counter:

                if arguments.function_name == "None":
                    continue

                WRONG = True
                while WRONG:
                    
                    engine = pyttsx3.init()
                    engine.say(f"Currently on Line {argument_counter + 1} for putting arguments onto {arguments.function_name} block.")
                    engine.runAndWait()

                    string = arguments.string_of_arguments_determiner(buttons())

                    if string == "Error":

                        engine = pyttsx3.init()
                        engine.say(f"Try putting a valid argument on Line {argument_counter + 1} again.")
                        engine.runAndWait()

                    else: 

                        WRONG = False

            else:
                string = arguments.string

            font_surface = FONT.render(string, True, WHITE_FONT)
            centered = font_surface.get_rect(center=arguments.rect.center)
                        
            pygame.draw.rect(screen, GREY, arguments.rect)
            screen.blit(font_surface, centered)
        
        argument_counter += 1

        pygame.display.flip()

    RUN_NOT_PRESSED = True

    engine = pyttsx3.init()
    engine.say("Press read, then press a line number if you would like to hear the arguments of the block. Press Run if you are ready for your program to start")
    engine.runAndWait()

    while RUN_NOT_PRESSED:

        if GPIO.input(23) == True:

            WRONG = True
            while WRONG == True:

                if len(buttons()) == 2:

                    button_value = (buttons())[1]
                    WRONG = False

                elif len(buttons()) == 3:
                    button_value = (buttons())[1] + (buttons())[2]
                    WRONG = False

                else:

                        engine = pyttsx3.init()
                        engine.say("Invalid input, try putting in a number between 1 and 12.")
                        engine.runAndWait()

            WRONG = True
            while WRONG:
                if int(button_value) not in range(1, 13):
                        
                    engine = pyttsx3.init()
                    engine.say("That is not a valid line number. Try again.")
                    engine.runAndWait()

                else: 

                    engine = pyttsx3.init()
                    engine.say(f"Line {button_value} has a {function_list[button_value - 1].function_name} block and its arguments are {list_of_arguments[button_value - 1].string}")
                    engine.runAndWait()

        elif GPIO.input(27) == True:

            pass #FIGURE THIS OUT LATER WITH MAYBE A FUNCTION

            



program_startup()