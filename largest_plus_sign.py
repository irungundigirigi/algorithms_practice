#!/usr/bin/env python3

"""
Given a matrix of binary values, returns the size of the largest + sign 
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
        left[i][0] = mat[i][0]

    """ populate the matrixes"""
    for i in range(size):
        for j in range(1,size):
            if m[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1
    for i in left:
        print(i)

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
    print('left matrix')
    print(get_largest_plus(mat))



