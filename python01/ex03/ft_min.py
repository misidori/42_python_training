import sys

def my_min(x=0, y=0, z=0):
	if x is not None and y is not None and z is not None:
		minimum = x
		if minimum > y:
			minimum = y
		if minimum > z:
			minimum = z
		return minimum
	else:
		return None

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	if argc != 3:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
	else:
		x = float(arguments[0])
		y = float(arguments[1])
		z = float(arguments[2])
		print(f"The min is: {my_min(x, y, z)}")

if __name__ == "__main__":
	main()
