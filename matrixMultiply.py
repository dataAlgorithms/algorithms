#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1. ijk-algorithm
'''
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", dest="filename", default="2000.in",
     help="input file with two matrices", metavar="FILE")
(options, args) = parser.parse_args()

def read(filename):
    lines = open(filename, 'r').read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B

def printMatrix(matrix):
    for line in matrix:
        print "\t".join(map(str,line))

def standardMatrixProduct(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def ijkAlgoMain():

    A, B = read(options.filename)
    C = standardMatrixProduct(A, B)
    printMatrix(C)
    
'''
2. ikj algorithms
'''
def ikjMatrixProduct(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def ikjAlgoMain():
    print ''
    A, B = read(options.filename)
    C = ikjMatrixProduct(A, B)
    printMatrix(C)
    
'''
3. Psyco ikj-algorithm


def psycoIkjAlgoMain():
    import psyco
    psyco.full()
    print ''
    A, B = read(options.filename)
    C = ikjMatrixProduct(A, B)
    printMatrix(C)
'''
    
'''
4. Numpy
'''
import numpy

def printMatrixNumpy(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print "\t".join(map(str,line))

def numpyMain():
    print ''
    A, B = read(options.filename)
    A = numpy.matrix(A)
    B = numpy.matrix(B)
    C = A * B # easy and intuitive, isn't it?
    printMatrixNumpy(C)
    
'''
5. scipy
'''

import scipy

def printMatrixScipy(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print "\t".join(map(str,line))

def scipyMain():
    print ''
    A, B = read(options.filename)
    A = scipy.matrix(A)
    B = scipy.matrix(B)
    C = A * B # easy and intuitive, isn't it?
    printMatrixScipy(C)
    
'''
6. strassenAlgorithms
'''
from optparse import OptionParser
from math import ceil, log

import random
random.seed(1234)

def createRandomMatrix(n):
    maxVal = 1000 # I don't want to get Java / C++ into trouble
    matrix = []
    for i in xrange(n):
        matrix.append([random.randint(0,maxVal) for el in xrange(n)])
    return matrix

def saveMatrix(matrixA, matrixB, filename):
    f = open(filename, 'w')
    for i, matrix in enumerate([matrixA, matrixB]):
        if i != 0:
            f.write("\n")
        for line in matrix:
            f.write("\t".join(map(str, line)) + "\n")

def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def strassenR(A, B):
    """
    Implementation of the strassen algorithm, similar to
    http://en.wikipedia.org/w/index.php?title=Strassen_algorithm&oldid=498910018#Source_code_of_the_Strassen_algorithm_in_C_language
    """
    n = len(A)

    if n <= LEAF_SIZE:
        return ikj_matrix_product(A, B)
    else:
        # initializing the new sub-matrices
        new_size = n/2
        a11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        b11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        aResult = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        bResult = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + new_size]    # top right
                a21[i][j] = A[i + new_size][j]    # bottom left
                a22[i][j] = A[i + new_size][j + new_size] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + new_size]    # top right
                b21[i][j] = B[i + new_size][j]    # bottom left
                b22[i][j] = B[i + new_size][j + new_size] # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassenR(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = add(a21, a22)      # a21 + a22
        p2 = strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract(b12, b22) # b12 - b22
        p3 = strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract(b21, b11) # b21 - b11
        p4 =strassenR(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = add(a11, a12)      # a11 + a12
        p5 = strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)

        aResult = subtract(a21, a11) # a21 - a11
        bResult = add(b11, b12)      # b11 + b12
        p6 = strassenR(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = subtract(a12, a22) # a12 - a22
        bResult = add(b21, b22)      # b21 + b22
        p7 = strassenR(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        aResult = add(p1, p4) # p1 + p4
        bResult = add(aResult, p7) # p1 + p4 + p7
        c11 = subtract(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = add(p1, p3) # p1 + p3
        bResult = add(aResult, p6) # p1 + p3 + p6
        c22 = subtract(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                C[i][j] = c11[i][j]
                C[i][j + new_size] = c12[i][j]
                C[i + new_size][j] = c21[i][j]
                C[i + new_size][j + new_size] = c22[i][j]
        return C


def strassen(A, B):
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd
    # matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in xrange(m)] for j in xrange(m)]
    BPrep = [[0 for i in xrange(m)] for j in xrange(m)]
    for i in xrange(n):
        for j in xrange(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenR(APrep, BPrep)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            C[i][j] = CPrep[i][j]
    return C
    
if __name__ == "__main__":
    ijkAlgoMain()
    ikjAlgoMain()
    numpyMain()
    scipyMain()
    
    print ''
    n = 3
    matrixA = createRandomMatrix(n)
    matrixB = createRandomMatrix(n)
    saveMatrix(matrixA, matrixB, "2000.in")

    parser = OptionParser()
    parser.add_option("-i",
                      dest="filename",
                      default="2000.in",
                      help="input file with two matrices",
                      metavar="FILE")
    parser.add_option("-l",
                      dest="LEAF_SIZE",
                      default="8",
                      help="when do you start using ikj",
                      metavar="LEAF_SIZE")
    (options, args) = parser.parse_args()

    LEAF_SIZE = options.LEAF_SIZE
    A, B = read(options.filename)
    
    C = strassen(A, B)
    print_matrix(C)
