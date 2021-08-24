print('A program that will read in three integers and output a message telling whether exactly two of them are greater than 10')

print(' ** Please enter three integers **')

a = int(input('Enter 1st integer: '))
b = int(input('Enter 2nd integer: '))
c = int(input('Enter 3rd integer: '))

if(a > 10 and b > 10 and c > 10): # if all three int are greater than 10
  result = 'All three integers are greater than 10'
elif (a > 10 and b > 10): # if only a and b are greater than 10
  result = str(a) + ' and ' + str(b) + ' are greater than 10'
elif (b > 10 and c > 10): # if only b and c are greater than 10
  result = str(b) + ' and ' + str(c) + ' are greater than 10'
elif (a > 10 and c > 10): # if only a and c are greater than 10
  result = str(a) + ' and ' + str(c) + ' are greater than 10'
else: # if less than 2 is only greater than 10
  result = 'None or only one of the integers is greater than 10'

print(result)



