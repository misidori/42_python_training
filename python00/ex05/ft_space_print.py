def main():
	string = input("Insert a string: ")
	len_str = int(len(string))
	to_print = len_str - 20
	if len_str > 20:
		while to_print < len_str:
			print(string[to_print], end="")
			to_print += 1
	else:
		while len_str < 20:
			print(" ", end="")
			len_str += 1
		print(string)

if __name__ == "__main__":
	main()
