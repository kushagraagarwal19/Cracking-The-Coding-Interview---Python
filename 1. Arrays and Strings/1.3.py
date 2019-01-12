def URLify(string,trueLength):
    answer = ''
    index = 0
    while(index < trueLength):
        if string[index] != ' ':
            answer = answer + string[index]
        if string[index] == ' ':
            answer = answer + '%20'
        index += 1
    return answer

a = URLify('Mr John Smith    ',13)
print(a)