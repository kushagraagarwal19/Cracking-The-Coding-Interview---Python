def spiral(matrix):
    rowsActual = len(matrix)
    columnsActual = len(matrix[0])
    elemTraverseHmap = {}
    answer = []
    direction = 'R'
    # Start row, and column index
    i = j = 0
    # Ending row, and column index
    k = rowsActual-1
    l = columnsActual-1
    # Iterator
    m = 0

    for index in range(0,rowsActual*columnsActual):
        # if index == 8:
        #         print ('hello')
        if direction == 'R':
            
            if (str(i) + ',' + str(m)) not in elemTraverseHmap and m <= l:
                answer.append(matrix[i][m])
                elemTraverseHmap[str(i) + ',' + str(m)] = 1
                m += 1
            else:
                direction = 'D'
                i += 1
                m = i
                
        if direction == 'D':
            if (str(m) + ',' + str(l)) not in elemTraverseHmap and m <= k:
                answer.append(matrix[m][l])
                elemTraverseHmap[str(m) + ',' + str(l)] = 1
                m += 1
            else:
                direction = 'L'
                l = l-1
                m = l
        if direction == 'L':
            if (str(k) + ',' + str(m)) not in elemTraverseHmap and m >= j:
                answer.append(matrix[k][m])
                elemTraverseHmap[str(k) + ',' + str(k)] = 1
                m = m-1
            else:
                direction = 'U'
                k = k-1
                m = k
        if direction == 'U':
            if (str(m) + ',' + str(j)) not in elemTraverseHmap and m >= i:
                answer.append(matrix[m][j])
                elemTraverseHmap[str(m) + ',' + str(j)] = 1
                m = m - 1
            else:
                direction = 'R'
                i = i + 1
                m = i
        print(answer)
        print(index)
    # print(answer)
    return elemTraverseHmap

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16] 
    ]

# matrix = [
#         [1],
#         [5],
#         [9],
#         [13] 
#     ]

answer = spiral(matrix)
for each in answer:
    print(each)