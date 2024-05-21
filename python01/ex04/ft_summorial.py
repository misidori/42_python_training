import sys

def main():
	arguments = sys.argv[1:]
	argc = len(arguments)
	if argc != 1:
		print("Error! Usage: python3 ft_summorial.py <n>")
		return 1
	else:
		num = int(sys.argv[1])
		if num < 0:
			print("Error! n must be >=0")
		else:
			result = 0
			while num >= 0:
				result += num
				num -= 1
			print(f"The sum is: {result}")

if __name__ == "__main__":
	main()
