def palindromePermutation(string):
    hashMap = {}
    for each in string:
        if each == ' ':
            continue
        if each in hashMap:
            hashMap[each] += 1
        else:
            hashMap[each] = 1

    countofOne = 0
    for each in hashMap:
        if hashMap[each] == 1:
            countofOne += 1