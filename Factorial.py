number = int(input("Enter a  integer: "))
factorial = 1
for index in range(1, number + 1):
    factorial *= index

print(number, "factorial is", factorial)