import pygame
from Classes import *
# initialize Pygame
pygame.init()

# define the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ON = True
OFF = False


class GUI:
    def __init__(self):
        # creates the screen and sets the display caption, which is the name at the top left
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("CodeBuilders!")


        # define the font and font size to be used for the text displayed on the screen
        self.font = pygame.font.Font(None, 36)


        # creates a list of dictionaries, each iterable has a key of "argument" and "function"
        # to be used in the code for displaying each row, argument, and function.
        self.list_of_dicts = self.create_list()


        # creates surfaces to be used
        self.create_surfaces()

        # pins for buttons
        self.pins = [17, 16, 13, 12, 6, 5, 4, 27, 26, 25, 24, 23, 22, 21, 20, 19]

        # the values associated with each pin
        self.button_vals = {17: "1",
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

    def create_list(self):
        list_of_dicts = []

        # amount of positions we have on the rack, so thats going to be the amount of "lines" or 
        # items in our list of dictionaries
        amount_of_positions = 12


        # creates a list of dictionaries that have empty strings that we can change later, used
        # to refer what is on each line on the rack to be displayed on the GUI
        for position in range(amount_of_positions):
            list_of_dicts.append({"row_surface": None, 
                                  "row_rect": None,
                                  "function_surface": None, 
                                  "function_rect": None,
                                  "argument_surface": None,
                                  "argument_rect": None,
                                  "function": "cat",# (supposed to be a function, perhaps a class)
                                  "argument": "dog",
                                  "previous_state": OFF,
                                  "current_state": OFF})

        return list_of_dicts


    def create_surfaces(self):
        for i, line in enumerate(self.list_of_dicts):
            # creates surfaces for every line, function, and argument, and assigns it to the key in the 
            # dictionary in the list of dictionaries callled list_of_dicts
            
            # the reason why thers str() because the values for line["function"] are going to be classes,
            # and the str() calls on its string representation to make the surface.
            line["row_surface"] = self.font.render(str(f"{i}"), True, pygame.Color("white"))
            line["function_surface"]  = self.font.render(str(line["function"]), True, pygame.Color("white"))
            line["argument_surface"] = self.font.render(str(line["argument"]), True, pygame.Color("white"))


    def display_text(self):
            for line in self.list_of_dicts:
                # puts the "surfaces" or text onto the screen based on the positions that were defined
                # in setup_text
                self.screen.blit(line["row_surface"], line["row_rect"])
                self.screen.blit(line["function_surface"], line["function_rect"])
                self.screen.blit(line["argument_surface"], line["argument_rect"])


                # update the screen so stuff is actually on it
                pygame.display.flip()


    def setup_text(self):
        # iterates through the list of dictionaries
        for i, line in enumerate(self.list_of_dicts):


            # creates a rectangle to position the text on the screen
            line["row_rect"] = line["row_surface"].get_rect()
            line["function_rect"] = line["function_surface"].get_rect()
            line["argument_rect"] = line["argument_surface"].get_rect()


            line["row_rect"].center = (WINDOW_WIDTH // 6,(i + 1) * 50 - 20)
            line["function_rect"].center = (WINDOW_WIDTH // 3, (i + 1) * 50 - 20)
            line["argument_rect"].center = (WINDOW_WIDTH // 1.5, (i + 1) * 50 - 20)


    def change_text(self):
                self.delete_text()
                self.create_surfaces()
                self.display_text()


    def function_checking(self, analog_list): # iterates through the analog value list, and assigns
        # a function to the item in the list of dictionaries that was created at the beginning
        # with the same index. this works because there are 12 inputs for analog values, and also
        # 12 spaces for the blocks. 

        for i, analog_value in enumerate(analog_list):
            if analog_value > 0:
                if analog_value in range(165, 190):
                    self.list_of_dicts[i]["function"] = Forward()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(83, 100):
                    self.list_of_dicts[i]["function"] = Reverse()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(825, 850):
                    self.list_of_dicts[i]["function"] = TurnRight()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(500, 520):
                    self.list_of_dicts[i]["function"] = TurnLeft()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(65, 80):
                    self.list_of_dicts[i]["function"] = ForLoop()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(140, 160):
                    self.list_of_dicts[i]["function"] = WhileLoop()
                    self.list_of_dicts[i]["current_state"] = ON


                elif analog_value in range(330, 350):
                    self.list_of_dicts[i]["function"] = IfStatement()
                    self.list_of_dicts[i]["current_state"] = ON


            else:
                self.list_of_dicts[i]["function"] =  None
                self.list_of_dicts[i]["current_state"] = OFF


            if self.list_of_dicts[i]["current_state"] != self.list_of_dicts[i]["previous_state"]:
                self.change_text()
                self.list_of_dicts[i]["previous_state"] = self.list_of_dicts[i]["current_state"]


    def argument_setting(self):
        pass


    def delete_text(self):
        for dict in self.list_of_dicts:
            dict["function_surface"].fill("black")
            dict["argument_surface"].fill("black")

            self.screen.blit(dict["function_surface"], dict["function_rect"])
            self.screen.blit(dict["function_surface"], dict["function_rect"])

        pygame.display.flip()


    def run(self):
        tempList = [0, 90, 0, 170, 294, 982, 235, 546, 365, 464, 264, 0]
        tempList2 = [0, 90, 0, 170, 294, 982, 235, 546, 365, 464, 264, 90]
        running = True
        locked = False
        HIGH = True

        # creates surfaces to be put on the screen
        self.create_surfaces()

        # centers each surface's position at their designated spots
        self.setup_text()

        # actually puts everything on the screen
        self.display_text()

        # # makes it so GPIO pins can be used
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pins, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        variable = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # read based on variable
                elif event.type == pygame.KEYDOWN:
                    self.function_checking(tempList2)
                
#             if GPIO.input(12) == HIGH:
#                 locked = True

# # argument checking
#             while locked == True:
#                 for pin in self.pins:
#                         if GPIO.input(pin) == HIGH:
#                             self.create_surfaces()
#                             self.display_text()
#                             # use this (self.button_vals[i]) to configure arguments
#                             sleep(0.2)

#                 if GPIO.input(12) == HIGH:
#                     locked = False

            self.function_checking(tempList)

        # quit Pygame
        pygame.quit()

p = GUI()
p.run()