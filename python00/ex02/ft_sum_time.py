def main():
	hours = int(input("Insert hours: "))
	minutes = int(input("Insert minutes: "))
	seconds = int(input("Insert seconds: "))
	total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
	print(f"Total seconds: {total_seconds}")

if __name__ == "__main__":
	main()
