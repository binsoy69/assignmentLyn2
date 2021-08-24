print('A program that reads in the lengths of the three sides of a triangle and outputs the area of the triangle')
  
print(' ** Enter the lengths of the three sides of the triangle **')

a = int(input('Side 1: '))
b = int(input('Side 2: '))
c = int(input('Side 3: '))

s = (a+b+c) / 2     # get the value for s variable 
area = (s*(s - a)*(s - b)*(s - c)) ** 0.5   # use the formula for getting the area

print('The area of the triangle is ', area)



