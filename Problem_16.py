print('** A program that reads in real number and then outputs the area of a square and area of a circle **')

def square_area(s):
  return s ** 2

def circle_area(d):
  PI = 3.14
  area = ((d ** 2) * PI) / 4 
  return area


length = int(input('Enter a real number: '))

print('The area of the square is ', square_area(length))
print('The area of the circle is ', circle_area(length))