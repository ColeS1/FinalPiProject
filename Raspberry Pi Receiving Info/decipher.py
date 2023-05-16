# Ping_Theremin.py

from cyberbot import *
from ping import *
from time import sleep

my_string = "f4r89wpx34r5"

def parser(a_string):
    '''returns a list of tuples corresponding to functionality and arguments'''
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
            elif a_string[i] == " ":
                results.append((" ", " "))
            else:
                while j < len(a_string) and a_string[j].isdigit():
                    j += 1
                results.append((a_string[i], a_string[i+1:j]))
                i = j   
    return results
OUTPUT = parser(my_string)

index = 0      # index
j = 0          # subindex

def go_forward(time):
    bot(18, 19).servo_speed(54, -57)
    sleep(int(time))
    bot(18, 19).servo_speed(0, 0)

def go_reverse(time):
    bot(18, 19).servo_speed(-54, 57)
    sleep(int(time))
    bot(18, 19).servo_speed(0, 0)

def turn_right(time):
    bot(18, 19).servo_speed(50, 50)
    sleep(int(time))
    bot(18, 19).servo_speed(0, 0)

def turn_left(time):
    bot(18, 19).servo_speed(-50, -50)
    sleep(int(time))
    bot(18, 19).servo_speed(0, 0)

def check_space():
    '''determine what the number of elements of a loop or conditional is'''
    global index
    global j

    j = 0
    while OUTPUT[j][0] != " ":
        j += 1
    
def execute_until_space():
    '''excecute commands in loops and conditionals until space is reached'''
    global j
    global index

    j = index + 1
    while OUTPUT[j][0] != " ":
        dict_[OUTPUT[j][0]](OUTPUT[j][1])
        j += 1

def for_function(i):
    '''repeats the code corresponding for the number of times corresponding to the letter o'''
    global index
    for _ in range(int(i)):
        execute_until_space()

    index += int(OUTPUT[index][1])

def while_function(args):
    global index
    global j
    condition = True
    check_space()
    while condition:
        dist = ping(16).distance('cm')
        if args[1] == "<":
            if dist < int(args[2:]):
                execute_until_space()
                dist += 1
            else:
                condition = False
                
        elif args[1] == ">":
            if dist > int(args[2:]):
                execute_until_space()
            else:
                condition = False
    index += j - index       

def if_function(args):
    global index
    global j
    condition = True
    check_space()
    if condition:
        dist = ping(16).distance('cm')
        if args[1] == "<":
            if dist < int(args[2:]):
                execute_until_space()
                
        elif args[1] == ">":
            if dist > int(args[2:]):
                execute_until_space()
    index += j - index

def space(i):
    '''skip space'''

dict_ =    {"f":go_forward, 
            "e":go_reverse, 
           "r":turn_right,
           "l":turn_left,
           "o":for_function,
           "w":while_function,
           "s":if_function,
           " ":space
        }

def functionality(OUTPUT):
    '''executes program'''
    global index
    while index < len(OUTPUT):
        dict_[OUTPUT[index][0]]((OUTPUT[index][1]))
        index += 1

# ('f','2'),('r','1'),('o', '3'), ('f', '5'), ('r', '7'), (' ', ' '), ('e', '4'), 
OUTPUT = [('f','2'),('r','1'), ('s', 'p>8'), ('f', '1'), ('r','2'), (' ', ' '), (' ', ' '), ('l', '1')]
functionality(OUTPUT)