#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''

def pascal_triangle(n, i=0, triangle=None):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if triangle is None:
        triangle = []

    if type(n) is not int or n <= 0 or i >= n:
        return triangle

    line = [1 if j == 0 or j == i else triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(i + 1)]
    triangle.append(line)

    return pascal_triangle(n, i + 1, triangle)
