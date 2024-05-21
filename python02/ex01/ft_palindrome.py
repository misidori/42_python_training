import sys

def is_palindrome(string):
	i = 0
	palindrome = True
	string_temp = string.replace(" ", "")
	while i < (len(string_temp)//2):
		if string_temp[i] != string_temp[-(i+1)]:
			palindrome = False
			break
		i += 1
	if palindrome == True:
		return True
	else:
		return False

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	argv = sys.argv[1]
	palindrome = True

	if argc != 1:
		print("Error! Insert just 1 string!")
		return 1
	palindrome = is_palindrome(argv)
	if palindrome == True:
		print(f"The string {argv} is palindrome")
	else:
		print(f"The string {argv} is not palindrome")

if __name__ == "__main__":
	main()
