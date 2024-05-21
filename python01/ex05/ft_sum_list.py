def sum_list(my_list=0):
	total = 0
	i = 0
	while i < len(my_list):
		total += my_list[i]
		i += 1
	return total

def main():
	my_list = []
	num = 1
	while num != 0:
		num = int(input("Insert integer: "))
		if num != 0:
			my_list.append(num)
	result = sum_list(my_list)
	print(f"The sum is {result}")

if __name__ == "__main__":
	main()
