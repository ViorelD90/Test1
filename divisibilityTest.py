
countdown = 100
for num in range(countdown, 0, -1):
    if num % 5 == 0 and num % 3 == 0:
        print(num, "Testing")
    elif num % 3 == 0:
        print(num, "Software")
    elif num % 5 == 0:
        print(num, "Agile")
    else:
        print(num)

