sum = 0
for numbers in range(3):
	number = int(input('Enter numbers:'))
	sum += numbers
	sum *= numbers
	average = numbers / len(str(numbers))
print('The sum of number is:' , sum)
print('The product of number is:' , sum )
print('The average number is: ' , average)
