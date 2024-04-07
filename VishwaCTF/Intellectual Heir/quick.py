#cos
first=""
with open('file1.txt', 'r') as file:
    for line in file:
        if int(line[0]) == 1:
            first=''.join([first,"0"])
        else:
            first=''.join([first,"1"])
print(first)

#sin
print()
second=""
with open('file2.txt', 'r') as file:
    for line in file:
        if int(line[0]) == 0:
            second=''.join([second,"0"])
        else:
            second=''.join([second,"1"])
            
print(second)

p=int(first, base=2)
q=int(second,base=2)

enc=4400037514278889258479265625258024039636437755883377709505596356049534358755375772484057042989024750972247184288820831886430459963472328358741858934783775986591400972020736548834642094922678189447202173710409868474198821576627330424767999152339702779346380
e=65537
d= pow(e,-1,(p-1)*(q-1))

m=pow(enc, d, p*q)


def ass_to_str(input_string):
    result = ''
    for i in range(0, len(input_string), 2):
        code_point = int(input_string[i:i+2])

        result += chr(code_point)
    return result


print(ass_to_str(str(m)))