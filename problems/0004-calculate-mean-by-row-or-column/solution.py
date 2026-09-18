import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix = np.array(matrix)
	if mode == 'column':
		matrix = np.transpose(matrix)
	
	means = np.zeros(len(matrix))

	for i in range(len(matrix)):
		for y in range(len(matrix[0])):
			means[i] += matrix[i][y]
		means[i] /= len(matrix[0])

	return means