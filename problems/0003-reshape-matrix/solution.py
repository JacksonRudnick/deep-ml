import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if not (len(a) * len(a[0])) == (new_shape[0] * new_shape[1]):
		return []

	reshaped_matrix = np.zeros(new_shape)

	orow = 0
	ocol = 0

	for row in range(new_shape[0]):
		for col in range(new_shape[1]):
			reshaped_matrix[row][col] = a[orow][ocol]
			ocol += 1
			if ocol == len(a[0]):
				ocol = 0
				orow += 1


	return reshaped_matrix.tolist()