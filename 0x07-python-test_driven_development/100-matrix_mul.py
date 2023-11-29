#!/usr/bin/python3
"""
multiplication of two matrices
"""


def matrix_mul(m_a, m_b):
    """multiplication of two matrices

    Args:
        m_a : the first matrix(list of list)
        m_b : the second matrix(list of list)

    Raises:
        TypeError: if matrix...
        ValueError: if matrix...

    Return:
        the new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all((isinstance(i, list) for i in m_a)):
        raise TypeError('m_a must be a list of lists')
    if not all((isinstance(i, list) for i in m_b)):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(j, int) or
                isinstance(j, float))
               for j in [a for i in m_a for a in i]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(j, int) or
                isinstance(j, float))
               for j in [a for i in m_a for a in i]):
        raise TypeError("m_b should contain only integers or floats")
    if not all((len(a) == len(m_a[0])) for a in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all((len(b) == len(m_b[0])) for b in m_b):
        raise TypeError("each row of m_b must be of the same size")
    c_len_a = len(m_a[0])
    len_a = len(m_a)
    c_len_b = len(m_b[0])
    len_b = len(m_b)
    if c_len_a != len_b:
        raise ValueError("m_a and m_b can't be multiplied")
    transpose_b = []
    for i in range(c_len_b):
        b_list = []
        for j in range(len_b):
            b_list.append(m_b[j][i])
        transpose_b.append(b_list)

    new_matrix = []
    for a in m_a:
        m_list = []
        for b in transpose_b:
            ans = 0
            for k in range(len(transpose_b[0])):
                ans += a[k] * b[k]
            m_list.append(ans)
        new_matrix.append(m_list)
    return (new_matrix)
