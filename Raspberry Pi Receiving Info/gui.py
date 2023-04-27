import pygame
from time import sleep
# initialize Pygame
pygame.init()

# define the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class GUI:
    
    def __init__(self):


        # creates the screen and sets the display caption, which is the name at the top left
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("CodeBuilders!")

        # define the font and font size to be used for the text displayed on the screen
        self.font = pygame.font.Font(None, 36)

        # creates a list of dictionaries, each iterable has a key of "argument" and "function"
        # to be used in the code for displaying each row, argument, and function.
        self.function_and_argument_list = self.create_list()

        # creates surfaces to be used
        self.create_surfaces()



    def create_list(self):

        list_of_dicts = []

        # amount of positions we have on the rack, so thats going to be the amount of "lines" or 
        # items in our list of dictionaries
        amount_of_positions = 12

        # creates a list of dictionaries that have empty strings that we can change later, used
        # to refer what is on each line on the rack to be displayed on the GUI
        for position in range(amount_of_positions):
            list_of_dicts.append({"row_surface": None, 
                                  "function_surface": None, 
                                  "function_rect": None,
                                  "argument_surface": None,
                                  "argument_rect": None,
                                  "function": "cat",# (supposed to be a function, perhaps a class)
                                  "argument": ""})
        
        return list_of_dicts



    def create_surfaces(self):
        for i, row in enumerate(self.function_and_argument_list):

            # creates surfaces for every row, function, and argument, and assigns it to the key in the 
            # dictionary in the list of dictionaries callled function_and_argument_list
            row["row_surface"] = self.font.render(f"{i}", True, pygame.Color("white"))
            row["function_surface"]  = self.font.render(row["function"], True, pygame.Color("white"))
            row["argument_surface"] = self.font.render(row["argument"], True, pygame.Color("white"))



    def display_text(self):

        # iterates through the list of dictionaries, getting their positions and centering those positions
        # at the given coordingates, putting them onto the screen and then updating the screen after so
        # the words actually appear on the screen
        for i, row in enumerate(self.function_and_argument_list):

            # creates a rectangle to position the text on the screen
            # row doesn't need a key value rect since it never gets changed
            row_rect = row["row_surface"].get_rect()
            row["function_rect"] = row["function_surface"].get_rect()
            row["argument_rect"] = row["argument_surface"].get_rect()


            row_rect.center = (WINDOW_WIDTH // 3,(i + 1) * 50 - 20)
            row["function_rect"].center = (WINDOW_WIDTH // 2, (i + 1) * 50 - 20)
            row["argument_rect"].center = (WINDOW_WIDTH // 1, (i + 1) * 50 - 20)


            # draw the text surface on the screen
            self.screen.blit(row["row_surface"], row_rect)
            self.screen.blit(row["function_surface"], row["function_rect"])
            self.screen.blit(row["argument_surface"], row["argument_rect"])


            # update the screen so stuff is actually on it
            pygame.display.flip()

# currently only works for changing the function surface, not the argument
    def change_function_text(self, dictionary):
            
            # fills the surface with the background color
            dictionary["function_surface"].fill("black")

            # the rectangle that is filled with the background color goes over where the original surface was
            # to basically "delete" the old surface
            self.screen.blit(dictionary["function_surface"], dictionary["function_rect"])

            # creates a surface based on the function assigned in the event handling portion
            # of the code and assigns it to the "function_surface" key of the given dictionary
            dictionary["function_surface"]  = self.font.render(dictionary["function"], True, pygame.Color("white"))

            self.screen.blit(dictionary["function_surface"], dictionary["function_rect"])

            # updates the display
            pygame.display.flip()

    # def change_text(self, AR_value):
        # # use this to change a specific text whether it be based on an AR value and interpreting that
        # # into a function to actually put on the screen or not
        # pass

    def run(self):

        running = True
        self.display_text()

        while running:
            for event in pygame.event.get():
                ################
                # have functionality right here for if a button is pressed ? maybe arrow keys for reading
                # down the lines????
                if event.type == pygame.QUIT:
                    running = False


                # this isnt the actual event thats going to trigger the change, it will most likely be a shift
                # in current whether there is or isnt, and that will trigger a change from 0 to none,
                # and then depending on the analog value, there will be logic code within the elif
                # statement to change the code "function" to that specific function associated with
                # the analog value
                elif event.type == pygame.KEYDOWN:
                    self.function_and_argument_list[2]["function"] = "mouse" # this is a placeholder  for chanig the function
                    self.change_function_text(self.function_and_argument_list[2])


        # quit Pygame
        pygame.quit()

p = GUI()
p.run()