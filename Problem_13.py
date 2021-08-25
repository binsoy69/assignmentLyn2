""" A program to find the first three perfect numbers """

def main():
  perfect_numbers = []
  total = 0
  while total < 3:
    for i in range(1, 500):
      is_perfect = check_number(i)
      if is_perfect:
        perfect_numbers.append(i)
        total = total + 1

  print('The first three perfect numbers are ', perfect_numbers)

def check_number(n):
  sum = 0
  for i in range(1, n):
    if (n % i == 0):
      sum = sum + i
  
  if (sum == n):
    return True

# Run main function
main()