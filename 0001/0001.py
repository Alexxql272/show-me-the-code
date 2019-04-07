import random

# Generate a list include 0-9 and A-Z, 11-35 represent A-Z
element = 0
wordList = list()
while element <= 35:
    wordList.append(element)
    element += 1

i = 0
Codes = list()
num = int(input("Enter how many codes do you want:"))
while i < num:
    i += 1
    parameter = None
    Str = ''
    j = 0
    while j < 16:
        j += 1
        parameter = random.randint(0, 35)
        if parameter < 10:
            if j % 4 == 0 and j !=16:
                char = str(parameter) + '-'
            else:
                char = str(parameter)
        else:
            if j % 4 == 0 and j != 16:
                char = chr(parameter+55) + '-'
            else:
                char = chr(parameter+55)
        Str += char
    Codes.append(Str)

    hFile = open('data.txt', 'w')
    for code in Codes:
        print(code)
        hFile.write(code+'\n')
    hFile.close()
