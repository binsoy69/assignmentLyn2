""" A program to find the first three perfect numbers """

def main():
  perfect_numbers = []    # create a list for the perfect 

  total = 0   # initiate total number of perfect numbers to 0
  while total < 3:  # while perfect number is lesser than 3
    for i in range(1, 500): # loop from 1 to 500
      is_perfect = check_number(i) # check each number
      if is_perfect: # if number is perfect
        perfect_numbers.append(i) # add to the list
        total = total + 1 # increment total

  print('The first three perfect numbers are ', perfect_numbers) # print the first three perfect numbers
 
def check_number(n): # function for checking a perfect number
  sum = 0   # initiate sum 
  for i in range(1, n): # loop from 1 to n
    if (n % i == 0): # if n is divisible by the index
      sum = sum + i # add to sum 
  
  if (sum == n):  # if the sum is equal to n 
    return True # then it is a perfect number

# Run main function
main()