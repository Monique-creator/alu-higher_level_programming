#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    
    Args:
        n: number of rows to generate
        
    Returns:
        List of lists representing Pascal's triangle, empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Create new row
        row = []
        
        for j in range(i + 1):
            # First and last elements are always 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Sum of two elements from previous row
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        triangle.append(row)
    
    return triangle
