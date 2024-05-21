import sys

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	argv = [0] * argc
	i = 0
	while i < argc:
		argv[i] = int(arguments[i])
		i +=1
	if argc < 2:
		print("Error! You must insert at least 2 numbers")
		return 1
	arguments_sorted = sorted(argv, reverse = True)
	if argv == arguments_sorted:
		print("The inserted sequence is sorted!")
	else:
		print("The inserted sequence is not sorted!")
		print(f"The correct order is {arguments_sorted}")

if __name__ == "__main__":
	main()
