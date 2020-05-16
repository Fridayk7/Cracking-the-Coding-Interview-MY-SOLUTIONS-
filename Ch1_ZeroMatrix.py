def zero_matrix(matrix):
    n = len(matrix)
    n2 = len(matrix[0])
    zero_row =[False for i in range(n)]
    zero_column = [False for i in range(n2)]

    for i in range(n):
        for j in range(n2):
            print(matrix[i][j])
            if matrix[i][j] == 0:
                zero_row[i] = True
                zero_column[j] = True

    for i in range(len(zero_row)):
        if zero_row[i]:
            matrix = zerofy_row(matrix,i)

    for i in range(len(zero_column)):
        if zero_column[i]:
            matrix = zerofy_column(matrix,i)

    return matrix

def zerofy_column(matrix,col):
    for i in range(len(matrix[0])):
        matrix[i][col] = 0
    return matrix

def zerofy_row(matrix,row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
    return matrix






