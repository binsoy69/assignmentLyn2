print('** A program to compute the circumference of a circle **')

def get_circum(r, c):
  PI = 3.14
  c = 2 * PI * r
  return c

c = 0.0
radius = float(input('Enter the radius: '))
circumference = get_circum(radius, c)

print('The circumference of the circle is ', circumference)