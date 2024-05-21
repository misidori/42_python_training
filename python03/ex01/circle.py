class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle:
	def __init__(self, center, radius):
		self.center = Point(*center)
		self.radius = radius

	def __str__(self):
		return f"Circle of center at ({self.center.x}, {self.center.y}) and radius {self.radius}"

def main():
	obj = Circle((150, 100), 75)
	print(obj)

if __name__ == "__main__":
	main()


# Examples:
# 42~ > python circle.py
# Circle of center (150, 100) and radius 75
# 42~ >
# 42~ > python -c 'from circle import Circle; print(Circle((1,1),4))'
# Circle of center (1, 1) and radius 4
# 42~ >
