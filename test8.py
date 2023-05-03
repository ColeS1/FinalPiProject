string = "f4r89wpx34"
def parser(string):
    result = []
    for i in range(len(string)):
        temp = ""
        while i < len(string):
            if string[i].isalpha():
                letter = string[i]
                while string[i+1].isdigit():
                    temp += string[i+1]
                    i += 1
                result.append((letter, temp))
                i += 1
                temp = ""

OUTPUT = parser(string)
print(OUTPUT)






