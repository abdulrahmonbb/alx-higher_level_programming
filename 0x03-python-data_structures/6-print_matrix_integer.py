#!/usr/bin/python3

def print_matrix(matrix=[[]]):
	for row in matrix:
		print(" ".join("{:d}".format(num) for num in row))
