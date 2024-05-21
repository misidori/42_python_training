import sys

def find_min(arguments, argc):
	i = 0
	index = 0
	minimum = int(arguments[0])
	while i < argc:
		current_number = int(arguments[i])
		if minimum > current_number:
			minimum = current_number
			index = i
		i += 1
	ret_values = (minimum, index)
	return ret_values

def find_max(arguments, argc):
	i = 0
	index = 0
	maximum = int(arguments[0])
	while i < argc:
		current_number = int(arguments[i])
		if maximum < current_number:
			maximum = current_number
			index = i
		i += 1
	ret_values = (maximum, index)
	return ret_values

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	minimum = ()
	maximum = ()
	if argc == 0:
		print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
		return 1
	else:
		minimum = find_min(arguments, argc)
		maximum = find_max(arguments, argc)
	print(f"The min is {minimum[0]} and its position is {minimum[1]}")
	print(f"The max is {maximum[0]} and its position is {maximum[1]}")

if __name__ == "__main__":
	main()
