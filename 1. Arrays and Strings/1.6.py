def stringCompression(string):
    if len(string) <=1:
        return string
    start = string[0]
    count = 0
    answer = ''
    compCount = 0
    for each in string:
        if each == start:
            count+= 1
        else:
            answer += start + str(count)
            start = each
            count = 1
    answer += start + str(count)
    return string if len(string) < len(answer) else answer

a = stringCompression('abc')
print(a)