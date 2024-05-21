import sys

def trim(list_of_values=None):
	length = len(list_of_values)
	del list_of_values[len(list_of_values) - 1]
	del list_of_values[0]

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	if argc < 2:
		print("Error! You must insert at least 2 values")
		return 1
	trim(arguments)
	print("The new list is:", arguments[:])

if __name__ == "__main__":
	main()
