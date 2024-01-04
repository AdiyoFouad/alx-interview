#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''

def calculate_binomial_coefficient(n, k):
    '''Calculates the binomial coefficient "n choose k".
    '''
    if k == 0 or k == n:
        return 1
    return calculate_binomial_coefficient(n - 1, k - 1) + calculate_binomial_coefficient(n - 1, k)

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = [calculate_binomial_coefficient(i, j) for j in range(i + 1)]
        triangle.append(line)
    return triangle
