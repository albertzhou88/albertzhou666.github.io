def is_palindrome(forward):
    temp = forward
    backward = 0
    while temp > 0:
        backward = backward * 10 + temp % 10
        temp //= 10
    return backward == forward

num = int(input('Input a number: '))
print(is_palindrome(num))
