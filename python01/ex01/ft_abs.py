def main():
	expression = input("Insert an expression: ")
	result = eval(expression)
	if result < 0:
		result *= -1
	print(f"The result is: {result}")

if __name__ == "__main__":
	main()
