def main():
	limit = int(input("Insert an integer: "))
	file = open('words.txt')
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
