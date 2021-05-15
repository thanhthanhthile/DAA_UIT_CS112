direction = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]


def isFirstChar(string, table, m, n):
    firstChar_index = []
    for i in range(m):
        for j in range(n):
            if table[i][j] == string[0]:
                firstChar_index.append([i, j])
    return firstChar_index


def search_word(A: list, k, m, n, string, table, x, y):
    if len(A) == len(string):
        return True
    for element in direction:
        x_new, y_new = x + element[0], y + element[1]
        if x_new >= 0 and x_new < m and y_new >= 0 and y_new < n:
            if ([x_new, y_new] not in A) and (table[x_new][y_new] == string[k]):
                # A.append([x_new, y_new])
                # print(x_new, y_new)
                # print(k)
                if search_word(A + [[x_new, y_new]], k + 1, m, n, string, table, x_new, y_new):
                    return True
    return False


string = input()
table = []  # table is matrix m x n
while True:
    row = input()
    if row == '.':
        break
    else:
        table.append(row)
m = len(table)
n = len(table[0])
firstChar=isFirstChar(string, table, m, n)
if len(firstChar) == 0:
    print('false')
else:
    for element in firstChar:
        A = [element]
        if search_word(A, 1, m, n, string, table, element[0], element[1]):
            print('true')
            break
        else:
            if firstChar.index(element)==len(firstChar)-1:
                print('false')

