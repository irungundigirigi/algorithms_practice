#!/usr/bin/env python3

"""
Given a matrix of binary values, returns the arm-size of the largest + sign 
created by consecutive 1's.
Parameter: Binary matrix ()
"""
def get_largest_plus(m):

    """ Get the matrix size"""
    size = len(m)

    """Initialise auxiliary matrixes top, right, left and bottom. with all zeros"""
    left = [[0 for _ in range(size)] for _ in range(size)]
    right = [[0 for _ in range(size)] for _ in range(size)]
    bottom = [[0 for _ in range(size)] for _ in range(size)]
    top = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        left[i][0] = m[i][0]
        right[i][size - 1] = m[i][size - 1]
        top[0][i] = m[0][i]
        bottom[size -1][i] = m[size -1][i]

    """ populate the matrixes"""
    for i in range(size):
        for j in range(1,size):
            """left """
            if m[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1
            
            """ right matrix """
            if m[i][size - j] == 1:
                right[i][size - j -1] = right[i][size - j] + 1

            """ top matrix """
            if m[j][i] == 1:
                top[j][i] = top[j - 1][i] + 1

            """ bottom """
            if m[size -j -1][i] == 1:
                bottom[size - j -1][i] = bottom[size - j][i] + 1
    """ calculate the longest arm based min size on all sides"""
    longest_arm = 0
    for i in range(size):
        for j in range(size):
            arm = min(min(left[i][j], right[i][j]), min(top[i][j], bottom[i][j]))
            if arm > longest_arm:
                longest_arm = arm
    return longest_arm
if __name__=="__main__":
     
    # Binary Matrix of size N
    mat = [ [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
            [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
            [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 ],
            [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
            [ 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 0, 1, 1 ],
            [ 1, 1, 0, 0, 1, 0, 1, 0, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ]]
    print(get_largest_plus(mat))



