print('A program that gives the user the choice of computing the area of any of the following: a circle, a square, a rectangle, or a triangle')

loop = True

while loop:
  print('Find the area of any of the following: ')
  print('Type "1" for area of circle')
  print('Type "2" for area of square')
  print('Type "3" for area of rectangle')
  print('Type "4" for area of triangle')
    
  choice = int(input('Enter your choice: '))

  if choice == 1: # circle area
    print('Get the area for circle')
    r = int(input('Enter the radius: '))
    PI = 3.14
    area = PI * r * r

  elif choice == 2: # square area
    print('Get the area for square')
    side = int(input('Enter the side: '))
    area = side ** 2

  elif choice == 3: # rectangle area
    print('Get the area for rectangle')
    l = int(input('Enter the length: '))
    w = int(input('Enter the width: '))
    area = l * w

  elif choice == 4: # triangle area
    print('Get the area for triangle')
    h = int(input('Enter the height: '))
    b = int(input('Enter the base: '))
    area = (h * b) / 2

  else: # only 1, 2, 3, and 4 are the valid choices
    output = 'Please enter a valid choice '

  print('The area is ', area)

  print('Do you want to find another area?')

  option = input('Type "yes" to continue or "no" to exit: ')

  if option == 'no':
    loop = False
  





