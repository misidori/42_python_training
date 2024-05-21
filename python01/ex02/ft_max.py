import sys

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	i = 0
	if argc != 3:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
	else:
		max = float(arguments[0])
		while i < argc:
			if max < float(arguments[i]):
				max = float(arguments[i])
			i += 1
		print(f"The max is: {max}")

if __name__ == "__main__":
	main()
