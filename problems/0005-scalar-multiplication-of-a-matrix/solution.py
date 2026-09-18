import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	mul = [[scalar]*len(matrix[0])]*len(matrix)

	return (np.array(matrix) * np.array(mul)).tolist()
