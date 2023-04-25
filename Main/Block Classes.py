from abc import ABC, abstractmethod

class Block(ABC):

    def __init__(self, name, analog_value):

        self.name = name
        self.analog_value = analog_value

        #Depending on the GUI, figure out what shape size to make everything (such as if the blocks will be presented as rectangles on the GUI with their respective names)
        # So we'll eventually need a self.width and self.height in here along with any designs to make the rectangles nicer (so long as it is for all of them, if we want to
        # do something where for loop will be a certain color, then we can put in the constructor for the Block class the color of the block)

    @abstractmethod
    def code_generator(self, argument1= None, argument2 = None): #To make sure all of the classes have a way to allow this to basically make it into code based on the arguments
                                                                 #that will be given.

        raise NotImplementedError
    

class Forward(Block):

    pass

class Reverse(Block):

    pass

class TurnRight(Block):

    pass

class TurnLeft(Block):

    pass

class WhileLoop(Block):

    pass

class ForLoop(Block):

    pass

class IfStatement(Block):

    pass



