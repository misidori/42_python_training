import sys

def main():
	first_num = float(sys.argv[1])
	second_num = float(sys.argv[2])

	if first_num > second_num:
		print(f"{first_num} is greater than {second_num}")
	elif first_num == second_num:
		print(f"{first_num} is equal to {second_num}")
	else:
		print(f"{first_num} is less than {second_num}")

if __name__ == "__main__":
	main()
