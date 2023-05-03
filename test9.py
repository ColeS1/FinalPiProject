def extract_while():
    '''receive args of while'''
    for i in range(len(OUTPUT)):
        if OUTPUT[i][0] == 'w':
            return OUTPUT[i][1]
    return False

def extract_if():
    '''receive args for if'''
    for i in range(len(OUTPUT)):
        if OUTPUT[i][0] == 'i':
            return OUTPUT[i][1]
    return False

def go_forward(time):
    print(f"go forward for time: {time}")

def go_reverse(time):
    print(f"go reverse for time: {time}")

def turn_right(time):
    print(f"turn right for time: {time}")

def turn_left(time):
    print(f"turn left for time: {time}")

def for_function(iterations, final_output):
    '''repeats the code corresponding to o in the first element in the tuple '''
    for _ in range(int(iterations)):
        functionality(final_output)

def while_function(args):
    '''run while function'''
    while args[0]:
        functionality(args[1])

def if_function(args):
    """same as while function"""
    while args[0]:
        functionality(args[1])

dict_ = {
    "f": go_forward, 
    "e": go_reverse, 
    "r": turn_right,
    "l": turn_left,
    "o": for_function,
    "w": while_function,
    "s": if_function
}

def functionality(OUTPUT):
    i = 0

    while i < len(OUTPUT):

        if OUTPUT[i][0] == "w":
            i += 1
            while OUTPUT[i][0] != " ":
                args = extract_while()
                while_function(args)
                i += 1

        elif OUTPUT[i][0] == "s":
            i += 1
            while OUTPUT[i][0] != " ":
                args = extract_if()
                if_function(args)
                i += 1

        elif OUTPUT[i][0] == "o":
            iterations = int(OUTPUT[i][1])
            final_output = []
            j = i + 1
            while j < len(OUTPUT) and OUTPUT[j][0] != " ":
                final_output.append(OUTPUT[j])
                j += 1
            for_function(iterations, final_output)
            i = j

        else:
            dict_[OUTPUT[i][0]](OUTPUT[i][1])
            i += 1

OUTPUT = [('f','9'),('r','99'),('o', '3'), ('f', '5'), ('r', '7'), (' ', ' '), ('f', '4'), (" ", " ")]
functionality(OUTPUT)
