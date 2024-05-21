import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle:
	def __init__(self, center, radius):
		self.center = Point(*center)
		self.radius = radius

	def contains(self, *args):
		if len(args) == 1:
			point = args[0]
		elif len(args) == 2:
			point = Point(*args)
		distance = ((point.x - self.center.x)**2 + (point.y - self.center.y)**2)**0.5
		return distance <= self.radius

def main():
	arguments = sys.argv[1:]
	x = float(arguments[0])
	y = float(arguments[1])
	circle1 = Circle((0, 0), 1)
	result = circle1.contains(x, y)
	if result:
		print(f"The Point ({x}, {y}) lies in the Circle of center (0, 0) and radius 1")
	else:
		print(f"The Point ({x}, {y}) lies out of the Circle of center (0, 0) and radius 1")

if __name__ == "__main__":
	main()
