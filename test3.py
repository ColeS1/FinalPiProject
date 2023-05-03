DEBUG = False

# "f6r99"
# "wp+3f10r3"
# string = "f6r99wpy3f10 r3"
string = "f6r99"

#########################################
def go_forward(time):
    print(f"go forward for time: {time}")

def go_reverse(time):
    print(f"go reverse for time: {time}")

def turn_right(time):
    print(f"turn right for time: {time}")

def turn_left(time):
    print(f"turn left for time: {time}")



    # INPUT: {'f': ' ', 'f': '6', 'r': '99'}


def while_():
    """loop under a condition"""


def if_():
    """action under a condition"""

#########################################

def parse_string(string):
    result = []

    for i in range(len(string)):
        if string[i].isalpha():
            # if string[i] == "w":
            #     pass
            # else:
            j = i + 1
            while j < len(string) and string[j].isdigit():
                j += 1
            result[string[i]] = string[i+1:j]

    return result

# OUTPUT = {'f': '6', 'r': '99'}

OUTPUT = (parse_string(string))
print(OUTPUT)

def for_(number):
    """loop for number of times"""
    print(f"loop for {number} of times")
    for _ in range(number-1):
        '''do the code '''
        for key, value in OUTPUT.items():
            value = (dict_[key](value), value)

dict_ =    {"f":go_forward, 
           "e":go_reverse, 
           "r":turn_right,
           "l":turn_left,
           "o":for_,
           "w":while_,
           "s":if_
        }

for key, value in OUTPUT.items():
    value = (dict_[key](value), value)

    # print(OUTPUT)


for key in OUTPUT:
    OUTPUT[key] = (dict_[key](OUTPUT[key]), OUTPUT[key])
    print(OUTPUT)
    # value = (go_forward(6), 6)


# split at the spaces




# def parse_string(a_string):

#     results = []
#     current_result = {}

#     for i in range(len(a_string)):
#         if a_string[i].isalpha():
#             if a_string[i] == 'w':
#                 results.append(current_result)
#                 current_result = {}
#             else:
#                 j = i + 1
#                 while j < len(a_string) and a_string[j].isdigit():
#                     j += 1
#                 current_result[a_string[i]] = a_string[i+1:j]

#     results.append(current_result)
#     return results

# dict1 = parse_string(string)
# print(dict1)