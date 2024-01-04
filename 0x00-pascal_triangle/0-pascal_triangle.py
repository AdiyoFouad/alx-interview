#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        line = [1 if j == 0 or j == i else line[j - 1] + line[j] for j in range(i + 1)]
        triangle.append(line)

    return triangle
