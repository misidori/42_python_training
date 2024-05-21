class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Student(Person):
	def __init__(self, first_name, last_name, degree_course = None):
		super().__init__(first_name, last_name)
		self.degree_course = degree_course

	def __str__(self):
		if self.degree_course:
			return f"{self.first_name} {self.last_name} is registered to {self.degree_course}"
		else:
			return f"{self.first_name} {self.last_name} is not registered to any course"

def main():
	first_name = input("Insert first name: ")
	last_name = input("Insert last name: ")
	is_student = input("Are you a student? (y/n)")
	while is_student != "y" and is_student != "n":
		is_student = input("Please type \"y\" or \"n\": ")
	if is_student == 'y':
		degree_course = input("Please insert your degree course: ")
		user = Student(first_name, last_name, degree_course)
	elif is_student == 'n':
		user = Person(first_name, last_name)
	print(user)

if __name__ == "__main__":
	main()
