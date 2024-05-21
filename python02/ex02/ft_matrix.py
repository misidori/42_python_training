import sys

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)

	if argc != 2:
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return 1
	n = int(arguments[0])
	m = int(arguments[1])
	matrix = []
	i = 0
	while i < n:
		matrix.append([])
		j = 0
		while (j < m):
			matrix[i].append(float(input(f"Insert the element in position ({i}, {j}): ")))
			j += 1
		i += 1
	print("The inserted matrix is:")
	i = 0
	total_rows = [0] * n
	total_columns = [0] * m
	while i < n:
		j = 0
		while j < m:
			if j != 0:
				print(f", {matrix[i][j]}", end="")
			else:
				print(f"[{matrix[i][j]}", end="")
			if j == (m - 1):
				print("]")
			j += 1
		i += 1
	i = 0
	while i < n:
		j = 0
		while j < m:
			total_rows[i] += matrix[i][j]
			j += 1
		i += 1
	print(f"The sum over rows is: \n[", end="")
	i = 0
	while i < n:
		if i != 0:
			print(f", {total_rows[i]}", end="")
		else:
			print(f"{total_rows[i]}", end="")
		if i == (n - 1):
			print("]")
		i += 1
	j = 0
	while j < m:
		i = 0
		while i < n:
			total_columns[j] += matrix[i][j]
			i += 1
		j += 1
	print("The sum over columns is: \n[", end="")
	j = 0
	while j < m:
		if j != 0:
			print(f", {total_columns[j]}", end="")
		else:
			print(f"{total_columns[j]}", end="")
		if j == (m - 1):
			print("]")
		j += 1
	i = 0

if __name__ == "__main__":
	main()
