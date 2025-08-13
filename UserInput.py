passes = 0
failures = 0
invalid_inputs = 0

for student in range(10):
    result = 0
    while result != 1 and result != 2:
        result = int(input('Enter result (1 = pass, 2 = fail): '))
        if result != 1 and result != 2:
            print("Invalid input! Enter number  1 or 2.")
            invalid_inputs += 1

    if result == 1:
        passes += 1
    else:
        failures += 1

print("Number passed:", passes)
print("You failed:", failures)
print("Invalid attempts:", invalid_inputs)