import pickle

def count_word_lengths(filename):
	word_lengths = {}
	with open(filename, 'r') as file:
		for line in file:
			words = line.split()
			for word in words:
				length = len(word)
				if length in word_lengths:
					word_lengths[length] += 1
				else:
					word_lengths[length] = 1
	return word_lengths

def dump_dict_to_file(dictionary, filename):
	with open(filename, 'wb') as file:
		pickle.dump(dictionary, file)

def main():
	word_lengths = count_word_lengths('words.txt')
	dump_dict_to_file(word_lengths, 'word_count.pickle')

if __name__ == "__main__":
	main()
