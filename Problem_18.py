print('** A program that reads 10 integers into an array, computes the average, largest, and smallest numbers in the array')

numbers = []

for i in range(10):
  num = int(input('Enter an integer: '))
  numbers.append(num)

average = sum(numbers) / len(numbers)
print('The average of the integers is ', average)

largest = max(numbers)
print('The largest integer in the array is ', largest)

smallest = min(numbers)
print('The smallest integer in the array is ', smallest)