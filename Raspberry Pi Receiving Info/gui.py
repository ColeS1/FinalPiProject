import pygame

# initialize Pygame
pygame.init()

# define the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class GUI:
    
    def __init__(self):

        # creates a list of dictionaries, each iterable has a key of "argument" and "function"
        # to be used in the code for displaying each row, argument, and function.
        self.function_and_argument_list = self.create_list()

        # creates a list of surfaces, each item will have a row surface and 
        self.surface_list = self.create_surfaces()

        # creates the screen and sets the display caption, which is the name at the top left
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("CodeBuilders!")

        # define the font and font size to be used for the text
        self.font = pygame.font.Font(None, 36)

    def create_list(self):

        list_of_dicts = []
        
        # amount of positions we have on the rack, so thats going to be the amount of "lines" or 
        # values in the list
        amount_of_positions = 12

        # creates a list of dictionaries that have empty strings that we can change later, used
        # to refer what is on each line on the rack to be displayed on the GUI
        for position in range(amount_of_positions):
            list_of_dicts.append({"row_surface": None, 
                                  "function_surface": None, 
                                  "argument_surface": None,
                                  "function": "placeholder (supposed to be a function, perhaps a class)",
                                  "argument": ""})
        
        return list_of_dicts

    def delete_text(self):
            
            # issue with this is it doesnt know which surface to fill in and update. maybe take in an index and
            # analog value,
            self.text_surface.fill((0,0,0))
            self.function_surface.fill((0,0,0))
            self.argument_surface.fill("black")
            
            # draw the text surface on the screen
            self.screen.blit(self.text_surface, self.text_rect)
            self.screen.blit(self.function_surface, self.function_rect)
            self.screen.blit(self.argument_surface, self.argument_rect)

            # updates the display
            pygame.display.flip()

    def change_text(self, AR_value):
        # use this to change a specific text whether it be based on an AR value and interpreting that
        # into a function to actually put on the screen or not
        pass


    def display_text(self):
# perhaps make a list of dictionaries of surfaces, and each one containing a text, function, and argument, and then 
# iterate through that to blit on a screen
        for i, row in enumerate(self.function_and_argument_list):

            # creates surfaces for every row, function, and argument, and assigns it to the key in the 
            # dictionary in the list of dictionaries callled function_and_argument_list
            self.function_and_argument_list[row]["row_surface"] = self.font.render(f"{i}", True, pygame.Color("white"))
            self.function_and_argument_list[row]["function_surface"] = self.font.render(row["function"], True, pygame.Color("white"))
            self.function_and_argument_list[row]["argument_surface"] = self.font.render(row["argument"], True, pygame.Color("white"))
        

            # create a rectangle to position the text on the screen
            self.text_rect = self.text_surface.get_rect()
            self.function_rect = self.function_surface.get_rect()
            self.argument_rect = self.argument_surface.get_rect()

            self.text_rect.center = (WINDOW_WIDTH // 3, (i + 1) * 50)
            self.function_rect.center = (WINDOW_WIDTH // 2, (i + 1) * 50)
            self.argument_rect.center = (WINDOW_WIDTH // 1, (i + 1) * 50)

            # draw the text surface on the screen
            self.screen.blit(self.text_surface, self.text_rect)
            self.screen.blit(self.function_surface, self.function_rect)
            self.screen.blit(self.argument_surface, self.argument_rect)

            # update the screen
            pygame.display.flip()

    def change_function(self):
        # use this to change a list of functions that we are actually running
        pass
    def run(self):
        # make a dictionary displaying dictionary with 1-10 as keys and the values
        # being the code that the students program, and edit that dictionary perhaps and
        # redisplay the code. Might actually not be worth it. Might be too confusing
        # since i could make 2 lists and have the first one which is the row numbers displayed once
        # whereas the second is refreshed constantly, displaying new stuff over and over again.

        running = True
        self.display_text()
        while running:

            # this comes before the enumerate 
            for event in pygame.event.get():
                ################
                # have functionality right here for if a button is pressed ? maybe arrow keys for reading
                # down the lines????
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    self.delete_text()
                    self.function_and_argument_list[2]["function"] = "mouse"
                    self.display_text()
            
            #############
            # have an if statement here if there was a change in voltage for any of the analog pins
            # now have or dont have a current flowing anymore, update the dictionary accordingly

            # runs the code to display all the text 

            
            

        # quit Pygame
        pygame.quit()

    # does a class for gui's need to intake a window?
    # as in should i instantiate a window first and then put it into my gui class?

p = GUI()
p.run()