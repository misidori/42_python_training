def main():
	string = input("Insert a string: ")
	num = int(input("Insert an integer: "))
	len_str = len(string)
	if num >= len_str or num <= 0:
		print("Error: index out of range")
	else:
		print(string[num] + " " + string[len_str - num])

if __name__ == "__main__":
	main()
