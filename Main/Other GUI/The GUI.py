#####################################################################
# author: Cole Sylvester
# date:   March 20th, 2023 
# description: Person Reloaded Programming Assignment
#####################################################################
import pygame
from testingserial import serial_monitor
import pyttsx3


class Line():
    HEIGHT = 50
    WIDTH = 200
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
        self.font = pygame.font.Font(None, 36)
        self.font_surface = self.font.render(self.name, True, (255, 255, 255))
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
        self.rect = pygame.Rect((200, self.height, Functions.WIDTH, Functions.HEIGHT))
        self.font = pygame.font.Font(None, 36)

        self.analog_value:int = analog_value

        self.font_surface = self.font.render(self.function_determiner(), True, (255, 255, 255))
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
                    "ARGUMENT 1": 50,
                    "ARGUMENT 2": 100,
                    "ARGUMENT 3": 150,
                    "ARGUMENT 4": 200,
                    "ARGUMENT 5": 250,
                    "ARGUMENT 6": 300,
                    "ARGUMENT 7": 350,
                    "ARGUMENT 8": 400,
                    "ARGUMENT 9": 450,
                    "ARGUMENT 10": 500,
                    "ARGUMENT 11": 550,
                    "ARGUMENT 12": 600
                    }

    def __init__ (self, line_number, function_name, list_of_arguments: list):

        self.argument_location_name = f"Argument {line_number}"
        self.function_name = function_name
        self.arguments = list_of_arguments
        self.string_of_arguments = "No Arguments"

        self.height = Arguments.ARGUMENT_HEIGHTS[self.argument_location_name]
        self.rect = pygame.Rect((500, self.height, Arguments.WIDTH, Arguments.HEIGHT))
        self.font = pygame.font.Font(None, 36)

        self.font_surface = self.font.render(self.string_of_arguments, True, (255, 255, 255))
        self.rect_centered = self.font_surface.get_rect(center=self.rect.center)

    @property
    def function_arguments(self):

        return self._string_of_arguments

    @function_arguments.setter
    def function_arguments(self):

        if self.function_name == "Go Forward" or self.function_name == "Turn Left" or self.function_name == "Turn Right" or self.function_name == "Go Reverse" or self.function_name == "For Loop":
            try:

                if int("".join(self.arguments)) in range(0, 100):

                    if self.function_name == "For Loop":

                        self._string_of_arguments = "Repeat" + "".join(self.arguments) + "times"

                    else:

                        self._string_of_arguments = "".join(self.arguments) + "seconds"
                    

                else: 
                    
                    engine = pyttsx3.init()
                    VALUE_TOO_HIGH = f"Error on {self.line}. Numbers cannot exceed must stay between 0 and 99. Erasing all arguments..."
                    engine.say(VALUE_TOO_HIGH)
                    engine.runAndWait()
                    self.arguments = []


            except ValueError:

                engine = pyttsx3.init()
                WRONG_ARGUMENT = f"Error on {self.line}. Please put in only numbers for {self.function_arguments}. Erasing all arguments..."
                engine.say(WRONG_ARGUMENT)
                engine.runAndWait()
                self.arguments = []

        elif self.function_name == "While Loop" or self.function_name == "If":

            if len(self.arguments) not in range(3, 5):

                engine = pyttsx3.init()
                TOO_MANY_ARGUMENTS = f"Error on {self.line}. Too many arguments entered for {self.function_name}. Erasing all arguments..."
                engine.say(TOO_MANY_ARGUMENTS)
                engine.runAndWait()
                self.arguments = []

            elif len(self.arguments) in range(3, 5):

                if len(self.arguments) == 3:

                    try:
                        
                        if self.arguments[0] == "Ping" and (self.arguments[1] == "<" or self.arguments[1] == ">") and int(self.arguments[2]) in range(0, 10):
                            self._string_of_arguments = " ".join(self.arguments) + "cm"

                        else:

                            engine = pyttsx3.init()
                            INVALID_ARGUMENTS = f"Error on {self.line}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            self.arguments = []
                            

                    except ValueError:

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        self.arguments = []

                elif len(self.arguments) == 4:

                    try:
                        
                        if self.arguments[0] == "Ping" and (self.arguments[1] == "<" or self.arguments[1] == ">") and int(self.arguments[2]) in range(0, 10) and int(self.arguments[3] in range(0, 10)):

                            self._string_of_arguments = self.arguments[0] + " " + self.arguments[1] + " " + (self.arguments[2] + self.arguments[3])

                        else:

                            engine = pyttsx3.init()
                            INVALID_ARGUMENTS = f"Error on {self.line}. Invalid arguemnts for {self.function_name}. Erasing all arguments..."
                            engine.say(INVALID_ARGUMENTS)
                            engine.runAndWait()
                            self.arguments = []

                    except ValueError:

                        engine = pyttsx3.init()
                        NUM_NOT_NUM = f"Error on {self.line}. Ping distance must be a number on {self.function_name} blocks. Erasing all arguments..."
                        engine.say(NUM_NOT_NUM)
                        engine.runAndWait()
                        self.arguments = []

        else: 
            self._string_of_arguments = "No Arguments"
            


pygame.init()
line_list = []
for i in range(1, 13):

    line_list.append(Line(i))

# Initialize pygame library and display

screen = pygame.display.set_mode((800, 650))

# Create a person object

RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

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

    for (i, j) in zip((range(1, 13)), (list_of_analogs)):

        function_list.append(Functions(i, j))

    header_height = 50
    header_list = ["Line #", "Block Type", "Arguments"]
    header_dict = {"Line #": 0, "Block Type": 200, "Arguments": 400}


    for i in header_list:

        font = pygame.font.Font(None, 36)
        font_surface = font.render(i, True, (255, 255, 255))
        rect = pygame.Rect((header_dict[i], 0, Line.WIDTH, Line.HEIGHT))
        rect_centered = font_surface.get_rect(center=rect.center)
        pygame.draw.rect(screen, [0xA2, 0xAA, 0xAD], rect)
        screen.blit(font_surface, rect_centered)
    
    for lines in line_list:

        pygame.draw.rect(screen, [0xA2, 0xAA, 0xAD], lines.rect)
        screen.blit(lines.font_surface, lines.rect_centered)  # blit the text surface onto the rectangle

    for functions in function_list:
       
       pygame.draw.rect(screen, [0xA2, 0xAA, 0xAD], functions.rect)
       screen.blit(functions.font_surface, functions.rect_centered)  # blit the text surface onto the rectangle 

    pygame.display.flip()


