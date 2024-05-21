def main():
	name_file = input("Insert file name: ")
	try:
		file = open(name_file)
	except:
		print("Error! The specified file does not exist!")
		return 1
	limit = int(input("Insert an integer: "))
	read = file.readlines()
	print(f"The words longer than {limit} are the following:")
	for line in read:
		line = line.strip()
		words = line.split()
		for word in words:
			if len(word) > limit:
				print(word)

if __name__ == "__main__":
	main()
