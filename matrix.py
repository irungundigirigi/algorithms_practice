#!/usr/bin/env python3

def get_unique(m):
    unique_elements = {}
    for row in m:
        for element in row:
            if element not in unique_elements:
                unique_elements[element] = 1
            else:
                unique_elements[element] += 1

    for i, c in unique_elements.items():
        if c == 1:
            print(i)

m = [[1, 4, 8, 12], [2, 4, 6, 8]]
get_unique(m)

    