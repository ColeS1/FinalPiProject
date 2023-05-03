
def parser(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            i += 1
        else:
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            if j > i + 1:
                result.append((s[i], int(s[i+1:j])))
            else:
                result.append((s[i], ''))
            i = j
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

#create parser with special case of w and i
# 