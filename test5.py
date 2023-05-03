# string = "f6r99wpy3f10 r3"
string = "f6r99"
string = "f9r67wf4"

def parser(string):

    results = []
    current_result = []

    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] == 'w':
                results.append(tuple(current_result))
                current_result = []
            else:
                j = i + 1
                while j < len(string) and string[j].isdigit():
                    j += 1
                current_result.append((string[i], string[i+1:j]))

    if current_result:
        results.append(tuple(current_result))

    return results

list_of_tuples = parser(string)
print(list_of_tuples)