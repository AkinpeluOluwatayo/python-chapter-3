number = int(input('Enter five number: '))

number1 = number // 10000
number2 = (number // 1000) % 10
number4 = (number // 10) % 10
number5 = number % 10

if number1 == number5 and number2 == number4:
    print("Yess It's a palindrome!")
else:
    print("Noo It's not a palindrome.")