string = "f4r89wpx34r5"
# what if the string has a space
# what if the string has a for loop

def parser(a_string):
    results = []
    i = 0
    
    while i < len(a_string):
        if a_string[i].isalpha():
            j = i + 1
            if a_string[i] == "w" or a_string[i] == "s":
                j += 2
                while j < len(a_string) and a_string[j].isdigit():
                    j += 1
                results.append((a_string[i], a_string[i+1:j]))
                i = j
            if a_string[i] == " ":
                results.append((" ", " "))
            else:
                while j < len(a_string) and a_string[j].isdigit():
                    j += 1
                results.append((a_string[i], a_string[i+1:j]))
                i = j   
    return results

OUTPUT = parser(string)
print(OUTPUT)

def extract_while():
    '''recieve args of while'''
    for i in range(len(OUTPUT)):
        if OUTPUT[i][0] == 'w':
            return OUTPUT[i][1]
    return False
def extract_if():
    '''recieve args for if'''
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
    for _ in range(iterations):
        pass

args = ["ping", '<', 34]
def while_function():
    '''run while function'''
    while args[0]:
        pass
        
 
def if_function():
    """same as while function"""

dict_ =    {"f":go_forward, 
            "e":go_reverse, 
           "r":turn_right,
           "l":turn_left,
           "o":for_function,
           "w":while_function,
           "s":if_function
        }


def functionality(OUTPUT):
    i = 0

    while i < len(OUTPUT):

        if OUTPUT[i][0] == "w":
            i += 1
            ping = "the sensor"
            while ping < 3:
                j = i
                while OUTPUT[i][0] != " ":
                    dict_[OUTPUT[j][0]](OUTPUT[j][1])
                    j += 1

        elif OUTPUT[i][0] == "s":
            i += 1

            while OUTPUT[i][0] != " ":
                if_function()
                dict_[OUTPUT][i][0](OUTPUT[i][1])
                i += 1

        elif OUTPUT[i][0] == "o":
            for _ in range(int(OUTPUT[i][1])):
                j = i + 1

                while OUTPUT[j][0] != " ":
                    dict_[OUTPUT[j][0]](OUTPUT[j][1])
                    j += 1

            i += int(OUTPUT[i][1])

        elif OUTPUT[i][0] == " ":
            i += 1
            
        else:
            dict_[OUTPUT[i][0]](OUTPUT[i][1])
            i += 1

OUTPUT = [('f','9'),('r','99'),('o', '3'), ('f', '5'), ('r', '7'), (' ', ' '), ('f', '4'), ('w', 'px34'), ('f', '4'), ('r','45'), ('r','1')]
print(OUTPUT)
functionality(OUTPUT)

# add space for if while and for


######################### MAIN ###########################
if extract_while() != False:
    while_function(extract_while())


# have a list of dictionaries that is constantly updating
# have the code for the gui sending over a single command and the line that the command is on whenever something changes
# that way we can stay under the amount of characters that we need, base is going to have none for line