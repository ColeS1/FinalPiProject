output = {'f': '6', 'r': '99'}

for key in output:
    output[key] = (output[key], 'new_element')
    
print(output)

# OUTPUT: {'f': ('6', 'new_element'), 'r': ('99', 'new_element')}