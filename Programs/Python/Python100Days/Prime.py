import math

for num in range(2, 100):
    prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            prime = False
            break
    if prime == True:
        print(num)

