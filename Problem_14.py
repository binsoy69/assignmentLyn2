""" A program to find all the integer solutions to the equation 4x + 3y - 9z = 5 for values of x, y, and z between 0 and 100. """


solutions = 0 

for x in range(101): # loop from 0 to 100 for the x values 
  for y in range(101): # loop from 0 to 100 for the y values
    for z in range(101): # loop from 0 to 100 for the z values
      if (4 * x + 3 * y - 9 * z == 5): # if the values for x, y, and z satisfies the equation
        solutions += 1 # then add to the total number of solutions

        print(f'({x},{y},{z})') # print the values of x, y, z for correct answers

print('There are', solutions, ' solutions to this problem') # print the total number of solution

