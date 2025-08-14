Number = int(input("Enter a binary number: "))
decimal = 0
value = 1 

while binary > 0:
    digit = binary % 10       
    decimal += digit * value
             
