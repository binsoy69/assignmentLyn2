""" A program to compute the factorial of a number """


print(' ** Find the factorial of a number ** ')

num = int(input('Enter a number: ')) # get the user input

factorial = 1 # initiate the variable to 1

for i in range(1, num + 1): # loop from 1 to specified number
  factorial = factorial * i # get the factorial

print('The factorial of ', num, ' is ', factorial) # print the answer


