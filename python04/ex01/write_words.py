def main():
	limit = int(input("Insert an integer: "))
	file = open('words.txt')
	new_file = open('long_words.txt', 'w+')
	read = file.readlines()
	print(f"The words longer than {limit} have been written on \"long_words.txt\"")
	for line in read:
		line = line.strip()
		words = line.split()
		for word in words:
			if len(word) > limit:
				new_file.write(word)
				new_file.write("\n")
	new_file.close()

if __name__ == "__main__":
	main()
