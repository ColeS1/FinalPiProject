def parser(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if input_string[i].isalpha():
            letter = input_string[i]
            i += 1
            if letter == 'w':
                result.append((letter, input_string[i+1:]))
            while i < len(input_string) and input_string[i].isdigit():
                letter += input_string[i]
                i += 1
            result.append((letter[0], int(letter[1:])))
        else:
            i += 1
    return result

string = "f6r99wpy3f10 r3"
string = "f6r99"
string = "f9r67wf4"

tuples = parser(string)
print(tuples)

for i in range(len(tuples)):
    if tuples[i][0] == "w":
        pass



def while_if_args():
    pass