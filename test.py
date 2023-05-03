DEBUG = False

string = "f9r67wp+10f4"


#########################################
def go_forward():
    print(f"I went forward for")

def go_reverse():
    print(f"I went reverse for ")

def turn_right():
    print(f"I went right for ")

def turn_left():
    print(f"I went left for ")

def for_():
    """loop for number of times"""

def while_():
    """loop under a condition"""

def if_():
    """action under a condition"""


#########################################

def parse_string(a_string):
    results = []
    current_result = {}

    for i in range(len(a_string)):
        if a_string[i].isalpha():
            if a_string[i] == 'w':
                results.append(current_result)
                current_result = {}
            else:
                j = i + 1
                while j < len(a_string) and a_string[j].isdigit():
                    j += 1
                current_result[a_string[i]] = a_string[i+1:j]

    results.append(current_result)
    return results

dict1 = parse_string(string)
print(dict1)


for i in dict1:
    pass

dict_ =    {"f":go_forward(), 
           "e":go_reverse(), 
           "r":turn_right(),
           "l":turn_left(),
           "o":for_(),
           "w":while_(),
           "s":if_()
        }





# def check_func(string):
#     for i in range(len(string)):
#         if string[i].isalpha():
#             if DEBUG:
#                 print(string[i])
# OUTPUT: letters in the string

def check_func(a_string):
    result = {}

    for i in range(len(a_string)):
        if a_string[i].isalpha():
            j = i + 1
            while j < len(a_string) and a_string[j].isdigit():
                j += 1
            result[a_string[i]] = a_string[i+1:j]

    return result

print(check_func(string))

