print('A program that reads in the lenghts of the two sides of a right triangle and computes the hypotenuse of the triangle')
  
print(' ** Give the two sides of a right triangle **')
  
a = int(input('Side 1: '))  # get the length of side a
b = int(input('Side 2: ')) # get the length of side b

cSquared = (a ** 2) + (b ** 2)  # get the sum of a squared and b squared
hypotenuse = cSquared ** 0.5  # get the square root of c squared 

print('The hypotenuse of the right triangle is ', hypotenuse) # print the result


