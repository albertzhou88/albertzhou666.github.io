# Fibonacci sequence

a = 0
b = 1
for i in range(20):
    c = a + b
    a = b
    b = c
    print(a, end=' ')
print('\n')


