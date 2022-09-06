import math

for num in range(2,10000):
    sum = 1
    for factor in range(2, int(math.sqrt(num)) + 1):
        if (num % factor) == 0:
            sum += factor 
            if (num // factor) != factor:
                sum += num // factor
    if sum == num:
        print(num)


