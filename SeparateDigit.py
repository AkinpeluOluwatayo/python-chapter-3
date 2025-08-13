number = 12345
divisor = 10000 

while divisor > 0:
    digit = number // divisor     
    print(digit, end='  ')         
    number %= divisor              
    divisor //= 10 