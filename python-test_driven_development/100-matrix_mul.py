#!/usr/bin/python3
"""
This module contain a function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    multipy 2 matrix
    """
    er_message = "{0} must be a list"
    if not isinstance(m_a, list):
        raise TypeError(er_message.format("m_a"))
    if not isinstance(m_b, list):
        raise TypeError(er_message.format("m_b"))  
    if not all(isinstance(ele, list) for ele in m_a):
       raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    ma_col_len = len(m_a[0])
    for row in m_a:
        if len(row) !=ma_col_len:
            raise TypeError("each row of m_a must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    mb_col_len = len(m_b[0])
    for row in m_b:
        if len(row) !=mb_col_len:
            raise TypeError("each row of m_b must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    try:
        result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m_b)] for X_row in m_a]
        return result
    except:
        raise ValueError("m_a and m_b can't be multiplied")