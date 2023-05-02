#####################################################################
# author: Cole Sylvester
# date:   March 20th, 2023 
# description: Person Reloaded Programming Assignment
#####################################################################
import pygame
from testingserial import serial_monitor

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
    

    
    def __init__(self, number: int, analog_value: int):

        self.function_location_name:str = f"Function {number}"
        self.height = Functions.FUNCTION_HEIGHTS[self.function_location_name]
        self.rect = pygame.Rect((200, self.height, Line.WIDTH, Line.HEIGHT))
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


