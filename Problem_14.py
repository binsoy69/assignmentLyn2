""" A program to find all the integer solutions to the equation 4x + 3y - 9z = 5 for values of x, y, and z between 0 and 100. """


solutions = 0

for x in range(0, 101):
  for y in range(0, 101):
    for z in range(0, 101):
      if (4 * x + 3 * y - 9 * z == 5):
        solutions += 1

        print('(', x,',', y, ',', z, ')')

print('There are', solutions, ' solutions to this problem')

