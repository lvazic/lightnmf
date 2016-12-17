import random
from numpy import array
from numpy import transpose
from numpy.matrixlib.defmatrix import matrix


def cost_function(a, b, l1=False):
    """Calculates L2-norm cost function.

    This function calculates element-wise sum of square of differences between
    the original matrix and reconstructed matrix.

    Args:
        a: A NumPy Matrix object representing the original matrix.
        b: A NumPy Matrix object representing the reconstructed matrix.
        l1: A boolean indicating whether or not L1 norm should be used instead
        of L2 norm.

    Returns:
        A double representing the value of cost function
    """
    cost = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            cost += abs(a[i, j] - b[i, j]) if l1 else pow(a[i, j] - b[i, j], 2)
    return cost


def factorize(data_matrix, num_of_factors=10, num_of_iterations=100, l1=False):
    """Factorizes data matrix and returns weights and factors matrices.

    This function initializes weights and factors matrices with random values
    from uniform distribution and then searches for best solution using
     multiplicative update rules.

    Args:
        data_matrix: A NumPy Matrix object representing the original matrix.
        num_of_factors: An integer representing number of factors to be
        extracted.
        num_of_iterations: Number of iterations for multiplicative update
        rules.
        l1: A boolean indicating whether or not L1 norm should be used instead
        of L2 norm.

    Returns:
        A tuple consisting out of weights and features matrices.
    """
    if data_matrix[data_matrix < 0]:
        raise ValueError('Matrix contains negative values.')

    w = matrix([[random.random() for i in range(num_of_factors)] for j in range(data_matrix.shape[0])])
    h = matrix([[random.random() for i in range(data_matrix.shape[1])] for j in range(num_of_factors)])

    for i in range(num_of_iterations):
        cost = cost_function(data_matrix, w * h, l1)
        if cost == 0:
            break
        hn = (transpose(w) * data_matrix)
        hd = (transpose(w) * w * h)
        h = matrix(array(h) * array(hn) / array(hd))
        wn = (data_matrix * transpose(h))
        wd = (w * h * transpose(h))
        w = matrix(array(w) * array(wn) / array(wd))
    return w, h
