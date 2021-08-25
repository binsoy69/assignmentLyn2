""" A program that reads in a number N and then outputs the sum of the squares of the numbers from 1 to N """

def main():
  loop = True

  while loop:
    number = int(input('Enter a positive number: '))
    output = sum_of_squares(number)
    print('The sum of the squares from 1 to ', number, ' is ', output)
    
    cont = input('Press enter to continue or type "exit" to exit: ')
    if cont == 'exit':
      loop = False

def sum_of_squares(n):
  if n == 1:
    return 1
  else:
    return (n ** 2) + sum_of_squares(n-1)

# Run main function
main()