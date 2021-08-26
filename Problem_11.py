""" A program that reads in a number N and then outputs the sum of the squares of the numbers from 1 to N """


loop = True

while loop: # while loop is still true, run the program
  n = int(input('Enter a positive number: ')) # get the user input

  output = 0
  for i in range(1, n+1): # loop from 1 to n
    output = output + (i ** 2) # get the sum of the squares

  print('The sum of the squares from 1 to ', n, ' is ', output) # print the sum
    
  cont = input('Press enter to continue or type "exit" to exit: ') # ask the user 
  if cont == 'x': # is the user typed in 'x' 
    loop = False # the program will end
