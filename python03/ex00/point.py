import math

class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

def main():
	input1 = input("Insert the coordinates of the first point: ")
	input2 = input("Insert the coordinates of the second point: ")

	tupla1 = input1.split(',')
	tupla2 = input2.split(',')
	point1 = Point(tupla1[0], tupla1[1])
	point2 = Point(tupla2[0], tupla2[1])

	distance = ((point2.x - point1.x)**2 + (point2.y - point1.y)**2) ** 0.5
	print("Their distance is: " + str(distance))

if __name__ == "__main__":
	main()

