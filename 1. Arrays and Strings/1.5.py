def oneAway(string1, string2):
    array1 = 26 * [0]
    array2 = 26 * [0]

    for each in string1:
        array1[ord(each) - ord('a')] += 1

    for each in string2:
        array2[ord(each) - ord('a')] += 1

    # for index in range(26):
    #     print(array1[index], end = '')
    # print()
    # for index in range(26):
    #     print(array2[index], end = '')
        
    difference = 0
    for index in range(26):
        difference += abs(array1[index] - array2[index])
        
    return True if difference <= 3 else False

a = oneAway('bake', 'bake')
print(a)