import Gcd

def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)