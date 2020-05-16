def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        begin, end = layer, n-1-layer
        for j in range(begin,end):
            # temporarily save value of top
            top = matrix[layer][j]

            # change top elements with elements on the left
            # -j-i is because we wanna work from the bottom up of the matrix
            matrix[layer][j] = matrix[-j-1][layer]

            # Change left elements with bottom elements
            # - layer -1 is because we want reach the bottom of each layer
            # -j-1 is because we are working from right to left
            matrix[-j-1][layer] = matrix[-layer-1][-j-1]

            # Change bottom elements with right elements
            matrix[-layer-1][-j-1] = matrix[j][-layer-1]

            # Change right elements with top elements
            matrix[j][-layer-1] = top

    return matrix










rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
