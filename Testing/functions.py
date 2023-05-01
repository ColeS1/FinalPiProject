def forward():
    pass

def while_():
    pass


code = {"a": forward(), "b" : while_()}
codelist = ["a", "b", "c"]

sent = "bpg7a10t"

def parser(string):
    empty_list = []
    last_letter_index = 0
    for i in range(len(string)):

        if string[i] == "t":

            last_letter_index = i
            empty_list.append("end_of_loop")

        if i != 0 and string[i] in codelist:

            new_str = string[last_letter_index:i]
            empty_list.append(new_str)
            last_letter_index = i

        print(i)

    return empty_list

print(parser(sent))

