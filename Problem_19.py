print('** A program that allows the user to type in up to 10 positive numbers and then echoes back the numbers typed in but in reverse order **')

print('Enter 10 positive numbers')

numbers = []

for i in range(10):
  real_num = float(input('Enter a number: '))
  numbers.append(real_num)

numbers.reverse()
print(numbers)