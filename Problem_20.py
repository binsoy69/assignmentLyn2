print('** A program that reads in an m by n matrix, then reads in an n by p matrix, and then computes the product matrix and displays the two matrices as well as their product matrix on the screen **')

# three needed values
m = int(input('Enter the row number for matrix1: ')) 
n = int(input('Enter the column number for matrix1 / row number for matrix2: ')) 
p = int(input('Enter the column number for matrix2: ')) 

print('Enter the elements for matrix1: ')
matrix1 = [[int(input()) for i in range(n)] for j in range(m)] # matrix1 m row by n column
print('matrix1: ') 
# print the elements using nested for loops
for i in range(m):
  for j in range(n):
    print(format(matrix1[i][j], "<3"), end="")
  print()

print('Enter the elements for matrix2: ')
matrix2 = [[int(input()) for i in range(p)] for j in range(n)]  # matrix2 n row by p column
print('matrix2: ')
for i in range(n):
  for j in range(p):
    print(format(matrix2[i][j], "<3"), end="")
  print()

result = [[0 for i in range(p)] for j in range(m)] # resulting matrix m row by p column

for i in range(m):
  for j in range(p):
    for k in range(n):
      result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]


print('The result is: ')
for i in range(m):
  for j in range(p):
    print(format(result[i][j], "<3"), end="")
  print()
