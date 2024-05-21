def main():
	string = input("Insert a string: ")
	num = int(input("Insert an integer: "))
	len_str = len(string) - num

	if num >= len(string) or num <= 0:
		print("Error: index out of range")
	else:
		while num <= len_str:
			print(string[num], end="")
			num += 1

if __name__ == "__main__":
	main()
