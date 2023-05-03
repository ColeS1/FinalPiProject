
def go_forward():
    pass


string = "f9r67wf4"
def split_string(string, go_forward):
    results = []
    current_result = {}

    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] == 'w':
                results.append(current_result)
                current_result = {}
            else:
                j = i + 1
                while j < len(string) and string[j].isdigit():
                    j += 1
                key = string[i]
                value = string[i+1:j]
                current_result[key] = lambda v: go_forward(v) if v.isdigit() else v
                current_result[key](value)

    results.append(current_result)
    return results

print(split_string(string, go_forward=go_forward()))