import sys

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	character_count = {}
	i = 0
	while i < len(arguments):
		arguments[i] = arguments[i].lower()
		i += 1
	if argc == 0:
		print("Error! No string given")
		return 1
	i = 0
	while i < len(arguments):
		for character in arguments[i]:
			character_count[character] = character_count.get(character, 0) + 1
		i += 1
	keys_list = [*character_count.keys()]
	keys_list.sort()
	print("Char count:")
	for key in keys_list:
		value = character_count[key]
		if key != " ":
			print(f"{key} = {value}")
		else:
			print(f"  = {value}")

if __name__ == "__main__":
	main()
