#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
		squared = map(lambda i: i ** 2, matrix)
		squared_list = list(squared)
		return squared_list

