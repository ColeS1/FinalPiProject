class Block:
    buttons =  {17: "1",
                16: "2",
                13: "3",
                6: "4",
                5:"5",
                4: "6",
                26: "7",
                25: "8",
                24: "9",
                21: "0",
                27: "Run",
                12: "Lock",
                23: "Read",
                19: "Dist"}


class Forward(Block):

    def __init__ (self):
        pass

    def __str__(self):
        return "Forward"

class Reverse(Block):

    def __init__(self):
        pass

    def __str__(self):
        return "Reverse"

class TurnRight(Block):

    def __init__(self):
        pass

    def __str__(self):
        return "Turn Right"

class TurnLeft(Block):
    
    def __init__(self):
        pass

    def __str__(self):
        return "Turn Left"

class WhileLoop:

    def __init__(self):
        pass

    def __str__(self):
        return "While Loop"

class ForLoop(Block):

    def __init__(self):
        pass

    def __str__(self):
        return "For Loop"

class IfStatement:

    def __init__(self):
        pass

    def __str__(self):
        return "If Statement"

