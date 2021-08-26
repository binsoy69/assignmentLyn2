#print('** A program that takes a value x as an input and outputs this sum for n taken to be each of the values 1 to 100. **')

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)


x = float(input("Enter the value of x: ")) 
n = int(input("Enter the number of terms from 1 to 100: ")) 

sum1 = 1

for i in range(2,n+1): 
    sum1 = sum1 +x + ((x**i)/factorial(i)) 

print("The sum of series is",round(sum1,2)) 