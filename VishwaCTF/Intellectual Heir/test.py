def str_to_ass(input_string):
    ass_values = []
    for char in input_string:
        ass_values.append(str(ord(char)))
    ass_str = ''.join(ass_values)
    return ass_str

print(str_to_ass("aaacde"))