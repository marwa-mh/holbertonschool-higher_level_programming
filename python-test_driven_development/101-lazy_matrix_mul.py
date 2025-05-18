#!/usr/bin/python3
"""
This module contain a function lazy_matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrixes using numpy
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")   
    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    ma_col_len = len(m_a[0])
    if ma_col_len == 0:
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    for row in m_a:
        if len(row) !=ma_col_len:
            raise TypeError("setting an array element with a sequence.")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("invalid data type for einsum")
    mb_col_len = len(m_b[0])
    if mb_col_len == 0:
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")
    for row in m_b:
        if len(row) !=mb_col_len:
            raise TypeError("setting an array element with a sequence.")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("invalid data type for einsum")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = np.dot(m_a, m_b)
    return result