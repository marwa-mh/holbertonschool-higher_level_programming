#!/usr/bin/python3
import numpy as np
"""
This module contain a function lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrixes using numpy
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")  
    if not all(isinstance(ele, list) for ele in m_a):
       raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    result = np.dot(m_a, m_b)
    return result