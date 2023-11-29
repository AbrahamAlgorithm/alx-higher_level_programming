#!/usr/bin/python3
"""multiplication of two matrices using
numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices using numpy

    Args:
        m_a: the list of list
        m_b: the list of list
    Returns:
        the new matrix
    """
    return (np.matmul(m_a, m_b))
