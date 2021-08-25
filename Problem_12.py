""" A program to compute the factorial of a number """

def main():
  print(' ** Find the factorial of a number ** ')
  num = int(input('Enter a number: '))
  output = factorial(num)
  print('The factorial of ', num, ' is ', output)

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)


# Run main function
main()