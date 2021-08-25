""" A program to list the numbers from 0 to 25, their squares, square roots, fourth power, and fourth root. The output is in a neat five-column format """

def main():
  numbers = []              # create a list for every output
  squared = []
  squareRoots = []
  fourthPowers = []
  fourthRoots = []

  for i in range(0, 26):    # iterate from 0 to 25
   numbers.append(i)        
   squared.append(getSquared(i))
   squareRoots.append(getSqrt(i))
   fourthPowers.append(get4thPower(i))
   fourthRoots.append(get4thRoot(i))

  titles = ['Numbers', 'Squares', 'Square Roots', 'Fourth Power', 'Fourth Root'] # titles for each column
  data = [titles] + list(zip(numbers, squared, squareRoots, fourthPowers, fourthRoots)) 

  # create the 5 column format
  for x, y in enumerate(data):
    line = '|'.join(str(z).ljust(12) for z in y)
    print(line)
    if x == 0:
      print('-' * len(line))

def getSquared(n):
  return n ** 2

def getSqrt(n):
  return round(n ** 0.5, 3)

def get4thPower(n):
  return n ** 4

def get4thRoot(n):
  return round(n ** 0.25, 3)

main()
